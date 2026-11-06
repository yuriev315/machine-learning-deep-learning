#!/usr/bin/env python3
"""Size-gated, hash-verified downloader. Driven by manifests/resources.json.

Rules enforced here: a resource larger than 100 MiB is never downloaded -- it gets a .url
placeholder instead, unless the entry is marked approved_oversize (explicit user approval, 2026-11-05). Every download is checked against the official SHA256 when one exists;
without one it is recorded as HASH_UNVERIFIED (local hash only), never as verified.
"""
import csv, hashlib, json, os, sys, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = 104857600
HARD_LIMIT = 2 * 1024**3   # GitHub-style sanity cap, even for approved files
UA = {"User-Agent": "mfea-fetch/1.0"}

def remote_size(url):
    req = urllib.request.Request(url, method="HEAD", headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            v = r.headers.get("Content-Length")
            return int(v) if v else None
    except Exception as e:
        print("  HEAD failed:", e)
        return None

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def download(url, dest, limit=LIMIT):
    tmp = dest + ".part"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r, open(tmp, "wb") as f:
        n = 0
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            n += len(b)
            if n > limit:
                f.close(); os.remove(tmp)
                raise RuntimeError("exceeded size limit during download")
            f.write(b)
    os.replace(tmp, dest)

def main():
    res = json.load(open(os.path.join(ROOT, "manifests/resources.json")))
    only = set(sys.argv[1:])
    spath = os.path.join(ROOT, "manifests/download_status.csv")
    status = {}
    if os.path.exists(spath):
        status = {r["name"]: r for r in csv.DictReader(open(spath))}
    for r in res:
        if only and r["name"] not in only:
            continue
        print("*", r["name"], r["version"])
        size = r.get("expected_size") or remote_size(r["url"])
        fname = r.get("filename") or r["url"].split("/")[-1].split("?")[0]
        row = dict(name=r["name"], version=r["version"], filename=fname, url=r["url"], size=size or "",
                   official_sha256=r.get("sha256", ""), local_sha256="", status="", note=r.get("note", ""))
        limit = HARD_LIMIT if r.get("approved_oversize") else LIMIT
        if r.get("placeholder") or (size and size > limit):
            row["status"] = "URL_PLACEHOLDER"
            os.makedirs(os.path.join(ROOT, "placeholders"), exist_ok=True)
            with open(os.path.join(ROOT, "placeholders", fname + ".url"), "w") as f:
                f.write(f"[InternetShortcut]\nURL={r['url']}\n; filename={fname}\n; expected_size={size or 'unknown'}\n; version={r['version']}\n"
                        f"; purpose={r.get('purpose','')}\n; license={r.get('license','')}\n; platform={r.get('platform','')}\n"
                        f"; official_sha256={r.get('sha256','unavailable')}\n; download: {r.get('instructions','curl -LO <URL>')}\n")
        else:
            d = os.path.join(ROOT, "deps/archives", r["name"])
            os.makedirs(d, exist_ok=True)
            dest = os.path.join(d, fname)
            try:
                if not os.path.exists(dest):
                    download(r["url"], dest, limit)
                if os.path.getsize(dest) > limit:
                    raise RuntimeError("file over limit")
                row["local_sha256"] = sha256(dest)
                row["size"] = os.path.getsize(dest)
                if r.get("sha1"):
                    h1 = hashlib.sha1(open(dest, "rb").read()).hexdigest()
                    row["official_sha256"] = "sha1:" + r["sha1"]
                    if h1 != r["sha1"]:
                        os.remove(dest); row["status"] = "SHA1_MISMATCH_REMOVED"
                    else:
                        row["status"] = "SHA1_VERIFIED"
                elif r.get("sha512"):
                    h5 = hashlib.sha512(open(dest, "rb").read()).hexdigest()
                    row["official_sha256"] = "sha512:" + r["sha512"][:32] + "..."
                    if h5 != r["sha512"]:
                        os.remove(dest); row["status"] = "SHA512_MISMATCH_REMOVED"
                    else:
                        row["status"] = "SHA512_VERIFIED"
                elif r.get("sha256"):
                    if r["sha256"] != row["local_sha256"]:
                        os.remove(dest)
                        row["status"] = "SHA256_MISMATCH_REMOVED"
                    else:
                        row["status"] = "SHA256_VERIFIED"
                else:
                    row["status"] = "HASH_UNVERIFIED_NO_OFFICIAL_DIGEST"
            except Exception as e:
                row["status"] = "DOWNLOAD_FAILED"; row["note"] = str(e)[:120]
        print("   ->", row["status"], row["size"])
        status[r["name"]] = row
    with open(spath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name","version","filename","url","size","official_sha256","local_sha256","status","note"])
        w.writeheader()
        for k in sorted(status):
            w.writerow(status[k])
main()
