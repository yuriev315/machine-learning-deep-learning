#!/usr/bin/env python3
"""List lecture files linked from a course page.

usage: python3 -I course_links.py <course_dir_name> <page_url> <regex_on_url> [<out_items.json>]
Appends items {path, url} to out_items.json (default state/course_new_items.json).
"""
import json, os, re, sys, subprocess, urllib.parse
name, page, pat = sys.argv[1:4]
out = sys.argv[4] if len(sys.argv) > 4 else 'state/course_new_items.json'
html = subprocess.run(['curl', '-sL', '-A', 'Mozilla/5.0', '--max-time', '60', page], capture_output=True).stdout.decode('utf-8', 'replace')
links = []
for m in re.finditer(r'''href\s*=\s*(?:"([^"]+)"|'([^']+)'|([^\s>]+))''', html, re.I):
    u = urllib.parse.urljoin(page, (m.group(1) or m.group(2) or m.group(3)).strip())
    if re.search(pat, u, re.I) and u not in links: links.append(u)
items = json.load(open(out)) if os.path.exists(out) else {}
for i, u in enumerate(links, 1):
    base = urllib.parse.unquote(u.split('?')[0].rstrip('/').split('/')[-1])
    stem, ext = os.path.splitext(base)
    stem = re.sub(r'[^A-Za-z0-9._-]+', '_', stem).strip('_')
    p = f'university_materials/{name}/{i:02d}_{stem}_en{ext.lower()}'
    items[p] = dict(path=p, url=u, course=name, page=page)
json.dump(items, open(out, 'w'), indent=1, ensure_ascii=False)
print(name, len(links)); [print('  ', u) for u in links[:5]]
