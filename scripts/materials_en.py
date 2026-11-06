#!/usr/bin/env python3
"""Course lecture packs (category 17) and books (category 18): download -> verify -> record.

Adapted (copied, then edited) from /root/large_model_multimodal_literature/scripts/materials_en.py.
Seeds:   scripts/seeds/17_university_courses_seed*_cn.json, scripts/seeds/18_books_seed*_cn.json
Results: scripts/state/results/17_university_courses_en.json, .../18_books_en.json

A file entry may carry "copy_from": an absolute path of the same file already verified in a sibling
library (/root/<name>_literature/...). It is then copied (not downloaded), re-checked like a download,
and the item is recorded with origin "reused_other_library".

Each seed lists the files of ONE material (a whole book, or a whole course's lecture pack):
  "files": [{"url": ..., "name": "<local name with language suffix>", "kind": "pdf|html|zip|text",
             "label": "Lecture 3 ...", "main": true}]
  "mirror": {"start": [urls], "accept_prefix": "https://host/path/", "name": "<dir>_en"}  (complete HTML books)
A material is VERIFIED only if every listed file downloads (HTTP 200) and passes its type check
(PDF parses; zip passes testzip; HTML is a real page), the item checks pass (book: main PDF has
>= min_pages pages, title found in the first pages, a contents heading is present; course: number
of verified lecture files == expected_items), and the item is recorded with per-file SHA256 and a
pack SHA256 (sha256 of the sorted "sha256  relative_path" lines).

Usage:
  python3 -I scripts/materials_en.py fetch  13|14 [--sid 13-004] [--retry-failed]
  python3 -I scripts/materials_en.py status 13|14
  python3 -I scripts/materials_en.py links  <page_url> [--pattern '\\.pdf$']   # list links on an official page
"""
import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402

DEST_DIR = {"17": C.ROOT / "university_materials", "18": C.ROOT / "books"}
CLAIMS_PATH = C.STATE / "claims_en.json"


def seeds_path(code):
    return C.SEEDS / f"{C.cat_key(code)}_seed_cn.json"


def load_seeds(code):
    """All seed files of the category: <key>_seed_cn.json and <key>_seed_<part>_cn.json."""
    out = []
    for p in sorted(C.SEEDS.glob(f"{C.cat_key(code)}_seed*_cn.json")):
        for s in C.load_json(p, []):
            s["_seed_file"] = p.name
            out.append(s)
    sids = [s["sid"] for s in out]
    dup = {x for x in sids if sids.count(x) > 1}
    if dup:
        sys.exit(f"duplicate sid across seed files: {sorted(dup)}")
    return out


def save_result(code, sid, rec):
    with C.locked(f"mat_results_{code}"):
        results = C.load_json(results_path(code), {})
        results[sid] = rec
        C.save_json(results_path(code), results)


def results_path(code):
    return C.RESULTS / f"{C.cat_key(code)}_en.json"


SUFFIX_RE = re.compile(r"_(en|cn|cn_en|de|fr|ja|ko|zh)\.[A-Za-z0-9]+$")


def check_pdf(path, need_text=True):
    pypdf = C.load_pypdf()
    with open(path, "rb") as f:
        if b"%PDF-" not in f.read(1024):
            return {"ok": False, "note": "no %PDF- header"}
    try:
        rd = pypdf.PdfReader(str(path), strict=False)
        if rd.is_encrypted:
            try:
                rd.decrypt("")
            except Exception:
                pass
        n = len(rd.pages)
        sample = [0, 1, 2, n // 2, n - 1] if n > 3 else list(range(n))
        txt = ""
        for i in sorted(set(i for i in sample if 0 <= i < n)):
            try:
                txt += rd.pages[i].extract_text() or ""
            except Exception:
                pass
    except Exception as e:
        return {"ok": False, "note": f"pypdf: {e!r}"[:160]}
    return {"ok": n >= 1, "pages": n, "sample_chars": len(txt)}


def pdf_front_text(path, pages=12):
    pypdf = C.load_pypdf()
    rd = pypdf.PdfReader(str(path), strict=False)
    out = []
    for i in range(min(pages, len(rd.pages))):
        try:
            out.append(rd.pages[i].extract_text() or "")
        except Exception:
            out.append("")
    return "\n".join(out)


def check_file(path, kind):
    if kind == "pdf":
        return check_pdf(path)
    if kind == "zip":
        try:
            with zipfile.ZipFile(path) as z:
                bad = z.testzip()
                names = z.namelist()
            return {"ok": bad is None, "entries": len(names), "note": f"bad member {bad}" if bad else ""}
        except Exception as e:
            return {"ok": False, "note": f"zip: {e!r}"[:160]}
    if kind == "html":
        t = Path(path).read_bytes()[:2_000_000].decode("utf-8", "replace")
        text = re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<(script|style).*?</\1>", " ", t))
        n = len(re.sub(r"\s+", " ", text))
        return {"ok": "<html" in t.lower() and n > 500, "text_chars": n}
    # text-like (py, md, ipynb, txt)
    b = Path(path).read_bytes()
    return {"ok": len(b) > 100 and b"\x00" not in b[:4096], "bytes": len(b)}


def pack_hash(files):
    lines = sorted(f"{f['sha256']}  {f['path']}" for f in files)
    import hashlib
    return hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def run_mirror(spec, outdir):
    """Offline copy of a complete HTML book with wget (page requisites + link conversion)."""
    outdir.mkdir(parents=True, exist_ok=True)
    host = urllib.parse.urlparse(spec["start"][0]).netloc
    cmd = ["wget", "--quiet", "--page-requisites", "--convert-links", "--adjust-extension",
           "--no-host-directories", "--execute", "robots=on", "--wait=2", "--random-wait",
           "--tries=2", "--timeout=60", "--user-agent", C.UA, "--directory-prefix", str(outdir)]
    if spec.get("recursive"):
        cmd += ["--recursive", "--level", str(spec.get("level", 2)), "--no-parent",
                "--domains", host, "--reject-regex", spec.get("reject_regex", r"\?|#")]
    if spec.get("cut_dirs"):
        cmd += ["--cut-dirs", str(spec["cut_dirs"])]
    cmd += spec["start"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=spec.get("timeout", 3600))
    return p.returncode


def verify_mirror(spec, outdir):
    pages = sorted(outdir.rglob("*.html"))
    missing = []
    for must in spec.get("must_contain", []):  # [relative html path, text that must appear]
        rel, needle = must
        p = outdir / rel
        if not p.exists() or needle.lower() not in p.read_text("utf-8", "replace").lower():
            missing.append(f"{rel}: '{needle}'")
    remote_refs = 0
    for p in pages:
        t = p.read_text("utf-8", "replace")
        host = urllib.parse.urlparse(spec["start"][0]).netloc
        remote_refs += len(re.findall(rf'(?:src)="https?://{re.escape(host)}', t))
    return {"html_pages": len(pages), "missing": missing, "remote_src_refs_same_host": remote_refs,
            "ok": len(pages) >= spec.get("min_pages", 1) and not missing}


def cmd_fetch(args):
    code = args.code
    seeds = load_seeds(code)
    results = C.load_json(results_path(code), {})
    for s in seeds:
        sid = s["sid"]
        if args.sid and sid != args.sid:
            continue
        if s.get("exclude"):
            continue
        prev = results.get(sid, {})
        if prev.get("status") == "verified" and not args.sid:
            continue
        if prev.get("status") == "failed" and not (args.retry_failed or args.sid):
            continue
        dname = s["dir_name"]
        assert re.search(r"_(en|cn|cn_en|ja|de|fr)$", dname) or SUFFIX_RE.search(dname), f"{sid}: dir/file name lacks language suffix"
        stage = C.STAGING / f"{C.cat_key(code)}_{sid}_{int(time.time())}"
        stage.mkdir(parents=True)
        rec = {"sid": sid, "time": time.strftime("%F %T"), "files": [], "notes": []}
        if s.get("arxiv"):
            key = "arxiv:" + s["arxiv"]
            with C.locked("claims"):
                claims = C.load_json(CLAIMS_PATH, {})
                cl = claims.get(key)
                if cl and (cl["cat"], cl["sid"]) != (code, sid):
                    rec.update({"status": "duplicate_elsewhere", "claimed_by": cl})
                    save_result(code, sid, rec)
                    print(f"[{sid}] duplicate of {cl}")
                    shutil.rmtree(stage, ignore_errors=True)
                    continue
                claims[key] = {"cat": code, "sid": sid, "state": "downloading"}
                C.save_json(CLAIMS_PATH, claims)
            rec["key"] = key
        ok = True
        single = len(s.get("files", [])) == 1 and not s.get("mirror") and code == "18"
        for f in s.get("files", []):
            name = f["name"]
            assert SUFFIX_RE.search(name), f"{sid}: {name} lacks language suffix"
            dest = stage / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                if f.get("copy_from"):
                    src = Path(f["copy_from"])
                    if not re.match(r"^/root/[a-z_]+_literature/", str(src)) or "low_resource_language_llm_literature" in str(src) or not src.is_file():
                        raise C.HttpError(0, f"copy_from not a sibling-library file: {src}")
                    shutil.copyfile(src, dest)
                    st, final, ctype, nbytes = 200, f["url"], "copied", dest.stat().st_size
                    rec["origin"] = "reused_other_library"
                    rec.setdefault("origin_paths", []).append(str(src))
                else:
                    st, final, ctype, nbytes = C.http_get(f["url"], dest=dest, max_bytes=400 * 1024 * 1024, timeout=300)
            except C.HttpError as e:
                rec["files"].append({"path": name, "url": f["url"], "ok": False, "note": str(e)})
                rec["notes"].append(f"{name}: {e}")
                ok = False
                continue
            chk = check_file(dest, f.get("kind", "pdf"))
            entry = {"path": name, "url": f["url"], "final_url": final, "http_status": st, "content_type": ctype,
                     "bytes": nbytes, "label": f.get("label", ""), "check": chk, "ok": chk["ok"], "aux": bool(f.get("aux")),
                     "sha256": C.sha256_file(dest)}
            rec["files"].append(entry)
            if not chk["ok"]:
                ok = False
                rec["notes"].append(f"{name}: type check failed {chk}")
            print(f"[{sid}] {'ok ' if chk['ok'] else 'BAD'} {name} {chk}")
        if s.get("mirror"):
            mdir = stage / s["mirror"]["name"]
            rc = run_mirror(s["mirror"], mdir)
            mv = verify_mirror(s["mirror"], mdir)
            rec["mirror"] = {"wget_rc": rc, **mv}
            if not mv["ok"]:
                ok = False
                rec["notes"].append(f"mirror check failed: {mv}")
            for p in sorted(mdir.rglob("*")):
                if p.is_file():
                    rec["files"].append({"path": str(p.relative_to(stage)), "ok": True, "sha256": C.sha256_file(p),
                                         "bytes": p.stat().st_size, "mirror": True})
            print(f"[{sid}] mirror rc={rc} {mv}")
        # item-level checks
        if ok and code == "18":
            mains = [f for f in s.get("files", []) if f.get("main")] or s.get("files", [])[:1]
            for mf in mains:
                if mf.get("kind", "pdf") != "pdf":
                    continue
                p = stage / mf["name"]
                chk = check_pdf(p)
                front = pdf_front_text(p, 25)
                if re.search(r"[\u4e00-\u9fff]", s["title"]):
                    compact = lambda x: re.sub(r"[\s\W_]+", "", x)
                    tm = 1.0 if compact(s["title"]) in compact(front) else 0.0
                else:
                    tm = C.title_in_text(s["title"], front[:20000])
                has_toc = bool(re.search(r"(?i)table\s*of\s*contents|\bcontents\b|目\s*录", front))
                au = s.get("authors", [""])[0]
                au_ok = (not au) or C.fold(C.surname(au)).lower() in C.fold(front).lower() or au in front
                rec["book_check"] = {"pages": chk.get("pages"), "title_match": round(tm, 2), "toc_found": has_toc,
                                     "author_found": au_ok, "min_pages": s.get("min_pages", 100)}
                if (chk.get("pages") or 0) < s.get("min_pages", 100):
                    ok = False
                    rec["notes"].append(f"main PDF only {chk.get('pages')} pages")
                if tm < 0.8 and not s.get("title_check_override"):
                    ok = False
                    rec["notes"].append(f"title match {tm:.2f}")
                if not has_toc and not s.get("toc_override"):
                    ok = False
                    rec["notes"].append("no contents heading in first 25 pages")
                if not au_ok and not s.get("author_check_override"):
                    ok = False
                    rec["notes"].append("first author not found in front matter")
        if ok and code == "17":
            n_lect = sum(1 for f in rec["files"] if f.get("ok") and not f.get("mirror") and not f.get("aux"))
            exp = s.get("expected_items")
            rec["course_check"] = {"lecture_files_ok": n_lect, "expected_items": exp}
            if exp is None or n_lect < exp:
                ok = False
                rec["notes"].append(f"lecture files {n_lect} < expected {exp}")
        # move into place
        if ok:
            ddir = DEST_DIR[code]
            if single:
                name = s["files"][0]["name"]
                dest = ddir / name
                if dest.exists() and C.sha256_file(dest) != rec["files"][0]["sha256"]:
                    sys.exit(f"{sid}: refusing to overwrite {dest} with different content")
                shutil.move(str(stage / name), dest)
                rec["local_path"] = str(dest.relative_to(C.ROOT))
                for e in rec["files"]:
                    e["path"] = str(dest.relative_to(C.ROOT))
            else:
                dest = ddir / dname
                if dest.exists():
                    shutil.rmtree(dest)
                dest.mkdir(parents=True)
                for p in sorted(stage.iterdir()):
                    shutil.move(str(p), dest / p.name)
                for e in rec["files"]:
                    e["path"] = str((dest / e["path"]).relative_to(C.ROOT))
                manifest = {"sid": sid, "title": s.get("title") or s.get("course_title"),
                            "source": s.get("official_url") or s.get("landing_url"),
                            "retrieved": time.strftime("%F"),
                            "files": [{k: e.get(k) for k in ("path", "url", "label", "sha256", "bytes")} for e in rec["files"]]}
                C.save_json(dest / "manifest_en.json", manifest)
                rec["local_path"] = str(dest.relative_to(C.ROOT))
            rec["pack_sha256"] = pack_hash(rec["files"]) if len(rec["files"]) > 1 else rec["files"][0]["sha256"]
            rec["status"] = "verified"
            rec.setdefault("origin", "downloaded_this_round")
        else:
            rec["status"] = "failed"
        save_result(code, sid, rec)
        if rec.get("key"):
            with C.locked("claims"):
                claims = C.load_json(CLAIMS_PATH, {})
                if rec["status"] == "verified":
                    claims[rec["key"]] = {"cat": code, "sid": sid, "state": "verified", "file": rec.get("local_path")}
                elif claims.get(rec["key"], {}).get("sid") == sid:
                    del claims[rec["key"]]
                C.save_json(CLAIMS_PATH, claims)
        shutil.rmtree(stage, ignore_errors=True)
        print(f"[{sid}] {rec['status'].upper()} {s.get('title') or s.get('course_title')} | {'; '.join(rec['notes'])[:300]}")
    cmd_status(args)


def cmd_status(args):
    code = args.code
    seeds = load_seeds(code)
    results = C.load_json(results_path(code), {})
    by = {}
    for s in seeds:
        st = "excluded" if s.get("exclude") else results.get(s["sid"], {}).get("status", "todo")
        by.setdefault(st, []).append(s)
    ver = by.get("verified", [])
    recent = [s for s in ver if str(s.get("edition_year") or s.get("term_year") or "0") >= "2023"]
    print(f"[{code} {C.CAT_BY_CODE[code][2]}] 已核验完整资料 {len(ver)} / 目标约 50；待核验 {len(by.get('todo', []))}；"
          f"下载失败 {len(by.get('failed', []))}。 近三年版本/学期 {len(recent)}/{len(ver)}")
    for s in by.get("failed", []):
        print(f"  FAILED {s['sid']} {s.get('title') or s.get('course_title')} | {'; '.join(results[s['sid']].get('notes', []))[:200]}")
    for s in by.get("todo", []):
        print(f"  TODO {s['sid']} {s.get('title') or s.get('course_title')}")


def cmd_links(args):
    page = C.http_get(args.url, timeout=60).decode("utf-8", "replace")
    seen = []
    for href, label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', page, re.S | re.I):
        u = urllib.parse.urljoin(args.url, html.unescape(href))
        if args.pattern and not re.search(args.pattern, u, re.I):
            continue
        if u in seen:
            continue
        seen.append(u)
        print(f"{u}\t{re.sub(r'\\s+', ' ', re.sub(r'<[^>]+>', '', html.unescape(label))).strip()[:80]}")
    print(f"# {len(seen)} links", file=sys.stderr)


def main():
    sys.stdout.reconfigure(line_buffering=True)
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("code"); p.add_argument("--sid"); p.add_argument("--retry-failed", action="store_true"); p.set_defaults(f=cmd_fetch)
    p = sub.add_parser("status"); p.add_argument("code"); p.set_defaults(f=cmd_status)
    p = sub.add_parser("links"); p.add_argument("url"); p.add_argument("--pattern", default=""); p.set_defaults(f=cmd_links)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
