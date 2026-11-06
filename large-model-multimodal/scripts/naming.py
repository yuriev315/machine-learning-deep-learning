"""File names for papers: YYYY_FirstAuthorSurname_ShortTitle_en.pdf"""
import re, unicodedata
STOP = {'a', 'an', 'the', 'of', 'for', 'and', 'with', 'via', 'to', 'in', 'on', 'from', 'by', 'is', 'are', 'at', 'as', 'its', 'towards', 'toward', 'using', 'into', 'your', 'you', 'we', 'do', 'can', 'all', 'need'}
def ascii(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
def short_title(title, n=4):
    t = ascii(title).replace('$', '')
    head = t.split(':')[0] if ':' in t and len(t.split(':')[0].split()) <= 3 else t
    words = re.findall(r'[A-Za-z0-9]+', head)
    keep = [w for w in words if w.lower() not in STOP] or words
    out = ''.join(w if (w.isupper() or any(c.isdigit() for c in w)) else w[:1].upper() + w[1:] for w in keep[:n])
    return out[:48] or 'Untitled'
def surname(author):
    a = ascii(author or 'Anon').strip()
    parts = [p for p in re.split(r'\s+', a) if p]
    s = parts[-1] if parts else 'Anon'
    if s.lower() in ('jr', 'jr.', 'ii', 'iii') and len(parts) > 1: s = parts[-2]
    return re.sub(r'[^A-Za-z]', '', s)[:24] or 'Anon'
def paper_name(meta):
    y = (meta.get('published') or '0000')[:4]
    return f"{y}_{surname((meta.get('authors') or ['Anon'])[0])}_{short_title(meta.get('title', ''))}_en.pdf"
