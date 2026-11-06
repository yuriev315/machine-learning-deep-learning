#!/usr/bin/env python3
"""Download the files behind .url placeholders and check their SHA-256.

usage: python3 -I fetch_placeholders.py <library_dir> <download_dir> [--only SUBSTRING]
Each <name>.url gives URL, SizeBytes and SHA256; the file is saved at the same relative path
under <download_dir>. A mismatching SHA-256 is reported (sites sometimes update files).
"""
import configparser, hashlib, os, sys, time, urllib.request
lib, dest = sys.argv[1], sys.argv[2]
only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else ''
ok = bad = fail = 0
for root, _, files in os.walk(lib):
    for f in sorted(files):
        if not f.endswith('.url'): continue
        p = os.path.join(root, f); rel = os.path.relpath(p, lib)[:-4]
        if only and only not in rel: continue
        c = configparser.ConfigParser(interpolation=None); c.read(p, encoding='utf-8')
        url = c.get('InternetShortcut', 'URL', fallback=''); sha = c.get('File', 'SHA256', fallback='')
        out = os.path.join(dest, rel)
        if os.path.exists(out): continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            h = hashlib.sha256()
            with urllib.request.urlopen(req, timeout=120) as r, open(out + '.part', 'wb') as o:
                for b in iter(lambda: r.read(1 << 20), b''): h.update(b); o.write(b)
            os.replace(out + '.part', out)
            if sha and h.hexdigest() != sha: bad += 1; print('SHA256 differs:', rel)
            else: ok += 1
        except Exception as e:
            fail += 1; print('failed:', rel, e)
        time.sleep(3 if 'arxiv.org' in url else 0.5)
print(f'ok {ok}, sha256 differs {bad}, failed {fail}')
