"""Shared helpers for the ML/DL literature library: paths, per-host rate limiting
(cross-process flock), HTTP GET with bounded retries, text normalisation, the
three-year window, and JSON load/save that is atomic (write temp + rename).

Rate limits: arXiv >= 4 s between requests (export API and PDF host share one
budget), Semantic Scholar >= 3 s, Crossref/OpenAlex >= 1 s, other hosts >= 2 s.
"""
import fcntl
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
CACHE = SCRIPTS / "cache"
LOCK_DIR = Path(os.environ.get("MLDL_LOCK_DIR", "/tmp/mldl_ratelimit"))
UA = "Mozilla/5.0 (compatible; mldl_literature/1.0; personal literature collection, low request rate)"

WINDOW_START, WINDOW_END = "2023-10-29", "2026-10-29"
CATS = {
    "C01": "机器学习基础",
    "C02": "传统机器学习",
    "C03": "无监督与表示学习",
    "C04": "深度学习基础与训练",
    "C05": "计算机视觉",
    "C06": "自然语言处理与大语言模型",
    "C07": "生成模型",
    "C08": "图机器学习",
    "C09": "强化学习与决策",
    "C10": "可靠性与评测",
    "C11": "大学课程教材与讲义",
    "C12": "教科书、专著与参考书",
}
INTERVAL = {"arxiv.org": 4.0, "api.semanticscholar.org": 3.0, "api.crossref.org": 1.0,
            "api.openalex.org": 1.0}

STOP = {"a", "an", "the", "of", "for", "and", "in", "on", "with", "to", "via", "by", "is", "are",
        "from", "at", "as", "its", "do", "how", "can", "using", "based", "towards", "toward"}


def host_key(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return "arxiv.org" if host.endswith("arxiv.org") else host


def wait(key, interval):
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", key), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        delay = interval - (time.time() - (float(raw) if raw else 0.0))
        if delay > 0:
            time.sleep(delay)
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))


def http(url, data=None, accept="*/*", timeout=90, tries=3, headers=None):
    """Return (status, body_bytes, final_url, content_type). 4xx other than 429 is not retried."""
    key = host_key(url)
    err = ""
    for attempt in range(tries):
        wait(key, INTERVAL.get(key, 2.0))
        try:
            h = {"User-Agent": UA, "Accept": accept, **(headers or {})}
            req = urllib.request.Request(url, data=data, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), r.geturl(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            if 400 <= e.code < 500:
                return e.code, b"", url, ""
        except Exception as e:  # network error / timeout
            err = repr(e)[:200]
        time.sleep(8 * (attempt + 1))
    return None, err.encode(), url, ""


def fold(s):
    s = re.sub(r"[{}\\$]", "", s or "")
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", fold(strip_tags(s)).lower())


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", fold(strip_tags(s)).lower()) if t not in STOP and len(t) > 1]


def title_similarity(a, b):
    ta, tb = set(tokens(a)), set(tokens(b))
    return len(ta & tb) / max(1, len(ta | tb))


def title_in_text(title, text):
    """Fraction of title tokens present in text (whitespace/punctuation-insensitive)."""
    tt = tokens(title)
    blob = re.sub(r"[^a-z0-9]", "", fold(text).lower())
    return sum(1 for t in tt if t in blob) / len(tt) if tt else 0.0


def surname(name):
    parts = fold(name).replace(",", " ").split()
    return re.sub(r"[^A-Za-z]", "", parts[-1]) if parts else "Anon"


def short_title(title, n=4):
    title = fold(strip_tags(title))
    head = title.split(":")[0].strip()
    if ":" in title and 1 <= len(head.split()) <= 3:
        words = re.findall(r"[A-Za-z0-9]+", head)
    else:
        words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if w.lower() not in STOP][:n]
    return "".join(w[:1].upper() + w[1:] for w in words)[:40] or "Untitled"


def window_status(date):
    """date is YYYY, YYYY-MM or YYYY-MM-DD."""
    if not date:
        return "待核实"
    lo = (date + "-01-01")[:10]
    hi = (date + "-12-31")[:10] if len(date) == 4 else (date + "-31")[:10]
    if lo >= WINDOW_START and hi <= WINDOW_END:
        return "近三年"
    if hi < WINDOW_START:
        return "三年前"
    return "待核实（日期精度不足）"


def load(path, default):
    path = Path(path)
    return json.loads(path.read_text()) if path.exists() else default


def save(path, obj):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1))
    os.replace(tmp, path)
