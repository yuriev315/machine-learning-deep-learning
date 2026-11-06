#!/usr/bin/env python3
"""Download and verify books (C12) and university course materials (C11).

Manifests: scripts/seeds/C11_courses_cn.json and scripts/seeds/C12_books_cn.json, each a list of
entries with a fixed "id" (MLU### courses, MLB### books) and at least:
  title, format ("pdf" | "pdf_multi" | "html"), files [{"url", "label"}], title_phrase,
  min_pages (pdf: whole file; pdf_multi: sum over parts), source_page.
A "pdf_multi" or "html" entry is ONE package: every listed part must download and verify, and the
part list must equal the official table of contents (recorded by hand in "toc_check").

Verification:
  pdf/pdf_multi : HTTP 200, %PDF- header, pypdf parses every part, page count >= min_pages,
                  title_phrase found in the text of the first 8 pages of the first part
  html          : HTTP 200 for every listed page, text/html, >= 2 KB of visible text per page,
                  title_phrase found in the first page; pages saved with their images/CSS for
                  offline reading (wget --page-requisites --convert-links, no recursion)
Files land in books/ or university_materials/ under "<file_stem>_<lang>.pdf" or a directory
"<file_stem>_<lang>/" for packages. Results: scripts/cache/materials_results_en.json.

Usage: python3 -I scripts/fetch_materials_en.py <pypdf_lib_dir> <staging_dir> [ID ...]
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CACHE, ROOT, SCRIPTS, UA, host_key, http, load, save, wait  # noqa: E402


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def pdf_check(path, phrase=None, text_pages=8):
    import pypdf
    with open(path, "rb") as f:
        if not f.read(1024).lstrip().startswith(b"%PDF-"):
            return {"ok": False, "error": "not a PDF"}
    try:
        r = pypdf.PdfReader(str(path))
        n = len(r.pages)
        out = {"ok": True, "pages": n}
        if phrase:
            text = "\n".join((r.pages[i].extract_text() or "") for i in range(min(text_pages, n)))
            blob = re.sub(r"\s+", " ", text).lower()
            out["phrase_found"] = re.sub(r"\s+", " ", phrase).lower() in blob or \
                re.sub(r"[^a-z0-9]", "", phrase.lower()) in re.sub(r"[^a-z0-9]", "", blob)
            out["text_head"] = " ".join(text.split())[:240]
        try:
            out["outline_top"] = len(r.outline)
        except Exception:
            out["outline_top"] = None
        return out
    except Exception as e:
        return {"ok": False, "error": "pypdf: " + repr(e)[:200]}


def fetch_to(url, dest):
    st, body, final, ctype = http(url, accept="*/*", timeout=300, tries=3)
    if st == 200:
        dest.write_bytes(body)
    return {"url": url, "http_status": st, "final_url": final, "content_type": ctype,
            "bytes": len(body) if st == 200 else 0}


def visible_text_len(html):
    html = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", html)
    return len(" ".join(re.sub(r"<[^>]+>", " ", html).split()))


def arxiv_latest(aid):
    import xml.etree.ElementTree as ET
    ns = {"a": "http://www.w3.org/2005/Atom"}
    st, body, _, _ = http("https://export.arxiv.org/api/query?id_list=" + aid, accept="application/atom+xml")
    if st != 200:
        return None
    ent = ET.fromstring(body).find("a:entry", ns)
    if ent is None:
        return None
    return {"latest_version": ent.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1],
            "title": " ".join(ent.findtext("a:title", "", ns).split()),
            "published": ent.findtext("a:published", "", ns)[:10], "updated": ent.findtext("a:updated", "", ns)[:10]}


def isbns(path, pages=12):
    import pypdf
    r = pypdf.PdfReader(str(path))
    text = "\n".join((r.pages[i].extract_text() or "") for i in range(min(pages, len(r.pages))))
    found = re.findall(r"ISBN(?:-1[03])?[:\s]*((?:97[89][-\s]?)?\d{1,5}[-\s]?\d+[-\s]?\d+[-\s]?[\dX])", text)
    return sorted({re.sub(r"\s", "-", x) for x in found})


def do_pdf(e, stage, outdir):
    parts, total = [], 0
    if e.get("arxiv") and not e.get("files"):
        ax = arxiv_latest(e["arxiv"])
        if not ax:
            return {"status": "failed", "reason": "arXiv API lookup failed"}
        e["files"] = [{"url": "https://arxiv.org/pdf/" + ax["latest_version"], "label": "arXiv " + ax["latest_version"]}]
        arxiv_info = ax
    else:
        arxiv_info = None
    for i, f in enumerate(e["files"]):
        dest = stage / f"part{i:03d}.pdf"
        print(e["id"], "GET", f["url"], file=sys.stderr, flush=True)
        t = fetch_to(f["url"], dest)
        t["label"] = f.get("label", "")
        if t["http_status"] != 200:
            return {"status": "failed", "reason": f"{f['url']}: HTTP {t['http_status']}", "parts": parts + [t]}
        t.update(pdf_check(dest, e.get("title_phrase") if i == 0 else None))
        if not t["ok"]:
            return {"status": "failed", "reason": f"{f['url']}: {t.get('error')}", "parts": parts + [t]}
        if i == 0 and e.get("title_phrase") and not t.get("phrase_found"):
            return {"status": "failed", "reason": f"title phrase not found on first pages: {t.get('text_head')}",
                    "parts": parts + [t]}
        total += t["pages"]
        t["sha256"] = sha256(dest)
        parts.append(t)
    if total < e.get("min_pages", 1):
        return {"status": "failed", "reason": f"only {total} pages < min_pages {e['min_pages']}", "parts": parts}
    stem = e["file_stem"]
    if e["format"] == "pdf":
        target = outdir / f"{stem}.pdf"
        if target.exists() and sha256(target) != parts[0]["sha256"]:
            return {"status": "failed", "reason": f"refusing to overwrite {target.name}", "parts": parts}
        shutil.move(str(stage / "part000.pdf"), target)
        rel = target.relative_to(ROOT)
        files = [{"path": str(rel), "sha256": parts[0]["sha256"], "pages": parts[0]["pages"]}]
    else:
        tdir = outdir / stem
        tdir.mkdir(exist_ok=True)
        files = []
        for i, (f, t) in enumerate(zip(e["files"], parts)):
            name = f"{i + 1:02d}_{re.sub(r'[^A-Za-z0-9]+', '_', f.get('label') or 'part').strip('_')[:50]}_{e.get('lang', 'en')}.pdf"
            shutil.move(str(stage / f"part{i:03d}.pdf"), tdir / name)
            files.append({"path": str((tdir / name).relative_to(ROOT)), "sha256": t["sha256"], "pages": t["pages"],
                          "label": f.get("label", "")})
        rel = tdir.relative_to(ROOT)
    try:
        found = isbns(ROOT / files[0]["path"])
    except Exception:
        found = []
    return {"status": "ok", "local_path": str(rel), "files": files, "total_pages": total, "parts": parts,
            "isbn_in_pdf": found, "arxiv_info": arxiv_info}


def do_html(e, stage, outdir):
    tdir = outdir / e["file_stem"]
    work = stage / "site"
    work.mkdir()
    parts = []
    for i, f in enumerate(e["files"]):
        print(e["id"], "GET", f["url"], file=sys.stderr, flush=True)
        st, body, final, ctype = http(f["url"], accept="text/html", timeout=120)
        t = {"url": f["url"], "http_status": st, "content_type": ctype, "label": f.get("label", "")}
        if st != 200 or "html" not in ctype.lower():
            t["error"] = f"HTTP {st} {ctype}"
            return {"status": "failed", "reason": f"{f['url']}: {t['error']}", "parts": parts + [t]}
        html = body.decode("utf-8", "replace")
        t["visible_chars"] = visible_text_len(html)
        if t["visible_chars"] < e.get("min_chars_per_page", 2000):
            return {"status": "failed", "reason": f"{f['url']}: only {t['visible_chars']} visible chars",
                    "parts": parts + [t]}
        if i == 0 and e.get("title_phrase") and e["title_phrase"].lower() not in re.sub(r"\s+", " ", html).lower():
            return {"status": "failed", "reason": "title phrase not in first page", "parts": parts + [t]}
        parts.append(t)
    # offline copy with page requisites (images, CSS); one host, no recursion beyond the listed pages
    urls = stage / "urls.txt"
    urls.write_text("\n".join(f["url"] for f in e["files"]) + "\n")
    wait(host_key(e["files"][0]["url"]), 2.0)
    cmd = ["wget", "-q", "--page-requisites", "--convert-links", "--adjust-extension", "--no-parent",
           "--wait=1", "--random-wait", "--tries=3", "--timeout=60", "-e", "robots=on", "-U", UA,
           "-P", str(work), "-i", str(urls)]
    if e.get("span_hosts"):
        cmd.insert(1, "--span-hosts")
    rc = subprocess.run(cmd, timeout=3600).returncode
    if rc not in (0, 8):  # 8 = some requisite (e.g. an image) returned an error; pages verified above
        return {"status": "failed", "reason": f"wget exit {rc}", "parts": parts}
    if tdir.exists():
        shutil.rmtree(tdir)
    shutil.move(str(work), tdir)
    files = []
    for p in sorted(tdir.rglob("*")):
        if p.is_file():
            files.append({"path": str(p.relative_to(ROOT)), "sha256": sha256(p), "bytes": p.stat().st_size})
    n_html = sum(1 for f in files if f["path"].endswith((".html", ".htm")))
    return {"status": "ok", "local_path": str(tdir.relative_to(ROOT)), "files": files, "html_pages": n_html,
            "requisites_warning": rc == 8, "parts": parts}


def main():
    sys.path.insert(0, sys.argv[1])
    staging = Path(sys.argv[2])
    only = set(sys.argv[3:])
    staging.mkdir(parents=True, exist_ok=True)
    res_path = CACHE / "materials_results_en.json"
    results = load(res_path, {})
    for mf, outdir in (("C11_courses_cn.json", ROOT / "university_materials"), ("C12_books_cn.json", ROOT / "books")):
        for e in load(SCRIPTS / "seeds" / mf, []):
            if only and e["id"] not in only:
                continue
            old = results.get(e["id"], {})
            if not only and old.get("status") == "ok" and (ROOT / old["local_path"]).exists():
                continue
            stage = Path(tempfile.mkdtemp(prefix=e["id"] + "_", dir=staging))
            try:
                rec = do_html(e, stage, outdir) if e["format"] == "html" else do_pdf(e, stage, outdir)
            except Exception as ex:  # keep going with the other entries
                rec = {"status": "failed", "reason": repr(ex)[:300]}
            shutil.rmtree(stage, ignore_errors=True)
            rec["manifest"] = mf
            results[e["id"]] = rec
            save(res_path, results)
            print(e["id"], rec["status"], rec.get("reason", rec.get("local_path")), flush=True)
    print("done:", sum(r["status"] == "ok" for r in results.values()), "ok of", len(results))


if __name__ == "__main__":
    main()
