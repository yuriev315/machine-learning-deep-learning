#!/usr/bin/env python3
"""arXiv metadata and licence cache.

usage: python3 -I arxiv_meta.py <cache.json> <id> [<id> ...]   (ids may carry a version, e.g. 2404.00456v2)
       python3 -I arxiv_meta.py <cache.json> --file ids.txt
Metadata from export.arxiv.org/api (batches of 40), licence from oaipmh.arxiv.org (one per id).
"""
import json, os, re, sys, time, urllib.request, xml.etree.ElementTree as ET
UA = 'literature-archive/1.0'
cache_p = sys.argv[1]
ids = open(sys.argv[3]).read().split() if sys.argv[2] == '--file' else sys.argv[2:]
cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
def save():
    json.dump(cache, open(cache_p + '.tmp', 'w'), ensure_ascii=False, indent=0); os.replace(cache_p + '.tmp', cache_p)
import subprocess
def get(u):
    if 'oaipmh' in u:
        for a in range(5):
            r = subprocess.run(['curl', '-s', '--max-time', '40', '-A', UA, '-w', '\n%{http_code}', u], capture_output=True)
            body, _, code = r.stdout.rpartition(b'\n')
            if code == b'200': return body
            time.sleep(10 * (a + 1))
        raise RuntimeError(u)
    for a in range(5):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=60).read()
        except Exception as e:
            time.sleep(10 * (a + 1))
    raise RuntimeError(u)
base = lambda i: re.sub(r'v\d+$', '', i)
A = '{http://www.w3.org/2005/Atom}'; X = '{http://arxiv.org/schemas/atom}'
need = [i for i in dict.fromkeys(base(i) for i in ids) if i not in cache or 'title' not in cache[i]]
for k in range(0, len(need), 40):
    chunk = need[k:k + 40]
    x = ET.fromstring(get('https://export.arxiv.org/api/query?max_results=50&id_list=' + ','.join(chunk)))
    for e in x.findall(A + 'entry'):
        idu = e.findtext(A + 'id') or ''
        m = re.search(r'abs/(.+?)(v\d+)?$', idu)
        if not m: continue
        i = m.group(1)
        d = cache.setdefault(i, {})
        d.update(id=i, latest=(m.group(2) or ''), title=' '.join((e.findtext(A + 'title') or '').split()),
                 summary=' '.join((e.findtext(A + 'summary') or '').split()),
                 authors=[a.findtext(A + 'name') for a in e.findall(A + 'author')],
                 published=e.findtext(A + 'published'), updated=e.findtext(A + 'updated'),
                 primary=(e.find(X + 'primary_category').get('term') if e.find(X + 'primary_category') is not None else ''),
                 categories=[c.get('term') for c in e.findall(A + 'category')],
                 doi=e.findtext(X + 'doi') or '', journal_ref=e.findtext(X + 'journal_ref') or '', comment=e.findtext(X + 'comment') or '')
    save(); time.sleep(3.2)
    print('meta', k + len(chunk), len(need), flush=True)
need = [i for i in dict.fromkeys(base(i) for i in ids) if 'license' not in cache.get(i, {})]
for n, i in enumerate(need):
    t = get('https://export.arxiv.org/abs/' + i).decode('utf-8', 'replace')
    m = re.search(r'class="abs-license"[^>]*>\s*<a href="([^"]+)"', t) or re.search(r'href="(https?://[^"]*(?:creativecommons\.org/(?:licenses|publicdomain)|arxiv\.org/licenses)/[^"]*)"', t)
    cache.setdefault(i, {})['license'] = m.group(1).strip() if m else ''
    if n % 20 == 0: save(); print('lic', n, len(need), flush=True)
    time.sleep(2.0)
save(); print('done', flush=True)
