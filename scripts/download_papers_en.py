#!/usr/bin/env python3
"""Download and verify the full-text PDF of every resolved paper (C01-C10).

For each record in cache/papers_resolved_en.json:
  1. URL: the exact latest arXiv version (https://arxiv.org/pdf/<id>vN); for DOI-only
     records, vetted open URLs listed in seeds/paper_pdf_overrides_cn.json;
  2. download into a fresh empty staging directory (outside papers/);
  3. verify: HTTP 200, %PDF- header, pypdf parses, >= 4 pages (rules out abstract-only
     files), title tokens found on the first two pages (>= 0.8);
  4. SHA256; refuse duplicates by hash;
  5. move to papers/<year>_<FirstAuthorSurname>_<ShortTitle>_en.pdf.
Paywalled / login pages are never attempted. arXiv is rate limited to >= 4 s per request.

Results: cache/download_papers_en.json (re-runs skip verified files whose hash still matches).

Usage: python3 -I scripts/download_papers_en.py <pypdf_lib_dir> <staging_dir> [ID ...]
"""
import hashlib
import shutil
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import (CACHE, ROOT, SCRIPTS, http, load, save, short_title,  # noqa: E402
                       surname, title_in_text)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def inspect_pdf(path, title, pages_for_title=2):
    import pypdf
    info = {}
    with open(path, "rb") as f:
        info["magic_ok"] = f.read(1024).lstrip().startswith(b"%PDF-")
    if not info["magic_ok"]:
        info["error"] = "not a PDF"
        return info
    try:
        r = pypdf.PdfReader(str(path))
        info["pages"] = len(r.pages)
        text = "\n".join((r.pages[i].extract_text() or "") for i in range(min(pages_for_title, len(r.pages))))
        info["title_match"] = round(title_in_text(title, text), 3)
        letters = [c for c in text if c.isalpha()]
        info["ascii_letter_ratio"] = round(sum(c.isascii() for c in letters) / max(1, len(letters)), 3)
        info["first_text_head"] = " ".join(text.split())[:200]
        info["parse_ok"] = True
    except Exception as e:  # pypdf failure
        info["parse_ok"] = False
        info["error"] = "pypdf: " + repr(e)[:200]
    return info


def main():
    sys.path.insert(0, sys.argv[1])
    staging = Path(sys.argv[2])
    only = set(sys.argv[3:])
    staging.mkdir(parents=True, exist_ok=True)
    recs = load(CACHE / "papers_resolved_en.json", {})
    overrides = load(SCRIPTS / "seeds/paper_pdf_overrides_cn.json", {})
    res_path = CACHE / "download_papers_en.json"
    results = load(res_path, {})
    seen = {r["sha256"]: k for k, r in results.items() if r.get("status") == "ok"}
    (ROOT / "papers").mkdir(exist_ok=True)

    for pid, p in sorted(recs.items()):
        if only and pid not in only:
            continue
        old = results.get(pid, {})
        if old.get("status") == "ok" and (ROOT / old["local_path"]).exists():
            continue
        if old.get("status") == "failed" and not only and old.get("permanent"):
            continue
        urls = []
        if p.get("latest_version"):
            urls.append((f"arXiv {p['latest_version']}", "https://arxiv.org/pdf/" + p["latest_version"]))
        for u in overrides.get(p["key"], {}).get("pdf_urls", []):
            urls.append((overrides[p["key"]].get("version_label", "override"), u))
        rec = {"tries": []}
        year = (p.get("first_public") or "0000")[:4]
        fname = f"{year}_{surname((p.get('authors') or ['Anon'])[0])}_{short_title(p['title'])}_en.pdf"
        for label, url in urls:
            stage = Path(tempfile.mkdtemp(prefix=pid + "_", dir=staging))
            dest = stage / "download.bin"
            print(pid, "GET", url, file=sys.stderr, flush=True)
            st, body, final, ctype = http(url, accept="application/pdf", timeout=180)
            t = {"label": label, "url": url, "http_status": st, "final_url": final, "content_type": ctype}
            if st == 200:
                dest.write_bytes(body)
                t.update(inspect_pdf(dest, p["title"]))
                ok = t.get("parse_ok") and t.get("pages", 0) >= 4 and t.get("title_match", 0) >= 0.8
                if ok:
                    h = sha256(dest)
                    target = ROOT / "papers" / fname
                    if h in seen and seen[h] != pid:
                        t["error"] = f"duplicate of {seen[h]}"
                    elif target.exists() and sha256(target) != h:
                        t["error"] = f"name collision {fname}"
                    else:
                        shutil.move(str(dest), target)
                        seen[h] = pid
                        rec.update(status="ok", local_path=f"papers/{fname}", sha256=h,
                                   size=target.stat().st_size, pdf_url=url, version_label=label,
                                   pages=t["pages"], title_match=t["title_match"],
                                   ascii_letter_ratio=t.get("ascii_letter_ratio"))
                elif t.get("parse_ok"):
                    t["error"] = f"check failed: pages={t.get('pages')} title_match={t.get('title_match')}"
            else:
                t["error"] = body[:200].decode("utf-8", "replace") if st is None else f"HTTP {st}"
            rec["tries"].append(t)
            shutil.rmtree(stage, ignore_errors=True)
            if rec.get("status") == "ok":
                break
        if rec.get("status") != "ok":
            rec["status"] = "failed"
            rec["reason"] = "; ".join(f"{t['label']}: {t.get('error')}" for t in rec["tries"]) or "no legal open PDF URL"
            rec["permanent"] = not urls
        results[pid] = rec
        save(res_path, results)
    n = sum(r.get("status") == "ok" for r in results.values())
    print(f"done: {n} ok / {len(results)} attempted")


if __name__ == "__main__":
    main()
