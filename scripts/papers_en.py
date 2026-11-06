#!/usr/bin/env python3
"""Paper pipeline: resolve metadata -> download -> verify -> record (resume-safe).

Adapted (copied, then edited) from /root/large_model_multimodal_literature/scripts/papers_en.py.
Papers already verified in a sibling library on this host are copied and re-verified here
(origin "reused_other_library"), never reported as new downloads.

Seeds:   scripts/seeds/<NN_slug>_seed_cn.json   (list of candidate dicts, see README_cn.md)
Results: scripts/state/results/<NN_slug>_en.json (per-seed download/verification record)
Meta:    scripts/state/arxiv_meta_en.json        (arXiv API metadata cache, shared)
Claims:  scripts/state/claims_en.json            (one primary category per paper)

Usage (from anywhere):
  python3 -I scripts/papers_en.py resolve  <NN>            # arXiv API metadata, title check
  python3 -I scripts/papers_en.py download <NN> [--target 50] [--retry-failed] [--all]
  python3 -I scripts/papers_en.py status   <NN>
  python3 -I scripts/papers_en.py brief    <NN>            # abstracts for annotation -> scripts/work/
  python3 -I scripts/papers_en.py search   '<arXiv query>' [--max 40] [--sort relevance|submittedDate]
  python3 -I scripts/papers_en.py manual   <NN> <sid> --note '<what was checked by hand>'
  python3 -I scripts/papers_en.py venue    <NN>            # OpenAlex publication-venue lookup

A download is VERIFIED only if: HTTP 200, %PDF- header, pypdf parses, >=4 pages,
>=12000 extractable characters, a references/bibliography heading exists, the file is not a
supplement, >=80% of significant title tokens appear on the first 2 pages, and the first
author's surname (or team name) appears in the text. Right-paper PDFs failing only a soft check
go to status "pending" (not counted) until checked by hand with `manual`.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lrl_common_en as C  # noqa: E402

ATOM = "{http://www.w3.org/2005/Atom}"
ARXNS = "{http://arxiv.org/schemas/atom}"
META_PATH = C.STATE / "arxiv_meta_en.json"
CLAIMS_PATH = C.STATE / "claims_en.json"
OPENALEX_PATH = C.STATE / "openalex_venue_en.json"
OTHER_LIBS = [Path("/root/large_model_multimodal_literature"), Path("/root/machine_learning_deep_learning_literature"),
              Path("/root/time_series_literature"), Path("/root/industrial_process_monitoring_literature")]


def seeds_path(code):
    return C.SEEDS / f"{C.cat_key(code)}_seed_cn.json"


def results_path(code):
    return C.RESULTS / f"{C.cat_key(code)}_en.json"


def load_seeds(code):
    seeds = C.load_json(seeds_path(code), [])
    sids = [s["sid"] for s in seeds]
    dup = {x for x in sids if sids.count(x) > 1}
    if dup:
        sys.exit(f"duplicate sid in seeds: {sorted(dup)}")
    return seeds


def norm_arxiv(a):
    a = (a or "").strip()
    a = re.sub(r"^(https?://arxiv\.org/(abs|pdf)/|arxiv:)", "", a, flags=re.I)
    a = re.sub(r"\.pdf$", "", a)
    return re.sub(r"v\d+$", "", a)


# ---------------------------------------------------------------- arXiv API
def parse_feed(xml_bytes):
    root = ET.fromstring(xml_bytes)
    out = []
    for e in root.findall(f"{ATOM}entry"):
        idurl = (e.findtext(f"{ATOM}id") or "").strip()
        if "/abs/" not in idurl:
            continue
        full = idurl.split("/abs/")[1]
        m = re.match(r"(.+?)(v(\d+))?$", full)
        base, ver = m.group(1), int(m.group(3) or 1)
        title = re.sub(r"\s+", " ", e.findtext(f"{ATOM}title") or "").strip()
        out.append({
            "arxiv": base,
            "latest_version": ver,
            "title": title,
            "authors": [re.sub(r"\s+", " ", a.findtext(f"{ATOM}name") or "").strip()
                        for a in e.findall(f"{ATOM}author")],
            "published": (e.findtext(f"{ATOM}published") or "")[:10],
            "updated": (e.findtext(f"{ATOM}updated") or "")[:10],
            "abstract": re.sub(r"\s+", " ", e.findtext(f"{ATOM}summary") or "").strip(),
            "comment": re.sub(r"\s+", " ", e.findtext(f"{ARXNS}comment") or "").strip(),
            "journal_ref": re.sub(r"\s+", " ", e.findtext(f"{ARXNS}journal_ref") or "").strip(),
            "doi": (e.findtext(f"{ARXNS}doi") or "").strip(),
            "primary_category": (e.find(f"{ARXNS}primary_category").get("term")
                                 if e.find(f"{ARXNS}primary_category") is not None else ""),
            "fetched": time.strftime("%Y-%m-%d"),
        })
    return out


MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def _strip(h):
    import html
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()


def abs_page_meta(a):
    """Fallback when the export API is rate limited: parse arxiv.org/abs/<id>."""
    import html
    page = C.http_get(f"https://arxiv.org/abs/{a}", timeout=60).decode("utf-8", "replace")
    def metas(name):
        return [html.unescape(x) for x in re.findall(rf'<meta name="{name}" content="([^"]*)"', page)]
    title = (metas("citation_title") or [""])[0].strip()
    if not title:
        return None
    authors = []
    for au in metas("citation_author"):
        if "," in au:
            last, first = au.split(",", 1)
            authors.append(f"{first.strip()} {last.strip()}".strip())
        else:
            authors.append(au.strip())
    hist = re.findall(r"\[v(\d+)\]\s*(?:</[^>]+>\s*)*\s*\w{3}, (\d{1,2}) (\w{3}) (\d{4})", page)
    if not hist:
        hist = re.findall(r"\[v(\d+)\].{0,200}?\w{3}, (\d{1,2}) (\w{3}) (\d{4})", page, re.S)
    vers = [(int(v), f"{y}-{MONTHS[mo]:02d}-{int(d):02d}") for v, d, mo, y in hist if mo in MONTHS]
    if not vers:
        return None
    vers.sort()
    def cell(cls):
        m = re.search(rf'<td class="tablecell {cls}[^"]*">(.*?)</td>', page, re.S)
        return _strip(m.group(1)) if m else ""
    prim = re.search(r'<span class="primary-subject">[^<]*\(([^)]+)\)', page)
    return {"arxiv": a, "latest_version": vers[-1][0], "title": re.sub(r"\s+", " ", title),
            "authors": authors, "published": vers[0][1], "updated": vers[-1][1],
            "abstract": re.sub(r"\s+", " ", (metas("citation_abstract") or [""])[0]).strip(),
            "comment": cell("comments"), "journal_ref": cell("jref"),
            "doi": re.sub(r"^https?://doi.org/", "", cell("doi")).split()[0] if cell("doi") else "",
            "primary_category": prim.group(1) if prim else "",
            "fetched": time.strftime("%Y-%m-%d"), "source": "arxiv.org/abs page (API fallback)"}


def arxiv_query(params):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    return parse_feed(C.http_get(url, timeout=60))


def cmd_search(args):
    q = args.query
    res = arxiv_query({"search_query": q, "max_results": args.max, "sortBy": args.sort,
                       "sortOrder": "descending"})
    for r in res:
        fa = r["authors"][0] if r["authors"] else ""
        print(f"{r['arxiv']}\t{r['published']}\t{r['primary_category']}\t{fa}\t{r['title']}")


def title_search(title):
    words = [w for w in C.tokens(title) if w not in C.STOP][:12]
    if not words:
        return None, 0.0
    q = " AND ".join(f"ti:{w}" for w in words)
    best, score = None, 0.0
    for r in arxiv_query({"search_query": q, "max_results": 10}):
        s = C.title_similarity(title, r["title"])
        if s > score:
            best, score = r, s
    return best, score


def cmd_resolve(args):
    code = args.code
    seeds = load_seeds(code)
    with C.locked("meta"):
        meta = C.load_json(META_PATH, {})
    todo = []
    for s in seeds:
        a = norm_arxiv(s.get("arxiv"))
        if s.get("pdf_url") and not a:
            continue  # non-arXiv seed; metadata from seed itself
        if a and a in meta and not args.refresh:
            continue
        todo.append(s)
    # batch id_list lookups
    ids = [norm_arxiv(s["arxiv"]) for s in todo if s.get("arxiv")]
    fetched = {}
    api_ok = True
    for i in range(0, len(ids), 40):
        chunk = ids[i:i + 40]
        try:
            for r in arxiv_query({"id_list": ",".join(chunk), "max_results": len(chunk)}):
                fetched[r["arxiv"]] = r
        except C.HttpError as e:
            print(f"export API failed ({e}); falling back to abs pages")
            api_ok = False
            break
    if not api_ok:
        for a in ids:
            if a in fetched:
                continue
            try:
                r = abs_page_meta(a)
            except C.HttpError as e:
                print(f"[{a}] abs page failed: {e}")
                r = None
            if r:
                fetched[a] = r
    fixes = []
    for s in todo:
        a = norm_arxiv(s.get("arxiv"))
        r = fetched.get(a) if a else None
        sim = C.title_similarity(s.get("title", ""), r["title"]) if r and s.get("title") else (1.0 if r else 0.0)
        if r and sim >= 0.85:
            fetched_ok = r
        else:
            # wrong / missing id: search by title
            if not s.get("title"):
                print(f"[{s['sid']}] no title and id lookup failed: {a}")
                continue
            try:
                best, score = title_search(s["title"])
            except C.HttpError as e:
                print(f"[{s['sid']}] title search failed ({e}); retry resolve later")
                continue
            if best and score >= 0.9:
                fixes.append((s["sid"], a, best["arxiv"], score))
                fetched_ok = best
            else:
                print(f"[{s['sid']}] UNRESOLVED id={a!r} sim={sim:.2f} best={best and best['arxiv']} "
                      f"{best and best['title']!r} score={score:.2f}")
                continue
        with C.locked("meta"):
            meta = C.load_json(META_PATH, {})
            meta[fetched_ok["arxiv"]] = fetched_ok
            C.save_json(META_PATH, meta)
        if norm_arxiv(s.get("arxiv")) != fetched_ok["arxiv"]:
            s["arxiv"] = fetched_ok["arxiv"]
    if fixes:
        # write corrected ids back to the seed file (only the arxiv field changes)
        with C.locked(f"seeds_{code}"):
            cur = load_seeds(code)
            m = {sid: new for sid, _, new, _ in fixes}
            for s in cur:
                if s["sid"] in m:
                    s.setdefault("arxiv_seed_given", s.get("arxiv", ""))
                    s["arxiv"] = m[s["sid"]]
            C.save_json(seeds_path(code), cur)
        for sid, old, new, sc in fixes:
            print(f"[{sid}] id corrected {old or '-'} -> {new} (title sim {sc:.2f})")
    print(f"resolve {code}: {len(todo)} looked up, {len(fixes)} corrected")


# ---------------------------------------------------------------- verification (child process)
def verify_pdf(path, title, authors, team_hint=""):
    pypdf = C.load_pypdf()
    out = {"ok_hard": False, "status": "failed", "notes": []}
    with open(path, "rb") as f:
        head = f.read(1024)
    if b"%PDF-" not in head:
        out["notes"].append("not a PDF (no %PDF- header)")
        return out
    try:
        rd = pypdf.PdfReader(str(path), strict=False)
        if rd.is_encrypted:
            try:
                rd.decrypt("")
            except Exception:
                pass
        n = len(rd.pages)
    except Exception as e:
        out["notes"].append(f"pypdf cannot parse: {e!r}"[:200])
        return out
    out["pages"] = n
    texts = {}

    def page_text(i):
        if i not in texts:
            try:
                texts[i] = rd.pages[i].extract_text() or ""
            except Exception:
                texts[i] = ""
        return texts[i]

    idx = list(range(min(n, 150)))
    if n > 150:
        idx += list(range(max(150, n - 60), n))
    chars = 0
    for i in idx:
        chars += len(page_text(i))
    out["chars_extracted"] = chars
    out["pages_extracted"] = len(idx)
    first = " ".join(page_text(i) for i in range(min(n, 2)))
    first3 = " ".join(page_text(i) for i in range(min(n, 3)))
    alltext = " ".join(texts[i] for i in idx)
    tm = C.title_in_text(title, first) if title else 0.0
    out["title_match"] = round(tm, 2)
    sur = C.surname(authors[0]) if authors else ""
    team = team_hint or (authors[0] if authors and re.search(r"team|group|lab|ai\b|inc\b|google|meta|openai|deepseek|qwen", authors[0], re.I) else "")
    a_first = bool(sur) and C.fold(sur).lower() in C.fold(first3).lower()
    a_any = bool(sur) and C.fold(sur).lower() in C.fold(alltext).lower()
    if sur and not a_first:
        # PDF text extraction often splits diacritics into spacing marks ("Ruci´nski", "ˇ c"):
        # compare letters only, still restricted to the first pages
        squash = lambda x: re.sub(r"[^a-z]", "", C.fold(x).lower())
        a_first = len(squash(sur)) >= 3 and squash(sur) in squash(first3)
    team_ok = bool(team) and any(w.lower() in alltext.lower() for w in re.findall(r"[A-Za-z]{4,}", team)[:2])
    out["author_check"] = "first_pages" if a_first else ("later_pages" if a_any else ("team_name" if team_ok else "not_found"))
    refs = bool(re.search(r"(References|REFERENCES|Bibliography|BIBLIOGRAPHY|Works Cited|Literatur|R[ée]f[ée]rences|Referencias|Refer[êe]ncias|Riferimenti)", alltext))
    out["references_heading"] = refs
    supp = bool(re.match(r"\s*(Supplementary|Supplemental|Appendix)\b", first, re.I))
    out["supplement_like"] = supp
    urls = sorted(set(re.findall(r"https?://(?:github\.com|huggingface\.co|[A-Za-z0-9.-]*github\.io)/[^\s)\]}>,;\"']+", first3)))
    out["urls_first_pages"] = [u.rstrip(".") for u in urls][:8]
    hard = n >= 4 and chars >= 12000 and not supp
    out["ok_hard"] = hard
    if not hard:
        if n < 4:
            out["notes"].append(f"only {n} pages")
        if chars < 12000:
            out["notes"].append(f"only {chars} extractable characters")
        if supp:
            out["notes"].append("looks like a supplement/appendix")
        out["status"] = "failed"
        return out
    soft = []
    if tm < 0.8:
        soft.append(f"title match {tm:.2f} < 0.8")
    if out["author_check"] == "not_found":
        soft.append("first-author surname/team not found")
    if not refs:
        soft.append("no references heading found")
    if soft:
        out["status"] = "pending"
        out["notes"] += soft
    else:
        out["status"] = "verified"
    return out


def run_verify_child(path, title, authors, team_hint="", timeout=600):
    cmd = [sys.executable, "-I", str(Path(__file__).resolve()), "_verify", str(path),
           json.dumps({"title": title, "authors": authors, "team": team_hint})]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return json.loads(p.stdout.strip().splitlines()[-1])
    except subprocess.TimeoutExpired:
        return {"ok_hard": False, "status": "pending", "notes": [f"verification timed out after {timeout}s"]}
    except Exception as e:
        return {"ok_hard": False, "status": "failed", "notes": [f"verifier crashed: {e!r}"[:200]]}


def cmd_verify_child(args):
    p = json.loads(args.payload)
    print(json.dumps(verify_pdf(Path(args.path), p["title"], p["authors"], p.get("team", ""))))


# ---------------------------------------------------------------- other libraries
def other_lib_index():
    """arXiv id -> (lib, relpath) of PDFs verified in sibling libraries (read-only scan of their
    catalog_cn.csv and per-paper state JSON files; files are only ever copied out)."""
    import csv
    import glob
    idx = {}
    rx = re.compile(r"(?:arxiv[:/]|arxiv\.org/(?:abs|pdf)/)([0-9]{4}\.[0-9]{4,5})", re.I)
    for lib in OTHER_LIBS:
        cat = lib / "catalog_cn.csv"
        if cat.exists():
            try:
                with open(cat, encoding="utf-8-sig") as f:
                    for row in csv.DictReader(f):
                        a = norm_arxiv(row.get("arXiv ID") or row.get("arxiv_id") or "")
                        if not a:
                            m = re.search(r"arXiv[:\s]*([0-9]{4}\.[0-9]{4,5})", " ".join(v or "" for v in row.values()), re.I)
                            a = m.group(1) if m else ""
                        rel = row.get("本地相对路径") or row.get("本地路径") or ""
                        if a and rel and (lib / rel).is_file():
                            idx.setdefault(a, (str(lib), rel))
            except Exception:
                pass
        for jf in glob.glob(str(lib / "scripts" / "**" / "*.json"), recursive=True):
            try:
                d = C.load_json(jf, {})
            except Exception:
                continue
            if not isinstance(d, dict):
                continue
            for k, r in d.items():
                if not isinstance(r, dict) or r.get("status") != "verified" or not r.get("local_path"):
                    continue
                rel = r["local_path"]
                if not str(rel).lower().endswith(".pdf") or not (lib / rel).is_file():
                    continue
                m = None
                for v in (r.get("key"), k, r.get("pdf_url"), r.get("source_url"), r.get("landing")):
                    m = rx.search(str(v or "")) or (re.fullmatch(r"([0-9]{4}\.[0-9]{4,5})(v\d+)?", str(v or "")))
                    if m:
                        break
                if m:
                    idx.setdefault(m.group(1), (str(lib), rel))
    return idx


# ---------------------------------------------------------------- download
def paper_key(s):
    a = norm_arxiv(s.get("arxiv"))
    if a:
        return "arxiv:" + a
    if s.get("doi"):
        return "doi:" + s["doi"].lower()
    return "title:" + " ".join(C.tokens(s.get("title", "")))


def seed_meta(s, meta):
    a = norm_arxiv(s.get("arxiv"))
    if a:
        m = meta.get(a)
        if not m:
            return None
        return {"title": m["title"], "authors": m["authors"], "first_public": m["published"],
                "date_precision": "日", "first_public_basis": "arXiv v1 提交日",
                "version": f"arXiv {a}v{m['latest_version']}", "version_date": m["updated"],
                "pdf_url": f"https://arxiv.org/pdf/{a}v{m['latest_version']}",
                "landing": f"https://arxiv.org/abs/{a}v{m['latest_version']}"}
    if not s.get("pdf_url"):
        return None
    return {"title": s["title"], "authors": s.get("authors", []),
            "first_public": s.get("first_public_date", ""),
            "date_precision": s.get("date_precision", ""),
            "first_public_basis": s.get("first_public_basis", "种子人工记录"),
            "version": s.get("version", ""), "version_date": s.get("version_date", ""),
            "pdf_url": s["pdf_url"], "landing": s.get("landing_url", s["pdf_url"])}


def file_name(m, s):
    year = (m["first_public"] or "0000")[:4]
    au = m["authors"][0] if m["authors"] else "Anon"
    sur = C.safe_name(C.surname(au)) if not re.search(r"team|group", au, re.I) else C.safe_name(au.split()[0]) + "Team"
    st = s.get("short") or C.short_title(m["title"])
    return f"{year}_{sur}_{C.safe_name(st)}_en.pdf"


def save_one(code, sid, results):
    """Merge ONE record into the results file under the category lock (other records, e.g. a
    concurrent `manual` promotion, are re-read from disk and kept)."""
    with C.locked(f"results_{code}"):
        cur = C.load_json(results_path(code), {})
        cur[sid] = results[sid]
        C.save_json(results_path(code), cur)
        results.update({k: v for k, v in cur.items() if k != sid})


def cmd_download(args):
    code = args.code
    import fcntl
    C.STATE.mkdir(parents=True, exist_ok=True)
    lockf = open(C.STATE / f".download_{code}_en.lock", "a+")
    try:
        fcntl.flock(lockf, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(f"another download process for category {code} is running; not starting a second one")
    seeds = load_seeds(code)
    rpath = results_path(code)
    results = C.load_json(rpath, {})
    meta = C.load_json(META_PATH, {})
    others = other_lib_index()
    C.PAPERS.mkdir(exist_ok=True)

    def n_verified():
        return sum(1 for r in results.values() if r.get("status") == "verified")

    order = [s for s in seeds if not s.get("reserve")] + [s for s in seeds if s.get("reserve")]
    for s in order:
        sid = s["sid"]
        prev = results.get(sid, {})
        if prev.get("status") == "verified":
            if prev.get("key") != paper_key(s):
                print(f"[{sid}] WARNING seed changed after verification ({prev.get('key')} -> {paper_key(s)}); keeping record")
            continue
        if prev.get("status") in ("pending", "duplicate_elsewhere", "excluded"):
            continue
        if prev.get("status") == "failed" and not args.retry_failed:
            continue
        if s.get("exclude") or s.get("cross_only"):
            continue
        if not args.all and n_verified() >= args.target:
            break
        m = seed_meta(s, meta)
        if not m:
            results[sid] = {"status": "failed", "stage": "metadata", "key": paper_key(s),
                            "notes": ["metadata not resolved (run resolve) or no pdf_url"], "time": time.strftime("%F %T")}
            save_one(code, sid, results)
            print(f"[{sid}] no metadata")
            continue
        key = paper_key(s)
        with C.locked("claims"):
            claims = C.load_json(CLAIMS_PATH, {})
            cl = claims.get(key)
            if cl and (cl["cat"], cl["sid"]) != (code, sid):
                results[sid] = {"status": "duplicate_elsewhere", "key": key, "claimed_by": cl,
                                "notes": [f"already primary in category {cl['cat']} ({cl['sid']}); add as cross tag there"],
                                "time": time.strftime("%F %T")}
                save_one(code, sid, results)
                print(f"[{sid}] duplicate of {cl}")
                continue
            claims[key] = {"cat": code, "sid": sid, "state": "downloading"}
            C.save_json(CLAIMS_PATH, claims)
        stage = C.STAGING / f"{C.cat_key(code)}_{sid}_{int(time.time())}"
        stage.mkdir(parents=True)
        tmp = stage / "download.pdf"
        rec = {"key": key, "title": m["title"], "source_url": m["pdf_url"], "landing": m["landing"],
               "version": m["version"], "version_date": m["version_date"], "time": time.strftime("%F %T")}
        a = norm_arxiv(s.get("arxiv"))
        try:
            if a and a in others:
                lib, rel = others[a]
                shutil.copyfile(Path(lib) / rel, tmp)
                rec["origin"] = "reused_other_library"
                rec["origin_path"] = str(Path(lib) / rel)
            else:
                st, final, ctype, nbytes = C.http_get(m["pdf_url"], dest=tmp)
                rec.update({"origin": "downloaded_this_round", "http_status": st, "final_url": final,
                            "content_type": ctype, "bytes": nbytes})
        except C.HttpError as e:
            rec.update({"status": "failed", "stage": "download", "notes": [str(e)]})
            results[sid] = rec
            save_one(code, sid, results)
            with C.locked("claims"):
                claims = C.load_json(CLAIMS_PATH, {})
                if claims.get(key, {}).get("sid") == sid:
                    del claims[key]
                C.save_json(CLAIMS_PATH, claims)
            shutil.rmtree(stage, ignore_errors=True)
            print(f"[{sid}] download failed: {e}")
            continue
        v = run_verify_child(tmp, m["title"], m["authors"], s.get("team", ""))
        rec["verification"] = v
        rec["status"] = v["status"]
        rec["notes"] = v.get("notes", [])
        if v["status"] in ("verified", "pending"):
            rec["sha256"] = C.sha256_file(tmp)
            name = file_name(m, s)
            dest = C.PAPERS / name
            if dest.exists() and C.sha256_file(dest) != rec["sha256"]:
                dest = C.PAPERS / name.replace("_en.pdf", f"_{C.safe_name(a or rec['sha256'][:8])}_en.pdf")
            if not dest.exists():
                shutil.move(str(tmp), dest)
            rec["local_path"] = str(dest.relative_to(C.ROOT))
        results[sid] = rec
        save_one(code, sid, results)
        with C.locked("claims"):
            claims = C.load_json(CLAIMS_PATH, {})
            if rec["status"] in ("verified", "pending"):
                claims[key] = {"cat": code, "sid": sid, "state": rec["status"], "file": rec.get("local_path")}
            elif claims.get(key, {}).get("sid") == sid:
                del claims[key]
            C.save_json(CLAIMS_PATH, claims)
        shutil.rmtree(stage, ignore_errors=True)
        print(f"[{sid}] {rec['status']}: {m['title'][:70]} | p={v.get('pages')} ch={v.get('chars_extracted')} "
              f"tm={v.get('title_match')} au={v.get('author_check')} {'; '.join(rec['notes'])}")
    cmd_status(args)


# ---------------------------------------------------------------- status / brief / manual
def first_public_of(s, meta):
    m = seed_meta(s, meta)
    return (m or {}).get("first_public", "")


def cmd_status(args):
    code = args.code
    seeds = load_seeds(code)
    results = C.load_json(results_path(code), {})
    meta = C.load_json(META_PATH, {})
    by = {}
    for s in seeds:
        if s.get("cross_only"):
            by.setdefault("cross_only (tag only, primary elsewhere)", []).append(s)
            continue
        if s.get("exclude"):
            by.setdefault("excluded", []).append(s)
            continue
        st = results.get(s["sid"], {}).get("status", "todo" if not s.get("reserve") else "reserve")
        by.setdefault(st, []).append(s)
    ver = by.get("verified", [])
    old = [s for s in ver if first_public_of(s, meta) and first_public_of(s, meta) < C.WINDOW_START]
    undated = [s for s in ver if not first_public_of(s, meta)]
    recent = len(ver) - len(old) - len(undated)
    pend = by.get("pending", [])
    fail = by.get("failed", [])
    print(f"[{code} {C.CAT_BY_CODE[code][2]}] 已核验完整资料 {len(ver)} / 目标约 50；待核验 {len(pend)}；下载失败 {len(fail)}。"
          f" 近三年 {recent}/{len(ver)} = {recent / max(1, len(ver)):.1%}；三年前 {len(old)}（上限 5）；未定日期 {len(undated)}")
    for k, v in sorted(by.items()):
        if k != "verified":
            print(f"  {k}: {len(v)}")
    for s in old:
        print(f"  OLD {s['sid']} {first_public_of(s, meta)} {s.get('title', '')[:60]} | reason: {s.get('old_reason', '')[:40]!r}")
    for s in pend + fail + by.get("duplicate_elsewhere", []):
        r = results.get(s["sid"], {})
        print(f"  {r['status'].upper()} {s['sid']} {s.get('title', '')[:60]} | {'; '.join(r.get('notes', []))[:160]}")
    subs = {}
    for s in ver:
        subs[s.get("subtopic", "?")] = subs.get(s.get("subtopic", "?"), 0) + 1
    print("  subtopics:", "; ".join(f"{k} {v}" for k, v in sorted(subs.items(), key=lambda x: -x[1])))


def cmd_brief(args):
    code = args.code
    seeds = load_seeds(code)
    results = C.load_json(results_path(code), {})
    meta = C.load_json(META_PATH, {})
    ann = C.load_json(C.ANNOT / f"{C.cat_key(code)}_annot_cn.json", {})
    lines = [f"# Brief for annotation: {code} {C.CAT_BY_CODE[code][2]}\n"]
    for s in seeds:
        r = results.get(s["sid"], {})
        if r.get("status") not in ("verified", "pending"):
            continue
        if args.missing_only and s["sid"] in ann:
            continue
        a = norm_arxiv(s.get("arxiv"))
        m = meta.get(a, {}) if a else {}
        lines.append(f"## {s['sid']} | {r.get('title') or s.get('title')}")
        lines.append(f"- arXiv: {a or '-'}  first public: {m.get('published', s.get('first_public_date', ''))}  "
                     f"latest: {m.get('updated', '')}  primary cat: {m.get('primary_category', '')}")
        au = m.get("authors") or s.get("authors") or []
        lines.append(f"- authors ({len(au)}): {'; '.join(au[:6])}{' ...' if len(au) > 6 else ''}")
        lines.append(f"- seed subtopic: {s.get('subtopic', '')}; type: {s.get('type', '')}; cross: {s.get('cross', [])}")
        if m.get("comment"):
            lines.append(f"- arXiv comment: {m['comment']}")
        if m.get("journal_ref"):
            lines.append(f"- journal_ref: {m['journal_ref']}")
        if m.get("doi"):
            lines.append(f"- doi: {m['doi']}")
        urls = r.get("verification", {}).get("urls_first_pages", [])
        if urls:
            lines.append(f"- URLs on first pages of PDF: {' '.join(urls)}")
        lines.append(f"- pages: {r.get('verification', {}).get('pages')}")
        lines.append(f"\nABSTRACT: {m.get('abstract') or s.get('abstract', '(non-arXiv; see seed)')}\n")
    out = C.WORK / f"{C.cat_key(code)}_brief_en.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out} ({len(lines)} lines)")


def cmd_manual(args):
    code = args.code
    rpath = results_path(code)
    with C.locked(f"results_{code}"):
        results = C.load_json(rpath, {})
        r = results.get(args.sid)
        if not r or r.get("status") != "pending":
            sys.exit(f"{args.sid} is not pending: {r and r.get('status')}")
        if not r.get("verification", {}).get("ok_hard"):
            sys.exit("hard checks not passed; cannot promote")
        if len(args.note) < 20:
            sys.exit("note too short: say exactly what was checked")
        r["status"] = "verified"
        r["manual_verification"] = {"note": args.note, "time": time.strftime("%F %T")}
        C.save_json(rpath, results)
    with C.locked("claims"):
        claims = C.load_json(CLAIMS_PATH, {})
        if r["key"] in claims:
            claims[r["key"]]["state"] = "verified"
        C.save_json(CLAIMS_PATH, claims)
    print(f"{args.sid} promoted to verified")


def cmd_text(args):
    """Print the first pages' text of a downloaded paper (for manual checks)."""
    pypdf = C.load_pypdf()
    r = C.load_json(results_path(args.code), {}).get(args.sid, {})
    p = C.ROOT / r.get("local_path", "")
    rd = pypdf.PdfReader(str(p), strict=False)
    for i in range(min(args.pages, len(rd.pages))):
        print(f"--- page {i + 1} ---")
        print((rd.pages[i].extract_text() or "")[:args.chars])


def cmd_venue(args):
    code = args.code
    seeds = load_seeds(code)
    results = C.load_json(results_path(code), {})
    for s in seeds:
        r = results.get(s["sid"], {})
        if r.get("status") != "verified":
            continue
        with C.locked("openalex"):
            cache = C.load_json(OPENALEX_PATH, {})
        if r["key"] in cache and not args.refresh:
            continue
        title = r.get("title") or s.get("title")
        q = re.sub(r"[^A-Za-z0-9 ]+", " ", C.fold(title))
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
            {"filter": f"title.search:{q}", "per-page": 8,
             "select": "id,doi,title,publication_date,type,primary_location,locations"})
        try:
            data = json.loads(C.http_get(url, timeout=60))
        except Exception as e:
            print(f"[{s['sid']}] openalex error {e}")
            continue
        found = []
        for w in data.get("results", []):
            if C.title_similarity(title, w.get("title") or "") < 0.93:
                continue
            for loc in w.get("locations") or []:
                src = (loc or {}).get("source") or {}
                name = src.get("display_name") or ""
                if not name or re.search(r"arxiv|ssrn|research ?gate|zenodo|semantic scholar|europe pmc|pubmed central|hal|openreview$", name, re.I):
                    continue
                found.append({"source": name, "source_type": src.get("type"), "version": loc.get("version"),
                              "landing": loc.get("landing_page_url"), "work_type": w.get("type"),
                              "work_doi": w.get("doi"), "pub_date": w.get("publication_date")})
        with C.locked("openalex"):
            cache = C.load_json(OPENALEX_PATH, {})
            cache[r["key"]] = {"venues": found, "checked": time.strftime("%F")}
            C.save_json(OPENALEX_PATH, cache)
        print(f"[{s['sid']}] {len(found)} venue loc(s): {'; '.join(sorted({f['source'] for f in found}))[:120]}")


def main():
    sys.stdout.reconfigure(line_buffering=True)
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("resolve"); p.add_argument("code"); p.add_argument("--refresh", action="store_true"); p.set_defaults(f=cmd_resolve)
    p = sub.add_parser("download"); p.add_argument("code"); p.add_argument("--target", type=int, default=50)
    p.add_argument("--retry-failed", action="store_true"); p.add_argument("--all", action="store_true"); p.set_defaults(f=cmd_download)
    p = sub.add_parser("status"); p.add_argument("code"); p.set_defaults(f=cmd_status)
    p = sub.add_parser("brief"); p.add_argument("code"); p.add_argument("--missing-only", action="store_true"); p.set_defaults(f=cmd_brief)
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--max", type=int, default=40)
    p.add_argument("--sort", default="relevance", choices=["relevance", "submittedDate", "lastUpdatedDate"]); p.set_defaults(f=cmd_search)
    p = sub.add_parser("manual"); p.add_argument("code"); p.add_argument("sid"); p.add_argument("--note", required=True); p.set_defaults(f=cmd_manual)
    p = sub.add_parser("text"); p.add_argument("code"); p.add_argument("sid"); p.add_argument("--pages", type=int, default=2)
    p.add_argument("--chars", type=int, default=3000); p.set_defaults(f=cmd_text)
    p = sub.add_parser("venue"); p.add_argument("code"); p.add_argument("--refresh", action="store_true"); p.set_defaults(f=cmd_venue)
    p = sub.add_parser("_verify"); p.add_argument("path"); p.add_argument("payload"); p.set_defaults(f=cmd_verify_child)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
