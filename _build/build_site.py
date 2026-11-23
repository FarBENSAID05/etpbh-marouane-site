# -*- coding: utf-8 -*-
"""Génère le site statique ETPBH MAROUANE (fr à la racine, ar/ et en/).
Usage :  python build_site.py <dossier_sortie>
Le dossier de sortie est le dépôt Git déployé par Hostinger dans public_html."""
import sys, os, hashlib, html, datetime
from strings import T
from data import *

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public_html")
LANGS = ["fr", "ar", "en"]
TODAY = datetime.date.today().isoformat()
e = html.escape

def ver(path):
    p = os.path.join(OUT, path)
    return hashlib.md5(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "1"

ICONS = {
 "crane":'<path d="M4 21h10M7 21V8l11-5 2 3-13 6"/><path d="M18 6v6M16 12h4v3h-4z"/>',
 "dig":'<path d="M3 17h9l2-4h5l2 4v2H3z"/><path d="M14 13l-3-7-5 2 2 5"/><circle cx="7" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
 "mixer":'<rect x="2" y="9" width="6" height="7" rx="1"/><path d="M8 11l4-3 8 2-1 6-11 0"/><circle cx="6" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>',
 "truck":'<path d="M2 7h11v9H2zM13 10h4l4 3v3h-8z"/><circle cx="6" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/>',
 "road":'<path d="M8 3L4 21M16 3l4 18M12 4v3M12 10v3M12 16v4"/>',
 "shield":'<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "phone":'<path d="M5 3h4l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v4a2 2 0 01-2 2A16 16 0 013 5a2 2 0 012-2z"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin":'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0112 2.5a7 7 0 017 7C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "wa":'<path d="M4 20l1.3-4A8 8 0 1112 20a8 8 0 01-4-1.1z"/><path d="M9 9c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1c-1-.4-2-1.4-2.4-2.4l1-1-1-2z"/>',
 "menu":'<path d="M4 7h16M4 12h16M4 17h16"/>',
}
def icon(k, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'
WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 00-11.2 19.6L3 29l6.6-1.7A13 13 0 1016 3zm0 23.6a10.6 10.6 0 01-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1116 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 01-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 00-.9.4 3.6 3.6 0 00-1.1 2.7 6.3 6.3 0 001.3 3.3 14.4 14.4 0 005.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 002.2-1.5 2.7 2.7 0 00.2-1.5c-.1-.2-.3-.3-.6-.4z"/></svg>'

ROAD = '''<svg class="road" viewBox="0 0 1440 220" preserveAspectRatio="none" aria-hidden="true">
<path d="M-20 170 C 260 90, 520 120, 760 150 S 1180 210, 1460 110" stroke="#1B1C1B" stroke-width="70" fill="none"/>
<path d="M-20 170 C 260 90, 520 120, 760 150 S 1180 210, 1460 110" stroke="#F9AC08" stroke-width="4" stroke-dasharray="38 30" fill="none" opacity=".85"/></svg>'''

def depth(lang): return "" if lang == "fr" else "../"
def url(lang, page):  # page: "" or "materiel.html"
    return f"{DOMAIN}/{T[lang]['prefix']}{page}"

def head(lang, page, title, desc):
    t = T[lang]; d = depth(lang)
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{url(l,page)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{url("fr",page)}">'
    fonts = ("https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" if lang == "ar"
             else "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@500;600;700&display=swap")
    ld = {
      "@context":"https://schema.org","@type":"LocalBusiness","@id":DOMAIN+"/#org",
      "name":"EURL ETPBH MAROUANE","url":DOMAIN+"/","logo":DOMAIN+"/assets/img/logo-520.png",
      "image":DOMAIN+"/assets/img/og-etpbh.jpg","telephone":PHONE_INTL,"email":EMAIL,
      "address":{"@type":"PostalAddress","streetAddress":"Rue El Fath Ibn Khalfane N°45, Îlot N°32, RDC 04","addressLocality":"Hydra, Alger","postalCode":"16035","addressCountry":"DZ"},
      "areaServed":"DZ","description":t["desc_home"],
      "founder":{"@type":"Person","name":"LATELLI Madani"},
    }
    import json
    return f'''<!doctype html>
<html lang="{lang}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(lang,page)}">
{alts}
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(lang,page)}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-etpbh.jpg">
<meta property="og:locale" content="{t['og_locale']}">
<meta name="theme-color" content="#111111">
<link rel="icon" href="{d}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{d}assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="{d}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{d}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="{d}assets/css/site.css?v={ver('assets/css/site.css')}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>'''

def header(lang, page):
    t = T[lang]; d = depth(lang)
    home = "index.html" if page == "materiel.html" else ""
    links = []
    for href, label in t["nav"]:
        if href.startswith("#"):
            h = (f"{home or './'}{href}" if page == "materiel.html" else href)
            if page == "materiel.html": h = f"./{href}"
            links.append(f'<a href="{h}">{e(label)}</a>')
        else:
            cur = ' aria-current="page"' if page == href else ""
            links.append(f'<a href="{href}"{cur}>{e(label)}</a>')
    langs = []
    for l in LANGS:
        target = d + T[l]["prefix"] + (page or "")
        if not (page or "") and target == "": target = "./"
        if target.endswith("/") is False and page == "" : target = target or "./"
        cur = ' aria-current="true"' if l == lang else ""
        langs.append(f'<a href="{target or "./"}" hreflang="{l}" lang="{l}"{cur}>{l.upper()}</a>')
    return f'''<header class="hdr"><div class="wrap">
<a class="brand" href="./" aria-label="ETPBH MAROUANE — {e(t['home'])}"><picture><source srcset="{d}assets/img/logo-260.webp" type="image/webp"><img src="{d}assets/img/logo-260.png" width="260" height="144" alt="ETPBH MAROUANE"></picture></a>
<nav class="nav" id="nav" aria-label="Navigation">{''.join(links)}</nav>
<div class="langs">{''.join(langs)}</div>
<a class="btn btn-amber hide-m" href="https://wa.me/{WA}" target="_blank" rel="noopener">{e(t['cta'])}</a>
<button class="menu-btn" aria-controls="nav" aria-expanded="false" aria-label="{e(t['menu'])}">{icon('menu')}</button>
</div></header>'''

def footer(lang, page):
    t = T[lang]; d = depth(lang)
    nav = "".join(f'<li><a href="{("./" if page=="materiel.html" and h.startswith("#") else "")+h}">{e(l)}</a></li>' for h, l in t["nav"])
    return f'''<footer class="ftr"><div class="wrap">
<div class="cols">
<div><span class="logo-w"><img src="{d}assets/img/logo-260.png" width="260" height="144" alt="ETPBH MAROUANE"></span><p>{e(t['ft_about'])}</p></div>
<div><h3>{e(t['ft_links'])}</h3><ul>{nav}</ul></div>
<div><h3>{e(t['ft_contact'])}</h3><ul>
<li><a href="tel:{PHONE_INTL}" class="num">{PHONE}</a></li>
<li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
</div>
<div class="legal"><span>© {datetime.date.today().year} EURL ETPBH MAROUANE — {e(t['legal'])}</span><a href="https://profitpilot.dz" rel="noopener">{e(t['credit'])}</a></div>
</div></footer>
<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>
<script src="{d}assets/js/site.js?v={ver('assets/js/site.js')}" defer></script>
</body></html>'''

def maplink(q):
    import urllib.parse
    return "https://www.openstreetmap.org/search?query=" + urllib.parse.quote(q)

def home(lang):
    t = T[lang]
    stats = "".join(f'<li><b class="num">{v}</b><span>{e(l)}</span></li>' for v, l in t["stats"])
    svc = "".join(f'''<article class="card"><div class="ico">{icon(k)}</div><h3>{e(h)}</h3><p>{e(p)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in li)}</ul></article>''' for k, h, p, li in t["svc"])
    how = "".join(f'<div class="step"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["how"])
    refm = "".join(f'<div class="proj"><b>{e(n)}</b><span>{e(p)}</span></div>' for n, p in t["ref_main"])
    refn = "".join(f'<li><b>{e(n)}</b><span>{e(p)}</span></li>' for n, p in t["ref_nat"])
    badges = "".join(f'<span class="badge">{e(b)}</span>' for b in t["q_badges"])
    qmaps = ["Hydra, Alger, Algérie", "Saoula, Alger, Algérie"]
    qcards = "".join(f'<div class="card"><div class="ico">{icon("pin")}</div><h3>{e(h)}</h3><p>{e(p)}</p><a href="{maplink(m)}" target="_blank" rel="noopener">{e(t["map"])}</a></div>' for (h, p), m in zip(t["q_cards"], qmaps))
    fleet = "".join(f'<article class="card{" dark" if i==0 else ""}"><h3 class="num">{e(n)}</h3><p><b>{e(h)}</b></p><p>{e(p)}</p></article>' for i, (n, h, p) in enumerate(t["fleet_cards"]))
    f = t["f"]
    opts = "".join(f"<option>{e(o)}</option>" for o in t["f_opts"])
    data_attrs = f'data-title="{e(t["f_title"])}" ' + " ".join(f'data-l{k}="{e(v)}"' for k, v in [("nom",f["nom"]),("soc",f["societe"]),("tel",f["tel"]),("besoin",f["besoin"]),("lieu",f["lieu"]),("duree",f["duree"]),("details",f["details"])])
    body = f'''{header(lang,"")}
<main id="main">
<section class="hero"><div class="wrap">
<span class="tag">{e(t['tag'])}</span>
<h1>{t['h1']}</h1>
<p class="lead">{e(t['lead'])}</p>
<div class="ctas"><a class="btn btn-amber" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a><a class="btn btn-ghost" href="materiel.html">{e(t['see_fleet'])}</a></div>
</div>{ROAD}</section>
<div class="stats"><div class="wrap"><ul>{stats}</ul></div></div>

<section id="services"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['svc_k'])}</span><h2>{e(t['svc_h'])}</h2><p>{e(t['svc_p'])}</p></div>
<div class="grid g3">{svc}</div>
</div></section>

<section class="sec-alt" id="parc"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['fleet_k'])}</span><h2>{e(t['fleet_h'])}</h2><p>{e(t['fleet_p'])}</p></div>
<div class="grid g3">{fleet}</div>
<p style="margin-top:24px"><a class="btn btn-dark" href="materiel.html">{e(t['fleet_btn'])}</a></p>
</div></section>

<section id="methode"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['how_k'])}</span><h2>{e(t['how_h'])}</h2></div>
<div class="steps">{how}</div>
</div></section>

<section class="sec-alt" id="references"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['ref_k'])}</span><h2>{e(t['ref_h'])}</h2></div>
<div class="refs"><div class="ref-main"><h3>{e(t['ref_main_t'])}</h3>{refm}</div>
<div><h3>{e(t['ref_nat_t'])}</h3><ul class="ref-list">{refn}</ul></div></div>
</div></section>

<section id="qualification"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['q_k'])}</span><h2>{e(t['q_h'])}</h2><p>{e(t['q_p'])}</p><div class="badges">{badges}</div></div>
<div class="loc">{qcards}</div>
</div></section>

<section class="sec-alt" id="contact"><div class="wrap contact">
<div><span class="kicker">{e(t['c_k'])}</span><h2>{e(t['c_h'])}</h2><p>{e(t['c_p'])}</p>
<ul class="c-list">
<li>{icon('phone')}<div>{e(t['c_tel'])}<br><a href="tel:{PHONE_INTL}" class="num">{PHONE}</a></div></li>
<li>{icon('wa')}<div>{e(t['c_wa'])}<br><a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="num">{PHONE}</a></div></li>
<li>{icon('mail')}<div>{e(t['c_mail'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li>{icon('pin')}<div>{e(t['c_addr'])}<br>{e(t['q_cards'][0][1])}</div></li>
</ul><p><b>{e(t['c_contact'])}</b></p></div>
<form class="devis" novalidate {data_attrs}>
<div class="row"><div class="f"><label for="f-nom">{e(f['nom'])}</label><input id="f-nom" name="nom" required autocomplete="name"></div>
<div class="f"><label for="f-soc">{e(f['societe'])}</label><input id="f-soc" name="societe" autocomplete="organization"></div></div>
<div class="row"><div class="f"><label for="f-tel">{e(f['tel'])}</label><input id="f-tel" name="tel" type="tel" required autocomplete="tel" inputmode="tel"></div>
<div class="f"><label for="f-besoin">{e(f['besoin'])}</label><select id="f-besoin" name="besoin" required><option value="">{e(t['f_choose'])}</option>{opts}</select></div></div>
<div class="row"><div class="f"><label for="f-lieu">{e(f['lieu'])}</label><input id="f-lieu" name="lieu"></div>
<div class="f"><label for="f-duree">{e(f['duree'])}</label><input id="f-duree" name="duree"></div></div>
<div class="f"><label for="f-det">{e(f['details'])}</label><textarea id="f-det" name="details"></textarea></div>
<div class="acts"><button class="btn btn-amber" type="submit">{icon('wa')} {e(t['f_send'])}</button><button class="btn btn-dark" type="button" data-mail>{icon('mail')} {e(t['f_mail'])}</button></div>
<p class="note">{e(t['f_note'])}</p>
</form>
</div></section>
</main>
{footer(lang,"")}'''
    return head(lang, "", t["title_home"], t["desc_home"]) + "\n" + body

def materiel(lang):
    t = T[lang]; li = LANGS.index(lang)
    thA = t["th_A"]
    rowsA = []
    for n, (k, mk, md, ch, yr, st) in enumerate(PARC, 1):
        pill = f'<span class="pill">{e(t["st_ok"])}</span>' if st == "ok" else f'<span class="pill wait">{e(t["st_enc"])}</span>'
        cells = [str(n), D[k][li], mk, md, C[ch][li], str(yr)]
        tds = "".join(f'<td data-l="{e(thA[i])}"{" class=cat" if i==1 else ""}>{e(c) if i!=0 else c}</td>' for i, c in enumerate(cells))
        rowsA.append(f"<tr>{tds}<td data-l=\"{e(thA[6])}\">{pill}</td></tr>")
    thB = t["th_B"]
    rowsB = "".join(
        f'<tr><td data-l="{e(thB[0])}">{n}</td><td class="cat" data-l="{e(thB[1])}">{e(D[k][li])}</td><td data-l="{e(thB[2])}" class="num">{e(cap if lang!="ar" else cap.replace("t","طن"))}</td><td data-l="{e(thB[3])}">{q}</td><td data-l="{e(thB[4])}">{e(t["d48"] if dl=="48" else t["dplan"])}</td></tr>'
        for n, (k, cap, q, dl) in enumerate(MOBIL, 1))
    thC = t["th_C"]
    rowsC = "".join(f'<tr><td class="cat" data-l="{e(thC[0])}">{e(r[li])}</td><td data-l="{e(thC[1])}">{r[3]}</td></tr>' for r in ACQ)
    th = lambda hs: "".join(f'<th scope="col">{e(h)}</th>' for h in hs)
    body = f'''{header(lang,"materiel.html")}
<main id="main">
<section class="page-hero" style="padding:56px 0 48px"><div class="wrap"><span class="kicker" style="color:var(--amber)">{e(t['fleet_k'])}</span><h1>{e(t['mat_h1'])}</h1><p>{e(t['mat_lead'])}</p></div></section>
<section><div class="wrap">
<div class="fleet-sec"><div class="fleet-h"><div><h2>{e(t['A_h'])}</h2><p>{e(t['A_p'])}</p></div></div>
<table class="tbl"><thead><tr>{th(thA)}</tr></thead><tbody>{''.join(rowsA)}</tbody></table>
<p class="legend"><b>{e(t['total_A'])}</b></p></div>
<div class="fleet-sec"><div class="fleet-h"><div><h2>{e(t['B_h'])}</h2><p>{e(t['B_p'])}</p></div></div>
<table class="tbl"><thead><tr>{th(thB)}</tr></thead><tbody>{rowsB}</tbody></table>
<p class="legend"><b>{e(t['total_B'])}</b></p></div>
<div class="fleet-sec"><div class="fleet-h"><div><h2>{e(t['C_h'])}</h2><p>{e(t['C_p'])}</p></div></div>
<table class="tbl"><thead><tr>{th(thC)}</tr></thead><tbody>{rowsC}</tbody></table>
<p class="legend"><b>{e(t['total_C'])}</b></p></div>
<div class="card dark" style="display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap"><div><h3>{e(t['mat_cta_h'])}</h3><p style="margin:0">{e(t['mat_cta_p'])}</p></div><a class="btn btn-amber" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a></div>
</div></section>
</main>
{footer(lang,"materiel.html")}'''
    return head(lang, "materiel.html", t["title_mat"], t["desc_mat"]) + "\n" + body

def notfound():
    blocks = "".join(f'<div class="card" lang="{l}" dir="{T[l]["dir"]}"><h2>{e(T[l]["notfound_h"])}</h2><p>{e(T[l]["notfound_p"])}</p><a class="btn btn-dark" href="/{T[l]["prefix"]}">{e(T[l]["home"])}</a></div>' for l in LANGS)
    h = head("fr", "", "Page introuvable — ETPBH MAROUANE", T["fr"]["notfound_p"]).replace('href="favicon.ico"','href="/favicon.ico"').replace('href="assets/','href="/assets/').replace('href="site.webmanifest','href="/site.webmanifest')
    h = h.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
    return h + f'\n<main id="main"><section><div class="wrap"><p style="text-align:center;margin-bottom:24px"><a href="/"><img src="/assets/img/logo-260.png" width="200" alt="ETPBH MAROUANE" style="margin:auto"></a></p><div class="grid g3">{blocks}</div></div></section></main></body></html>'

def write(rel, content):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p) or OUT, exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

for l in LANGS:
    pre = T[l]["prefix"]
    write(pre + "index.html", home(l))
    write(pre + "materiel.html", materiel(l))
write("404.html", notfound())
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
urls = []
for page in ["", "materiel.html"]:
    for l in LANGS:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{url(a,page)}"/>' for a in LANGS)
        urls.append(f"<url><loc>{url(l,page)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
write("site.webmanifest", '{"name":"ETPBH MAROUANE","short_name":"ETPBH","start_url":"/","display":"standalone","background_color":"#ffffff","theme_color":"#111111","icons":[{"src":"/assets/img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/assets/img/icon-512.png","sizes":"512x512","type":"image/png"}]}\n')
write(".htaccess", """# ETPBH MAROUANE — Hostinger (derrière Cloudflare)
Options -Indexes
ErrorDocument 404 /404.html
RewriteEngine On
# www -> domaine nu
RewriteCond %{HTTP_HOST} ^www\\.etpbh-marouane\\.dz$ [NC]
RewriteRule ^(.*)$ https://etpbh-marouane.dz/$1 [R=301,L]
# HTTPS (Cloudflare envoie X-Forwarded-Proto)
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\\.(css|js|webp|png|jpg|ico|svg)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\\.html$">
    Header set Cache-Control "public, max-age=600"
  </FilesMatch>
</IfModule>
""")
print("OK ->", os.path.abspath(OUT))
