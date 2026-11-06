#!/usr/bin/env python3
"""Engineering area: official documentation sets and reference implementations (source only).

Seeds:   scripts/seeds/19_engineering_seed_cn.json   (list of projects, see guides in README_cn.md)
Results: scripts/state/results/19_engineering_en.json

For every project the repository is fetched at ONE pinned ref (tag or commit) with a shallow git
fetch (no hooks, no submodules, no LFS smudge); repository code is never executed. Then:
  1. files that are weights / datasets / archives / binaries / build output, or larger than
     MAX_FILE_BYTES, are dropped and listed in the result record (excluded_files);
  2. reference_code/<Name>_<sha7>_original_en.tar.gz  = the filtered tree in its ORIGINAL layout
     (deterministic tar: sorted, mtime 0, uid 0);
  3. reference_code/<Name>_<sha7>_en/  = a COPY in which every file name carries a language suffix
     before its extension (foo.py -> foo_en.py, README_zh.md -> README_zh_cn.md); file contents are
     unchanged; this copy is for reading only and is NOT a runnable repository;
     reference_code/<Name>_<sha7>_en/path_map_en.csv maps original -> renamed path + sha256;
  4. if the seed names a documentation source tree ("docs": {"path": "docs"} or a separate repo),
     engineering_docs/<Name>_docs_<sha7>_en/ gets the renamed copy of that subtree, and the doc
     table of contents (mkdocs.yml nav, HF _toctree.yml, Sphinx toctree, docusaurus sidebars, or
     mint.json/docs.json) is resolved against the files to judge completeness.

Usage:
  python3 -I scripts/engineering_en.py fetch  [--eid E-03] [--retry-failed]
  python3 -I scripts/engineering_en.py status
  python3 -I scripts/engineering_en.py recheck-docs [--eid E-03]   # re-run TOC check from the saved archive
  python3 -I scripts/engineering_en.py refs <github_url>     # list tags / default-branch head (no clone)
"""
import argparse
import csv
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402

SEEDS_PATH = C.SEEDS / "19_engineering_seed_cn.json"
RESULTS_PATH = C.RESULTS / "19_engineering_en.json"
CODE_DIR = C.ROOT / "reference_code"
DOCS_DIR = C.ROOT / "engineering_docs"
MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_TREE_BYTES = 400 * 1024 * 1024

EXCLUDE_EXT = {
    ".safetensors", ".bin", ".pt", ".pth", ".ckpt", ".gguf", ".ggml", ".onnx", ".h5", ".hdf5", ".pb",
    ".tflite", ".mlmodel", ".npz", ".npy", ".pkl", ".pickle", ".joblib", ".parquet", ".arrow", ".feather",
    ".tar", ".tgz", ".gz", ".bz2", ".xz", ".zst", ".zip", ".7z", ".rar", ".whl", ".egg", ".jar",
    ".so", ".dylib", ".dll", ".exe", ".a", ".o", ".obj", ".lib", ".class", ".pyc", ".pyo",
    ".mp4", ".mov", ".avi", ".webm", ".mkv", ".wav", ".mp3", ".flac", ".ogg", ".m4a",
    ".sqlite", ".db", ".lmdb", ".idx", ".msgpack", ".model", ".spm", ".vocab",
}
EXCLUDE_DIRS = {".git", "node_modules", "build", "dist", "__pycache__", ".venv", "venv", ".tox",
                "site-packages", ".mypy_cache", ".pytest_cache", "target", ".next", ".cache"}
LANG_RULES = [  # (regex on the relative path, suffix)
    (re.compile(r"(?i)(^|[/_.-])(zh|zh-cn|zh_cn|zh-hans|zh-hant|zh_tw|chinese|cn)([/_.-]|$)"), "cn"),
    (re.compile(r"(?i)(^|[/_.-])(ja|jp|japanese)([/_.-]|$)"), "ja"),
    (re.compile(r"(?i)(^|[/_.-])(ko|kr|korean)([/_.-]|$)"), "ko"),
]


def load_seeds():
    seeds = C.load_json(SEEDS_PATH, [])
    ids = [s["eid"] for s in seeds]
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        sys.exit(f"duplicate eid: {sorted(dup)}")
    return seeds


def git(args, cwd=None, timeout=900):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_LFS_SKIP_SMUDGE="1", GIT_CONFIG_NOSYSTEM="1")
    cmd = ["git", "-c", "core.hooksPath=/dev/null", "-c", "protocol.file.allow=never",
           "-c", "advice.detachedHead=false"] + args
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:3])} failed: {p.stderr.strip()[-400:]}")
    return p.stdout


def fetch_repo(url, ref, dest):
    """Shallow fetch of exactly one ref (tag, branch or full commit sha) into dest."""
    C.wait_host("github.com", 2.0)
    dest.mkdir(parents=True)
    git(["init", "-q"], cwd=dest)
    git(["remote", "add", "origin", url], cwd=dest)
    git(["fetch", "-q", "--depth", "1", "--no-tags", "origin", ref], cwd=dest)
    git(["checkout", "-q", "FETCH_HEAD"], cwd=dest)
    sha = git(["rev-parse", "HEAD"], cwd=dest).strip()
    date = git(["log", "-1", "--format=%cI"], cwd=dest).strip()
    return sha, date


def lang_suffix(rel):
    for rx, suf in LANG_RULES:
        if rx.search(rel):
            return suf
    return "en"


def renamed(rel):
    p = Path(rel)
    name = p.name
    suf = lang_suffix(rel)
    if re.search(r"_(en|cn|cn_en|ja|ko)(\.[^.]+)?$", name):
        new = name  # already suffixed
    elif name.startswith(".") and name.count(".") == 1:
        new = f"{name}_{suf}"
    elif "." in name.lstrip("."):
        stem, ext = name.rsplit(".", 1)
        new = f"{stem}_{suf}.{ext}"
    else:
        new = f"{name}_{suf}"
    return str(p.with_name(new))


def filter_tree(root):
    """Delete excluded files in place; return (kept, excluded) lists of relative paths."""
    kept, excluded = [], []
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        rel_dir = Path(dirpath).relative_to(root)
        for d in list(dirnames):
            if d in EXCLUDE_DIRS:
                excluded.append({"path": str(rel_dir / d) + "/", "reason": "excluded directory"})
                shutil.rmtree(Path(dirpath) / d, ignore_errors=True)
                dirnames.remove(d)
        for f in filenames:
            p = Path(dirpath) / f
            rel = str(rel_dir / f)
            if p.is_symlink():
                excluded.append({"path": rel, "reason": "symlink"})
                p.unlink()
                continue
            size = p.stat().st_size
            ext = p.suffix.lower()
            if ext in EXCLUDE_EXT:
                excluded.append({"path": rel, "reason": f"excluded type {ext}", "bytes": size})
                p.unlink()
            elif size > MAX_FILE_BYTES:
                excluded.append({"path": rel, "reason": f"larger than {MAX_FILE_BYTES} bytes", "bytes": size})
                p.unlink()
            else:
                kept.append(rel)
    return sorted(kept), excluded


def det_tar(src_root, out_path, prefix):
    with tarfile.open(out_path, "w:gz", format=tarfile.PAX_FORMAT) as tf:
        for rel in sorted(str(p.relative_to(src_root)) for p in src_root.rglob("*") if p.is_file()):
            ti = tf.gettarinfo(str(src_root / rel), arcname=f"{prefix}/{rel}")
            ti.mtime, ti.uid, ti.gid, ti.uname, ti.gname = 0, 0, 0, "", ""
            with open(src_root / rel, "rb") as f:
                tf.addfile(ti, f)


def renamed_copy(src_root, rels, out_dir):
    out_dir.mkdir(parents=True)
    rows = []
    for rel in rels:
        new = renamed(rel)
        dst = out_dir / new
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src_root / rel, dst)
        rows.append((rel, new, C.sha256_file(dst)))
    with open(out_dir / "path_map_en.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["original_path", "renamed_path", "sha256"])
        w.writerows(rows)
    return rows


def detect_license(root):
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING", "LICENSE-APACHE", "LICENSE-MIT"):
        p = root / name
        if p.is_file():
            t = p.read_text("utf-8", "replace")[:3000]
            for rx, spdx in [(r"Apache License,?\s+Version 2\.0", "Apache-2.0"), (r"MIT License|Permission is hereby granted, free of charge", "MIT"),
                             (r"BSD 3-Clause|Redistribution and use in source and binary forms.*?Neither the name", "BSD-3-Clause"),
                             (r"BSD 2-Clause", "BSD-2-Clause"), (r"GNU AFFERO GENERAL PUBLIC LICENSE", "AGPL-3.0"),
                             (r"GNU LESSER GENERAL PUBLIC LICENSE", "LGPL"), (r"GNU GENERAL PUBLIC LICENSE\s+Version 3", "GPL-3.0"),
                             (r"GNU GENERAL PUBLIC LICENSE\s+Version 2", "GPL-2.0"), (r"Mozilla Public License", "MPL-2.0"),
                             (r"Creative Commons Attribution 4\.0", "CC-BY-4.0")]:
                if re.search(rx, t, re.S):
                    return {"file": name, "detected": spdx}
            return {"file": name, "detected": "unrecognized (read file)"}
    return {"file": None, "detected": "no license file at repo root"}


DOC_EXT = r"\.(md|mdx|rst|ipynb|txt|html|markdown)$"


def _rst_toctrees(text):
    """Entries of every `.. toctree::` (RST) and ```{toctree} / :::{toctree} (MyST) block."""
    out = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"\s*\.\. toctree::", ln):
            ind = len(ln) - len(ln.lstrip())
            i += 1
            while i < len(lines) and (not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > ind):
                out.append(lines[i].strip())
                i += 1
            continue
        m = re.match(r"\s*(`{3,}|:{3,})\s*\{toctree\}", ln)
        if m:
            fence = m.group(1)
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(fence):
                out.append(lines[i].strip())
                i += 1
        i += 1
    refs = []
    for x in out:
        if not x or x.startswith(":") or "://" in x or x in ("self", "genindex", "modindex", "search") or "*" in x:
            continue
        m = re.search(r"<([^>]+)>\s*$", x)
        refs.append((m.group(1) if m else x).strip())
    return refs


def _json_pages(obj, acc):
    """Mintlify docs.json/mint.json and fumadocs meta.json: strings inside any "pages" list."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "pages" and isinstance(v, list):
                for it in v:
                    if isinstance(it, str):
                        acc.append(it)
                    else:
                        _json_pages(it, acc)
            else:
                _json_pages(v, acc)
    elif isinstance(obj, list):
        for it in obj:
            _json_pages(it, acc)


def toc_check(docs_root, repo_root=None):
    """Resolve navigation/TOC entries against the saved files (best effort, no execution).
    Every supported TOC kind found is evaluated; the kind with most entries decides. A doc set
    counts as complete when >= min ratio of entries resolve AND the TOC is not trivially small
    (>= 10 entries or >= 50% of the doc source files). Navigation generated from the directory
    tree itself (docusaurus 'autogenerated', Jekyll front-matter nav_order) is recorded as such."""
    import json as _json
    files = [str(p.relative_to(docs_root)) for p in docs_root.rglob("*") if p.is_file()]
    stems = {re.sub(DOC_EXT, "", f).lower() for f in files}
    repo_stems, docs_rel = set(), ""
    if repo_root is not None:
        docs_rel = str(docs_root.relative_to(repo_root))
        repo_stems = {re.sub(DOC_EXT, "", str(p.relative_to(repo_root))).lower() for p in repo_root.rglob("*") if p.is_file()}
    dir_prefixes = {s.rsplit("/", 1)[0] for s in stems if "/" in s}
    for d_ in list(dir_prefixes):
        while "/" in d_:
            d_ = d_.rsplit("/", 1)[0]
            dir_prefixes.add(d_)
    bases = {}
    for st in stems:
        bases.setdefault(st.rsplit("/", 1)[-1], st)
    kinds = {}

    def add(kind, ref):
        if ref:
            kinds.setdefault(kind, []).append(ref)
    for tp in docs_root.rglob("_toctree.yml"):
        base = tp.parent.relative_to(docs_root)
        for m in re.findall(r"^\s*-?\s*local:\s*([^\s#]+)", tp.read_text("utf-8", "replace"), re.M):
            add("hf_toctree", str(base / m.strip("'\"")))
    for mp in [docs_root / n for n in ("mkdocs.yml", "mkdocs.yaml")] + [docs_root.parent / n for n in ("mkdocs.yml", "mkdocs.yaml")] + \
              [docs_root.parent.parent / n for n in ("mkdocs.yml", "mkdocs.yaml")]:
        if mp.is_file():
            t = mp.read_text("utf-8", "replace")
            nav = t.split("\nnav:", 1)[1] if "\nnav:" in t else ""
            nav = re.split(r"\n[A-Za-z_]+:", nav, maxsplit=1)[0]
            for m in re.findall(r"([A-Za-z0-9_./-]+\.(?:md|ipynb))\b", nav):
                add("mkdocs_nav", re.sub(rf"^{re.escape(docs_root.name)}/", "", m))
    for np_ in list(docs_root.rglob(".nav.yml")) + list(docs_root.rglob(".pages")):
        base = np_.parent.relative_to(docs_root)
        for m in re.findall(r"([A-Za-z0-9_./-]+\.(?:md|ipynb))\b", np_.read_text("utf-8", "replace")):
            add("mkdocs_awesome_nav", str(base / m))
    for f in files:
        if re.search(r"\.(rst|md)$", f):
            try:
                t = (docs_root / f).read_text("utf-8", "replace")
            except Exception:
                continue
            if "toctree" not in t:
                continue
            base = Path(f).parent
            for r_ in _rst_toctrees(t):
                add("sphinx_toctree", r_.lstrip("/") if r_.startswith("/") else str(base / r_))
    for jp in [docs_root / "docs.json", docs_root / "mint.json"]:
        if jp.is_file():
            acc = []
            try:
                _json_pages(_json.loads(jp.read_text("utf-8", "replace")), acc)
            except Exception:
                pass
            for a in acc:
                add("mintlify_" + jp.stem, a)
    for mj in docs_root.rglob("meta.json"):
        acc = []
        try:
            _json_pages(_json.loads(mj.read_text("utf-8", "replace")), acc)
        except Exception:
            pass
        base = mj.parent.relative_to(docs_root)
        for a in acc:
            if not a.startswith(("---", "...", "[", "http")):
                add("fumadocs_meta", str(base / a.lstrip("!")))
    for sj in docs_root.rglob("sidebar*.json"):
        base = sj.parent.relative_to(docs_root)
        for m in re.findall(r'"source"\s*:\s*"([^"]+)"', sj.read_text("utf-8", "replace")):
            add("sidebar_json_source", str(base / m))
    autogen = None
    for sp in list(docs_root.rglob("sidebars.js")) + list(docs_root.rglob("sidebars.ts")) + \
              [docs_root.parent / "sidebars.js", docs_root.parent / "sidebars.ts"]:
        if sp.is_file():
            t = sp.read_text("utf-8", "replace")
            if re.search(r"type:\s*['\"]autogenerated['\"]", t):
                autogen = "docusaurus_autogenerated"
            for m in re.findall(r"(?:id:\s*|^\s*|[\[,]\s*)['\"]([A-Za-z0-9_./-]+)['\"]", t, re.M):
                if "/" in m or m in bases:
                    add("docusaurus_sidebars", m)
    for nv in list(docs_root.rglob("_data/*.yml")) + list(docs_root.parent.glob("_data/*.yml")):
        for m in re.findall(r"url:\s*['\"]?(/[^\s'\"]+)", nv.read_text("utf-8", "replace")):
            if not m.startswith("//"):
                add("jekyll_nav", m.strip("/"))
    for sm in docs_root.rglob("SUMMARY.md"):
        base = sm.parent.relative_to(docs_root)
        for m in re.findall(r"\]\(([^)#\s]+\.md)", sm.read_text("utf-8", "replace")):
            add("gitbook_summary", str(base / m))
    md_pages = [f for f in files if re.search(r"\.(md|mdx|markdown)$", f)]
    if md_pages and not autogen:
        n_nav = 0
        for f in md_pages[:400]:
            head = (docs_root / f).read_text("utf-8", "replace")[:600]
            n_nav += bool(re.search(r"^(nav_order|sidebar_position|weight|sort_rank):", head, re.M))
        if n_nav >= 0.6 * min(len(md_pages), 400):
            autogen = "front_matter_navigation"

    def resolve(ref, fuzzy):
        r_ = re.sub(r"#.*$", "", ref).strip()
        r_ = os.path.normpath(r_).lower() if r_ else ""
        if r_.startswith("../") and repo_stems:
            rr = re.sub(DOC_EXT, "", os.path.normpath(os.path.join(docs_rel, r_)).lower())
            return rr in repo_stems or rr + "/readme" in repo_stems or rr + "/index" in repo_stems
        r_ = re.sub(DOC_EXT, "", r_.lstrip("./")) if r_ not in (".", "") else ""
        if not r_:
            return True
        for cand in (r_, r_ + "/index", r_ + "/readme", r_ + "/_index", re.sub(r"/index$", "", r_)):
            if cand in stems:
                return True
        if r_ in dir_prefixes:
            return True  # folder entry (fumadocs / awesome-nav section)
        if fuzzy:
            b = r_.rsplit("/", 1)[-1]
            return b in bases or re.sub(r"^\d+[-_]", "", b) in {re.sub(r"^\d+[-_]", "", x) for x in bases}
        return False
    n_docs = sum(1 for f in files if re.search(r"\.(md|mdx|rst|ipynb|txt|markdown)$", f))
    evals = {}
    for kind, refs in kinds.items():
        refs = sorted(set(refs))
        fuzzy = kind in ("jekyll_nav", "docusaurus_sidebars")
        missing = [r_ for r_ in refs if not resolve(r_, fuzzy)]
        evals[kind] = {"entries": len(refs), "missing": len(missing), "missing_examples": missing[:10],
                       "ratio": round(1 - len(missing) / len(refs), 3) if refs else None}
    best = max(evals, key=lambda k: evals[k]["entries"]) if evals else None
    b = evals.get(best, {})
    return {"toc_kind": best or autogen, "toc_entries": b.get("entries", 0), "toc_missing": b.get("missing", 0),
            "toc_missing_examples": b.get("missing_examples", []), "toc_resolved_ratio": b.get("ratio"),
            "toc_all_kinds": evals, "navigation_from_tree": autogen, "doc_source_files": n_docs, "toc_check_version": 2}


def docs_complete(tc, min_ratio=0.95, min_files=10):
    if tc["doc_source_files"] < min_files:
        return False, f"文档源文件仅 {tc['doc_source_files']} 个"
    if tc["toc_entries"]:
        nontrivial = tc["toc_entries"] >= 10 or tc["toc_entries"] >= 0.5 * tc["doc_source_files"]
        if tc["toc_resolved_ratio"] >= min_ratio and nontrivial:
            return True, f"{tc['toc_kind']} 目录 {tc['toc_entries']} 项，解析率 {tc['toc_resolved_ratio']}"
        if tc.get("navigation_from_tree") and not nontrivial:
            return True, f"导航由目录树/前置元数据生成（{tc['navigation_from_tree']}），已保存完整源树"
        return False, f"{tc['toc_kind']} 目录 {tc['toc_entries']} 项，解析率 {tc['toc_resolved_ratio']}" + ("" if nontrivial else "（目录过小）")
    if tc.get("navigation_from_tree"):
        return True, f"导航由目录树/前置元数据生成（{tc['navigation_from_tree']}），已保存完整源树"
    return False, "未找到可解析的目录/导航文件"


def save_result(eid, rec):
    with C.locked("eng_results"):
        res = C.load_json(RESULTS_PATH, {})
        res[eid] = rec
        C.save_json(RESULTS_PATH, res)


def safe(s):
    return re.sub(r"[^A-Za-z0-9-]+", "", s) or "Project"


def process(s):
    eid = s["eid"]
    stage = C.STAGING / f"eng_{eid}_{int(time.time())}"
    rec = {"eid": eid, "name": s["name"], "repo": s["repo"], "ref_requested": s["ref"], "time": time.strftime("%F %T"),
           "retrieved": time.strftime("%F"), "notes": []}
    try:
        src = stage / "src"
        sha, cdate = fetch_repo(s["repo"], s["ref"], src)
        rec.update({"commit": sha, "commit_date": cdate})
        shutil.rmtree(src / ".git")
        kept, excluded = filter_tree(src)
        total = sum((src / k).stat().st_size for k in kept)
        rec.update({"files_kept": len(kept), "bytes_kept": total, "excluded_files": excluded[:400],
                    "excluded_count": len(excluded), "license": detect_license(src)})
        if total > MAX_TREE_BYTES:
            raise RuntimeError(f"filtered tree too large ({total} bytes)")
        name = f"{safe(s['name'])}_{sha[:7]}"
        CODE_DIR.mkdir(exist_ok=True)
        arch = CODE_DIR / f"{name}_original_en.tar.gz"
        rdir = CODE_DIR / f"{name}_en"
        for p in (arch, rdir):
            if p.exists():
                shutil.rmtree(p) if p.is_dir() else p.unlink()
        det_tar(src, arch, name)
        rows = renamed_copy(src, kept, rdir)
        rec.update({"archive_path": str(arch.relative_to(C.ROOT)), "archive_sha256": C.sha256_file(arch),
                    "renamed_copy_path": str(rdir.relative_to(C.ROOT)),
                    "renamed_copy_pack_sha256": C.hashlib.sha256(("\n".join(sorted(f"{h}  {n}" for _, n, h in rows)) + "\n").encode()).hexdigest()})
        docs = s.get("docs") or {}
        if docs:
            dsrc_root = src
            dsha = sha
            if docs.get("repo"):
                dsrc_root = stage / "docsrepo"
                dsha, ddate = fetch_repo(docs["repo"], docs["ref"], dsrc_root)
                shutil.rmtree(dsrc_root / ".git")
                filter_tree(dsrc_root)
                rec["docs_repo_commit"], rec["docs_repo_commit_date"] = dsha, ddate
                darch = CODE_DIR / f"{safe(s['name'])}-docs_{dsha[:7]}_original_en.tar.gz"
                det_tar(dsrc_root, darch, f"{safe(s['name'])}-docs_{dsha[:7]}")
                rec["docs_archive_path"], rec["docs_archive_sha256"] = str(darch.relative_to(C.ROOT)), C.sha256_file(darch)
            dpath = dsrc_root / docs.get("path", "docs")
            if not dpath.is_dir():
                raise RuntimeError(f"docs path not found: {docs.get('path')}")
            tc = toc_check(dpath, dsrc_root)
            drels = sorted(str(p.relative_to(dpath)) for p in dpath.rglob("*") if p.is_file())
            ddir = DOCS_DIR / f"{safe(s['name'])}_docs_{dsha[:7]}_en"
            if ddir.exists():
                shutil.rmtree(ddir)
            drows = renamed_copy(dpath, drels, ddir)
            complete, why = docs_complete(tc, docs.get("min_toc_resolved", 0.95), docs.get("min_files", 10))
            rec["docs"] = {**tc, "path_in_repo": docs.get("path", "docs"), "local_path": str(ddir.relative_to(C.ROOT)),
                           "files": len(drows), "format": docs.get("format", "源文件（Markdown/RST，未构建 HTML）"),
                           "scope_note": docs.get("scope_note", ""), "complete_doc_set": complete, "completeness_basis": why,
                           "pack_sha256": C.hashlib.sha256(("\n".join(sorted(f"{h}  {n}" for _, n, h in drows)) + "\n").encode()).hexdigest()}
            if not complete:
                rec["notes"].append(f"docs not counted as complete set: {why}")
        rec["status"] = "verified"
    except Exception as e:
        rec["status"] = "failed"
        rec["notes"].append(repr(e)[:500])
    finally:
        shutil.rmtree(stage, ignore_errors=True)
    save_result(eid, rec)
    d = rec.get("docs", {})
    print(f"[{eid}] {rec['status'].upper()} {s['name']} {rec.get('commit', '')[:10]} files={rec.get('files_kept')} "
          f"excl={rec.get('excluded_count')} lic={rec.get('license', {}).get('detected')} "
          f"docs={d.get('complete_doc_set')} toc={d.get('toc_kind')}:{d.get('toc_entries')}/-{d.get('toc_missing')} | {'; '.join(rec['notes'])[:300]}")


def cmd_fetch(args):
    res = C.load_json(RESULTS_PATH, {})
    for s in load_seeds():
        if args.eid and s["eid"] != args.eid:
            continue
        prev = res.get(s["eid"], {})
        if not args.eid and prev.get("status") == "verified":
            continue
        if not args.eid and prev.get("status") == "failed" and not args.retry_failed:
            continue
        if s.get("exclude"):
            continue
        process(s)
    cmd_status(args)


def cmd_status(args):
    res = C.load_json(RESULTS_PATH, {})
    seeds = load_seeds()
    ver = [s for s in seeds if res.get(s["eid"], {}).get("status") == "verified"]
    docs_ok = [s for s in ver if res[s["eid"]].get("docs", {}).get("complete_doc_set")]
    fail = [s for s in seeds if res.get(s["eid"], {}).get("status") == "failed"]
    todo = [s for s in seeds if s["eid"] not in res and not s.get("exclude")]
    print(f"[19 工程资料] 源码项目已核验 {len(ver)}；其中完整文档集 {len(docs_ok)}；待处理 {len(todo)}；失败 {len(fail)}")
    stages = {}
    for s in ver:
        stages.setdefault(s.get("stage", "?"), []).append(s["name"])
    for k, v in stages.items():
        print(f"  {k}: {', '.join(v)}")
    for s in fail:
        print(f"  FAILED {s['eid']} {s['name']} | {'; '.join(res[s['eid']].get('notes', []))[:200]}")


def cmd_recheck_docs(args):
    """Re-run the TOC check on the docs subtree extracted from the saved ORIGINAL-layout archive
    (no network). The previous check is kept under docs.previous_checks."""
    res = C.load_json(RESULTS_PATH, {})
    for s in load_seeds():
        r = res.get(s["eid"], {})
        if r.get("status") != "verified" or not r.get("docs") or (args.eid and s["eid"] != args.eid):
            continue
        docs = s.get("docs") or {}
        arch = C.ROOT / (r.get("docs_archive_path") or r["archive_path"])
        stage = C.STAGING / f"recheck_{s['eid']}_{int(time.time())}"
        stage.mkdir(parents=True)
        try:
            with tarfile.open(arch) as tf:
                prefix = tf.getmembers()[0].name.split("/", 1)[0]
                tf.extractall(stage, filter="data")
            repo = stage / prefix
            droot = repo / docs.get("path", "docs") if docs.get("path", "docs") not in (".", "") else repo
            tc = toc_check(droot, repo)
            complete, why = docs_complete(tc, docs.get("min_toc_resolved", 0.95), docs.get("min_files", 10))
            d = r["docs"]
            prev = {k: d.get(k) for k in ("toc_kind", "toc_entries", "toc_missing", "toc_resolved_ratio", "complete_doc_set")}
            d.setdefault("previous_checks", []).append(prev)
            d.update(tc)
            d["complete_doc_set"], d["completeness_basis"] = complete, why
            d["rechecked"] = time.strftime("%F %T")
            r["notes"] = [n for n in r.get("notes", []) if not n.startswith("docs not counted")]
            if not complete:
                r["notes"].append(f"docs not counted as complete set: {why}")
            save_result(s["eid"], r)
            print(f"[{s['eid']}] {s['name']}: {prev['complete_doc_set']} -> {complete} | {why} | kinds={ {k: (v['entries'], v['ratio']) for k, v in tc['toc_all_kinds'].items()} } miss={tc['toc_missing_examples'][:4]}")
        finally:
            shutil.rmtree(stage, ignore_errors=True)


def cmd_refs(args):
    out = git(["ls-remote", "--tags", "--refs", args.url], timeout=120)
    tags = [l.split("refs/tags/")[1] for l in out.splitlines() if "refs/tags/" in l]
    head = git(["ls-remote", args.url, "HEAD"], timeout=120).split()[0]
    print(f"HEAD {head}")
    print("tags (last 30 by version sort):")
    def vkey(t):
        return [int(x) if x.isdigit() else -1 for x in re.findall(r"\d+|[A-Za-z]+", t)]
    for t in sorted(tags, key=vkey)[-30:]:
        print("  " + t)


def main():
    sys.stdout.reconfigure(line_buffering=True)
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("--eid"); p.add_argument("--retry-failed", action="store_true"); p.set_defaults(f=cmd_fetch)
    p = sub.add_parser("status"); p.set_defaults(f=cmd_status)
    p = sub.add_parser("recheck-docs"); p.add_argument("--eid"); p.set_defaults(f=cmd_recheck_docs)
    p = sub.add_parser("refs"); p.add_argument("url"); p.set_defaults(f=cmd_refs)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
