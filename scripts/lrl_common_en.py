"""Shared helpers for the low-resource-language LLM literature library.

Adapted (copied, then edited) from /root/large_model_multimodal_literature/scripts/lmm_common_en.py.
stdlib only, plus pypdf loaded from LRL_PYLIB (default /root/.cache/lrl_lit/pylib).
Run every script with `python3 -I`.
"""
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
SEEDS = SCRIPTS / "seeds"
ANNOT = SCRIPTS / "annotations"
STATE = SCRIPTS / "state"
RESULTS = STATE / "results"
WORK = SCRIPTS / "work"
PAPERS = ROOT / "papers"
PYLIB = os.environ.get("LRL_PYLIB", "/root/.cache/lrl_lit/pylib")
STAGING = Path(os.environ.get("LRL_STAGING", "/root/.cache/lrl_lit/staging"))
# shared with the sibling libraries on this host so the combined request rate per host stays low
LOCK_DIR = Path(os.environ.get("LRL_LOCK_DIR", "/tmp/lmm_ratelimit"))

RETRIEVAL_DATE = "2026-10-29"
WINDOW_START = "2023-10-29"  # retrieval date minus three years

UA = "lrl-literature-collector/1.0 (academic literature catalogue; low request rate)"

# minimum seconds between requests per host (shared across processes)
HOST_INTERVAL = {"export.arxiv.org": 5.0, "arxiv.org": 3.0, "api.openalex.org": 1.0}
DEFAULT_INTERVAL = 3.0

CATEGORIES = [
    ("01", "math_learning_foundations", "数学与学习基础"),
    ("02", "nlp_linguistics_foundations", "自然语言处理与语言学基础"),
    ("03", "multilingual_lowres_llm", "多语言及低资源语言大模型"),
    ("04", "corpus_sources_governance", "语料来源、治理与许可"),
    ("05", "data_processing_quality", "数据处理与质量"),
    ("06", "tokenization_vocab_arch", "分词、词表与模型架构"),
    ("07", "pretraining_continual", "预训练与持续预训练"),
    ("08", "instruction_tuning_peft", "指令微调与参数高效适配"),
    ("09", "synthetic_translation_distill", "合成数据、翻译与蒸馏"),
    ("10", "preference_alignment_safety", "偏好对齐与安全"),
    ("11", "reasoning_longctx_tools", "推理、长上下文与工具调用"),
    ("12", "rag_local_knowledge", "检索增强与本地知识"),
    ("13", "assistants_applications", "对话助手与实际应用"),
    ("14", "code_models_agents", "代码模型与编程智能体"),
    ("15", "evaluation_human", "评测与人工评价"),
    ("16", "efficient_train_deploy", "高效训练、推理与部署"),
    ("17", "university_courses", "大学官方教材与完整课程讲义"),
    ("18", "books", "完整教科书、专著与参考书"),
]
CAT_BY_CODE = {c: (c, s, n) for c, s, n in CATEGORIES}


def cat_key(code):
    c, s, _ = CAT_BY_CODE[code]
    return f"{c}_{s}"


def load_pypdf():
    if PYLIB not in sys.path:
        sys.path.insert(0, PYLIB)
    import pypdf  # noqa
    import logging
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    return pypdf


# ---------------------------------------------------------------- json state
@contextlib.contextmanager
def locked(name):
    """Exclusive inter-process lock (held for the block)."""
    STATE.mkdir(parents=True, exist_ok=True)
    with open(STATE / f".{name}_en.lock", "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def load_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".tmp{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, path)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- http
def wait_host(host, interval=None):
    interval = interval if interval is not None else HOST_INTERVAL.get(host, DEFAULT_INTERVAL)
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", host), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        try:
            nxt = float(raw) if raw else 0.0
        except ValueError:
            nxt = 0.0
        delay = nxt - time.time()
        if delay > 0:
            time.sleep(delay)
        f.seek(0)
        f.truncate()
        f.write(str(time.time() + interval))
        f.flush()


def push_backoff(host, seconds):
    """Make every process wait `seconds` before the next request to host."""
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", host), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        f.truncate()
        f.write(str(time.time() + seconds))


STOP_CODES = {401, 402, 403, 404, 410, 451}


class HttpError(Exception):
    def __init__(self, code, msg):
        super().__init__(f"HTTP {code}: {msg}")
        self.code = code


def http_get(url, dest=None, max_bytes=150 * 1024 * 1024, timeout=120, tries=3, accept="*/*"):
    """GET with per-host rate limit. Returns bytes, or writes to dest and returns
    (status, final_url, content_type, nbytes). Never retries 4xx stop codes."""
    host = urllib.parse.urlparse(url).netloc
    last = None
    for attempt in range(tries):
        wait_host(host)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                ctype = r.headers.get("Content-Type", "")
                clen = r.headers.get("Content-Length")
                if clen and int(clen) > max_bytes:
                    raise HttpError(413, f"too large ({int(clen)} bytes)")
                if dest is None:
                    data = r.read(max_bytes + 1)
                    if len(data) > max_bytes:
                        raise HttpError(413, "too large")
                    return data
                n = 0
                with open(dest, "wb") as out:
                    while True:
                        chunk = r.read(1 << 20)
                        if not chunk:
                            break
                        n += len(chunk)
                        if n > max_bytes:
                            raise HttpError(413, "too large")
                        out.write(chunk)
                return (r.status, r.geturl(), ctype, n)
        except urllib.error.HTTPError as e:
            last = HttpError(e.code, str(e.reason))
            if e.code in STOP_CODES:
                raise last
            if e.code in (429, 503):
                ra = e.headers.get("Retry-After") if e.headers else None
                wait = int(ra) if ra and ra.isdigit() else 60 * (attempt + 1)
                push_backoff(host, min(wait, 300))
        except HttpError as e:
            raise e
        except Exception as e:  # network errors
            last = HttpError(0, repr(e))
            time.sleep(5 * (attempt + 1))
    raise last


# ---------------------------------------------------------------- text utils
def fold(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(ch for ch in s if not unicodedata.combining(ch))


STOP = {"a", "an", "the", "of", "for", "and", "in", "on", "to", "with", "via", "by", "is",
        "are", "from", "at", "as", "or", "its", "we", "towards", "toward"}


def tokens(s):
    s = fold(s).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return [t for t in s.split() if t]


def title_similarity(a, b):
    import difflib
    na, nb = " ".join(tokens(a)), " ".join(tokens(b))
    return difflib.SequenceMatcher(None, na, nb).ratio()


def title_in_text(title, text):
    """Fraction of significant title tokens that appear in text."""
    tt = [t for t in tokens(title) if t not in STOP] or tokens(title)
    body = set(tokens(text))
    # also allow hyphen-joined words split in text
    joined = " ".join(tokens(text))
    hit = sum(1 for t in tt if t in body or t in joined)
    return hit / max(1, len(tt))


def surname(name):
    name = fold(name or "").strip()
    if not name:
        return ""
    if "," in name:
        return name.split(",")[0].strip()
    parts = name.split()
    return parts[-1] if parts else ""


def short_title(title, maxlen=36):
    t = fold(title)
    if ":" in t:
        head = t.split(":")[0].strip()
        if 2 <= len(head) <= 30 and len(head.split()) <= 4:
            words = re.findall(r"[A-Za-z0-9]+", head)
            s = "".join(w[:1].upper() + w[1:] for w in words)
            if s:
                return s[:maxlen]
    words = [w for w in re.findall(r"[A-Za-z0-9]+", t) if w.lower() not in STOP]
    out = ""
    for w in words:
        cand = out + (w[:1].upper() + w[1:])
        if len(cand) > maxlen:
            break
        out = cand
        if len(out) >= 24:
            break
    return out or "Untitled"


def safe_name(s):
    return re.sub(r"[^A-Za-z0-9]+", "", fold(s)) or "Anon"
