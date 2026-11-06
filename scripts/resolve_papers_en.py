#!/usr/bin/env python3
"""Resolve paper seeds (categories C01-C10) to bibliographic records and stable library IDs.

Seed files: scripts/seeds/Cxx_*_cn.txt, one paper per line, fields separated by " | ":
    id_hint | expected title | kind | cross categories | selection reason [| reason kept if old]
  id_hint : arXiv ID (e.g. 2312.00752), "doi:<DOI>", or "-" (resolve by title search)
  kind    : R = original research, S = survey/review, T = tutorial
  cross   : comma-separated category codes (e.g. C04,C10) or "-"
Lines starting with "#" are comments.

Steps (each cached under scripts/cache/, so re-runs only do missing work):
  1. arXiv API id_list lookup for every hinted ID;
  2. accept the hint only if the arXiv title matches the expected title (token Jaccard >= 0.6);
     otherwise search arXiv by title and take the best match >= 0.75;
  3. DOI-only seeds: Crossref metadata;
  4. Semantic Scholar batch lookup (venue / publication date / DOI) for resolved arXiv IDs;
  5. assign library IDs (MLP0001...) keyed by arXiv ID, else DOI, else normalised title;
     the same paper seeded in several categories becomes one record with cross categories.

Outputs: cache/registry_en.json (key -> ID, stable across runs) and cache/papers_resolved_en.json.

Usage: python3 -I scripts/resolve_papers_en.py
"""
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import (CACHE, SCRIPTS, http, load, norm, save, title_similarity,  # noqa: E402
                       tokens, window_status)

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$|^[a-z\-]+(\.[A-Z]{2})?/\d{7}$")


def parse_seeds():
    out = []
    for f in sorted((SCRIPTS / "seeds").glob("C[01][0-9]_*_cn.txt")):
        cat = f.name[:3]
        for ln, line in enumerate(f.read_text().splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            p = [x.strip() for x in line.split(" | ")]
            if len(p) < 5:
                sys.exit(f"{f.name}:{ln}: expected >= 5 fields: {line}")
            cross = [c for c in p[3].split(",") if c.strip() and c.strip() != "-"]
            out.append({"cat": cat, "src": f"{f.name}:{ln}", "hint": p[0], "title": p[1],
                        "kind": p[2], "cross": [c.strip() for c in cross], "reason": p[4],
                        "old_reason": p[5] if len(p) > 5 else ""})
    return out


def parse_atom(body):
    out = []
    for e in ET.fromstring(body).findall("a:entry", ATOM):
        abs_url = e.findtext("a:id", "", ATOM)
        if "/abs/" not in abs_url:
            continue
        vid = abs_url.rsplit("/abs/", 1)[-1]
        out.append({
            "id": re.sub(r"v\d+$", "", vid), "latest_version": vid, "abs_url": abs_url,
            "title": " ".join(e.findtext("a:title", "", ATOM).split()),
            "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
            "published": e.findtext("a:published", "", ATOM)[:10],
            "updated": e.findtext("a:updated", "", ATOM)[:10],
            "abstract": " ".join(e.findtext("a:summary", "", ATOM).split()),
            "comment": " ".join((e.findtext("arxiv:comment", "", ATOM) or "").split()),
            "journal_ref": " ".join((e.findtext("arxiv:journal_ref", "", ATOM) or "").split()),
            "doi": e.findtext("arxiv:doi", "", ATOM) or "",
            "primary_category": (e.find("arxiv:primary_category", ATOM).get("term")
                                 if e.find("arxiv:primary_category", ATOM) is not None else ""),
        })
    return out


def arxiv_by_ids(ids, cache):
    todo = sorted({i for i in ids if i not in cache})
    for i in range(0, len(todo), 50):
        chunk = todo[i:i + 50]
        st, body, _, _ = http("https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk),
                              accept="application/atom+xml")
        if st != 200:
            print("arXiv id_list failed", st, chunk[:3], file=sys.stderr)
            continue
        got = {r["id"]: r for r in parse_atom(body)}
        for a in chunk:
            cache[a] = got.get(a, {"error": "not returned"})
        save(CACHE / "arxiv_en.json", cache)


def arxiv_title_search(title, scache):
    k = norm(title)
    if k in scache:
        return scache[k]
    words = [w for w in re.findall(r"[A-Za-z0-9]+", title)]
    queries = ['ti:"' + " ".join(words) + '"', " AND ".join("ti:" + t for t in tokens(title)[:8])]
    res = []
    for q in queries:
        st, body, _, _ = http("https://export.arxiv.org/api/query?max_results=8&search_query="
                              + urllib.parse.quote(q), accept="application/atom+xml")
        if st == 200:
            res = parse_atom(body)
            if any(title_similarity(title, r["title"]) >= 0.75 for r in res):
                break
    scache[k] = res
    save(CACHE / "arxiv_search_en.json", scache)
    return res


def crossref(doi, ccache):
    if doi in ccache:
        return ccache[doi]
    st, body, _, _ = http("https://api.crossref.org/works/" + urllib.parse.quote(doi), accept="application/json")
    if st != 200:
        ccache[doi] = {"error": f"status {st}"}
    else:
        m = json.loads(body)["message"]

        def d(key):
            p = (m.get(key) or {}).get("date-parts", [[None]])[0]
            return "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(p) if x) if p and p[0] else ""
        ccache[doi] = {
            "title": " ".join((m.get("title") or [""])[0].split()),
            "authors": [" ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")
                        for a in m.get("author", [])],
            "published_online": d("published-online"), "published_print": d("published-print"),
            "issued": d("issued"), "container": (m.get("container-title") or [""])[0],
            "publisher": m.get("publisher", ""), "type": m.get("type", ""),
            "abstract": re.sub(r"<[^>]+>", "", m.get("abstract", "") or ""),
        }
    save(CACHE / "crossref_en.json", ccache)
    return ccache[doi]


def s2_batch(ids, s2):
    todo = [i for i in ids if i not in s2]
    fields = "title,venue,publicationVenue,year,publicationDate,externalIds,journal,publicationTypes"
    for i in range(0, len(todo), 400):
        chunk = todo[i:i + 400]
        st, body, _, _ = http("https://api.semanticscholar.org/graph/v1/paper/batch?fields=" + fields,
                              data=json.dumps({"ids": ["arXiv:" + a for a in chunk]}).encode(),
                              accept="application/json", headers={"Content-Type": "application/json"}, tries=4)
        if st != 200:
            print("Semantic Scholar batch failed", st, body[:200], file=sys.stderr)
            continue
        for a, rec in zip(chunk, json.loads(body)):
            if rec is None:
                s2[a] = {"error": "not found"}
                continue
            pv = rec.get("publicationVenue") or {}
            s2[a] = {"title": rec.get("title"), "venue": rec.get("venue") or "",
                     "venue_full": pv.get("name") or "", "venue_type": pv.get("type") or "",
                     "year": rec.get("year"), "date": rec.get("publicationDate") or "",
                     "doi": (rec.get("externalIds") or {}).get("DOI") or "",
                     "journal": (rec.get("journal") or {}).get("name") or "",
                     "types": rec.get("publicationTypes") or []}
        save(CACHE / "s2_en.json", s2)


def main():
    seeds = parse_seeds()
    ax = load(CACHE / "arxiv_en.json", {})
    sc = load(CACHE / "arxiv_search_en.json", {})
    cc = load(CACHE / "crossref_en.json", {})
    s2 = load(CACHE / "s2_en.json", {})
    reg = load(CACHE / "registry_en.json", {})

    arxiv_by_ids([s["hint"] for s in seeds if ARXIV_RE.match(s["hint"])], ax)

    problems, resolved = [], {}
    for s in seeds:
        rec = None
        if ARXIV_RE.match(s["hint"]):
            m = ax.get(s["hint"]) or {}
            if m.get("title") and title_similarity(s["title"], m["title"]) >= 0.6:
                rec = m
        if rec is None and not s["hint"].startswith("doi:"):
            cands = arxiv_title_search(s["title"], sc)
            best = max(cands, key=lambda r: title_similarity(s["title"], r["title"]), default=None)
            if best and title_similarity(s["title"], best["title"]) >= 0.75:
                rec = best
                ax.setdefault(best["id"], best)
                if s["hint"] not in ("-", best["id"]):
                    problems.append(f"{s['src']}: hint {s['hint']} wrong -> {best['id']} ({best['title'][:60]})")
        if rec is not None:
            s["key"], s["arxiv"] = "arxiv:" + rec["id"], rec
        elif s["hint"].startswith("doi:"):
            doi = s["hint"][4:].lower()
            c = crossref(doi, cc)
            if c.get("title") and title_similarity(s["title"], c["title"]) >= 0.6:
                s["key"], s["crossref"], s["doi"] = "doi:" + doi, c, doi
            else:
                problems.append(f"{s['src']}: DOI {doi} title mismatch/unavailable: {c.get('title') or c}")
        else:
            problems.append(f"{s['src']}: UNRESOLVED '{s['title'][:70]}' (hint {s['hint']})")
        if "key" in s:
            resolved.setdefault(s["key"], []).append(s)
    save(CACHE / "arxiv_en.json", ax)

    s2_batch(sorted(k[6:] for k in resolved if k.startswith("arxiv:")), s2)

    nxt = max([int(v[3:]) for v in reg.values()] + [0]) + 1
    out = {}
    for key, group in resolved.items():
        if key not in reg:
            reg[key] = f"MLP{nxt:04d}"
            nxt += 1
        pid = reg[key]
        first = group[0]
        cats = [first["cat"]]
        for g in group:
            for c in [g["cat"]] + g["cross"]:
                if c not in cats:
                    cats.append(c)
        if len(group) > 1:
            problems.append(f"merged duplicate seeds {[g['src'] for g in group]} -> {pid}")
        a = first.get("arxiv") or {}
        c = first.get("crossref") or {}
        aid = a.get("id", "")
        sx = s2.get(aid, {}) if aid else {}
        first_pub = a.get("published") or c.get("published_online") or c.get("issued") or c.get("published_print")
        out[pid] = {
            "id": pid, "key": key, "primary": first["cat"], "cats": cats, "kind": first["kind"],
            "seed_title": first["title"], "title": a.get("title") or c.get("title"),
            "authors": a.get("authors") or c.get("authors") or [],
            "arxiv": aid, "latest_version": a.get("latest_version", ""),
            "doi": a.get("doi") or sx.get("doi") or first.get("doi", ""),
            "first_public": first_pub or "",
            "first_public_source": "arXiv v1 提交日" if a.get("published") else ("Crossref 日期" if first_pub else ""),
            "version_date": a.get("updated") or "",
            "window": window_status(first_pub or ""),
            "abstract": a.get("abstract") or c.get("abstract") or "",
            "arxiv_comment": a.get("comment", ""), "journal_ref": a.get("journal_ref", ""),
            "s2": sx, "crossref": c, "reason": first["reason"],
            "old_reason": next((g["old_reason"] for g in group if g["old_reason"]), ""),
            "seed_src": [g["src"] for g in group],
        }
    save(CACHE / "registry_en.json", reg)
    save(CACHE / "papers_resolved_en.json", out)
    for p in problems:
        print("PROBLEM", p)
    print(f"seeds={len(seeds)} resolved_unique={len(out)} problems={len(problems)}")


if __name__ == "__main__":
    main()
