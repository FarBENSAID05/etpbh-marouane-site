import re,glob,json,os,html
root='.'
probs=[]
for f in sorted(glob.glob('**/*.html',recursive=True)):
    if f.endswith('404.html') or f.startswith('README'): continue
    s=open(f,encoding='utf-8').read()
    t=html.unescape(re.search(r'<title>(.*?)</title>',s).group(1)); d=html.unescape(re.search(r'name="description" content="(.*?)"',s).group(1))
    if len(t)>70: probs.append(f'{f}: title {len(t)} car. «{t}»')
    if not 110<=len(d)<=165: probs.append(f'{f}: description {len(d)} car.')
    nh1=len(re.findall(r'<h1[\s>]',s))
    if nh1!=1: probs.append(f'{f}: h1 x{nh1}')
    if 'rel="canonical"' not in s: probs.append(f'{f}: canonical')
    if len(re.findall(r'hreflang="(fr|ar|en|x-default)"',s))<4: probs.append(f'{f}: hreflang')
    for m in re.findall(r'<img(?![^>]*\balt=)[^>]*>',s): probs.append(f'{f}: img sans alt')
    for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(j)
        except Exception as e: probs.append(f'{f}: JSON-LD {e}')
    if '.html"' in s.replace('404.html',''):
        probs.append(f'{f}: lien .html restant: '+','.join(set(re.findall(r'"[^"]*\.html[^"]*"',s)))[:120])
    base=os.path.dirname(f)
    for h in re.findall(r'href="([^"#?]*)(?:#[^"]*)?"',s):
        if not h or h.startswith(('http','mailto','tel','//','data:')): continue
        p=os.path.normpath(os.path.join(base,h))
        if h.endswith('/') or h in ('./','../'): cand=[os.path.join(p,'index.html')]
        else: cand=[p,p+'.html',os.path.join(p,'index.html')]
        if not any(os.path.exists(c) for c in cand): probs.append(f'{f}: lien cassé {h}')
    if 'lang="ar"' in s[:200]:
        body=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S)
        for m in re.finditer(r'\d{1,3}(?: \d{3})+',re.sub(r'<[^>]+>',' ',body)):
            ctx=body[max(0,body.find(m.group(0))-20):body.find(m.group(0))]
            if '213' in m.group(0) or 'tel' in ctx or '0661' in m.group(0): continue
            probs.append(f'{f}: milliers avec espace «{m.group(0)}»')
print('\n'.join(sorted(set(probs))) or 'AUCUN PROBLÈME')
