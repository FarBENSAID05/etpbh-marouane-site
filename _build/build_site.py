# -*- coding: utf-8 -*-
"""Génère le site statique ETPBH MAROUANE (fr à la racine, ar/ et en/).
Usage :  python build_site.py <dossier_sortie>
Le dossier de sortie est le dépôt Git déployé par Hostinger dans public_html."""
import sys, os, hashlib, html, datetime
from strings import T, MEDIA, GALLERY, SVC_IMG, PHOTO_CREDITS
from families import F, FAM_KEYS, FAM_ORDER, FAM_ICON, FAM_GAL, FAM_ACQ
from data import *
from contenu import appliquer, CAT, FAM_FIG
appliquer(T, F)

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public_html")
LANGS = ["fr", "ar", "en"]
TODAY = datetime.date.today().isoformat()
e = html.escape

def ver(path):
    p = os.path.join(OUT, path)
    return hashlib.md5(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "1"

ICONS = {
 "rail": '<path d="M7 3h10a2 2 0 0 1 2 2v9a3 3 0 0 1-3 3H8a3 3 0 0 1-3-3V5a2 2 0 0 1 2-2Z"/><path d="M5 10h14"/><path d="M12 3v7"/><circle cx="8.5" cy="13.5" r="1"/><circle cx="15.5" cy="13.5" r="1"/><path d="m8 17-3 4"/><path d="m16 17 3 4"/>',
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
def statval(v):
    """Chiffre + unité : seul le chiffre est isolé en LTR, l'unité suit le sens de la page."""
    import re as _r
    m = _r.match(r'^(.*?)\s*(<small>.*</small>)$', v)
    return f'<span class="num">{m.group(1)}</span> {m.group(2)}' if m else f'<span class="num">{v}</span>'

def icon(k, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'
WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 00-11.2 19.6L3 29l6.6-1.7A13 13 0 1016 3zm0 23.6a10.6 10.6 0 01-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1116 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 01-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 00-.9.4 3.6 3.6 0 00-1.1 2.7 6.3 6.3 0 001.3 3.3 14.4 14.4 0 005.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 002.2-1.5 2.7 2.7 0 00.2-1.5c-.1-.2-.3-.3-.6-.4z"/></svg>'

ROAD = '''<svg class="road" viewBox="0 0 1440 220" preserveAspectRatio="none" aria-hidden="true">
<path d="M-20 170 C 260 90, 520 120, 760 150 S 1180 210, 1460 110" stroke="#1B1C1B" stroke-width="70" fill="none"/>
<path d="M-20 170 C 260 90, 520 120, 760 150 S 1180 210, 1460 110" stroke="#F9AC08" stroke-width="4" stroke-dasharray="38 30" fill="none" opacity=".85"/></svg>'''

def depth(lang): return "" if lang == "fr" else "../"
def url(lang, page):  # page: "" ou "materiel.html" -> URL publiée SANS extension (convention profitpilot.dz)
    return f"{DOMAIN}/{T[lang]['prefix']}{page[:-5] if page.endswith('.html') else page}"

THEME_JS = '<script>(function(){try{var s=localStorage.getItem("etp_theme");var t=(s==="light"||s==="dark")?s:(window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");document.documentElement.setAttribute("data-theme",t);}catch(e){document.documentElement.setAttribute("data-theme","light");}})();</script>'

def head(lang, page, title, desc, extra_ld=None):
    t = T[lang]; d = depth(lang)
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{url(l,page)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{url("fr",page)}">'
    fonts = (["thmanyahsans-Regular", "thmanyahserifdisplay-Black"] if lang == "ar" else ["dm-sans-latin-400-normal", "playfair-display-latin-900-normal"])
    preload = "\n".join(f'<link rel="preload" href="{d}assets/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>' for f in fonts)
    ld = {
      "@context":"https://schema.org","@type":"LocalBusiness","@id":DOMAIN+"/#org",
      "name":"EURL ETPBH MAROUANE","url":DOMAIN+"/","logo":DOMAIN+"/assets/img/logo-520.png",
      "image":DOMAIN+"/assets/img/og-etpbh.jpg","telephone":PHONE_INTL,"email":EMAIL,
      "address":{"@type":"PostalAddress","streetAddress":"Rue El Fath Ibn Khalfane N°45, Îlot N°32, RDC 04","addressLocality":"Hydra, Alger","postalCode":"16035","addressCountry":"DZ"},
      "areaServed":"DZ","description":t["desc_home"],
      "founder":{"@type":"Person","name":"LATELLI Madani"},
    }
    import json
    more = list(extra_ld or [])
    if page:
        more.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":t["home"],"item":url(lang,"")},
            {"@type":"ListItem","position":2,"name":title.split(" — ")[0],"item":url(lang,page)}]})
    ld_more = "".join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in more)
    return f'''<!doctype html>
<html lang="{lang}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{THEME_JS}
<meta name="color-scheme" content="light dark">
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
{preload}
<link rel="stylesheet" href="{d}assets/css/site.css?v={ver('assets/css/site.css')}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>{ld_more}
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>'''

LANG_NAME = {"fr":"Français","ar":"العربية","en":"English"}
UI = {"fr":{"lang":"Changer de langue","theme":"Basculer entre le mode sombre et le mode clair"},
      "ar":{"lang":"تغيير اللغة","theme":"التبديل بين الوضع الليلي والوضع النهاري"},
      "en":{"lang":"Change language","theme":"Switch between dark and light mode"}}

def header(lang, page):
    t = T[lang]; d = depth(lang)
    f = F[lang]
    pre = "" if page == "" else "./"
    def cur(x): return ' aria-current="page"' if page == x else ""
    fam_links = "".join(f'<a href="{k}.html"{cur(k+".html")}>{e(f["fam"][k]["short"])}</a>' for k in FAM_ORDER)
    links = [f'<div class="dd"><button class="dd-b" type="button" aria-haspopup="true">{e(f["menu"])} <span aria-hidden="true">▾</span></button><div class="dd-m">{fam_links}<a href="materiel.html"{cur("materiel.html")}>{e(f["all"])}</a></div></div>',
             f'<a href="{pre}#services">{e(t["nav"][0][1])}</a>',
             f'<a href="{pre}#references">{e(t["nav"][2][1])}</a>',
             f'<a href="qualification.html"{cur("qualification.html")}>{e(f["qualif_nav"])}</a>',
             f'<a href="{pre}#contact">{e(t["nav"][4][1])}</a>']
    langs = []
    for l in LANGS:
        target = d + T[l]["prefix"] + (page or "")
        if not (page or "") and target == "": target = "./"
        if target.endswith("/") is False and page == "" : target = target or "./"
        if l == lang:
            langs.append(f'<span class="lang-btn active" aria-current="page" lang="{l}"><span class="lang-code">{l.upper()}</span><span class="lang-name">{LANG_NAME[l]}</span></span>')
        else:
            langs.append(f'<a class="lang-btn" href="{target or "./"}" hreflang="{l}" lang="{l}" rel="alternate"><span class="lang-code">{l.upper()}</span><span class="lang-name">{LANG_NAME[l]}</span></a>')
    return f'''<header class="hdr"><div class="wrap">
<a class="brand" href="./" aria-label="ETPBH MAROUANE — {e(t['home'])}"><picture><source srcset="{d}assets/img/logo-260.webp" type="image/webp"><img src="{d}assets/img/logo-260.png" width="260" height="144" alt="ETPBH MAROUANE"></picture></a>
<nav class="nav" id="nav" aria-label="Navigation">{''.join(links)}</nav>
<div class="nav-lang"><div class="lang-drop"><button type="button" class="lang-drop-btn" aria-haspopup="true" aria-expanded="false" aria-label="{UI[lang]['lang']}" title="{UI[lang]['lang']}"><span>{lang.upper()}</span><svg class="lang-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></button><div class="lang-drop-menu">{''.join(langs)}</div></div>
<button type="button" class="theme-btn" aria-pressed="false" aria-label="{UI[lang]['theme']}" title="{UI[lang]['theme']}"><svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg><svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2m-7.07-17.07 1.41 1.41m11.32 11.32 1.41 1.41M2 12h2m16 0h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg></button></div>
<a class="btn btn-amber hide-m" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['cta'])}</a>
<button class="menu-btn" aria-controls="nav" aria-expanded="false" aria-label="{e(t['menu'])}">{icon('menu')}</button>
</div></header>'''

def footer(lang, page):
    t = T[lang]; d = depth(lang)
    f = F[lang]
    nav = "".join(f'<li><a href="{k}.html">{e(f["fam"][k]["t"])}</a></li>' for k in FAM_ORDER)
    nav += f'<li><a href="materiel.html">{e(f["all"])}</a></li><li><a href="qualification.html">{e(f["qualif_nav"])}</a></li>'
    nav += f'<li><a href="{"" if page=="" else "./"}#contact">{e(t["nav"][4][1])}</a></li>'
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

CARD_LINK = {"crane":"levage.html","dig":"terrassement.html","mixer":"beton.html","truck":"transport.html","road":"qualification.html","shield":"materiel.html"}

def maplink(q):
    import urllib.parse
    return "https://www.openstreetmap.org/search?query=" + urllib.parse.quote(q)

def home(lang):
    t = T[lang]; m = MEDIA[lang]; d = depth(lang)
    stats = "".join(f'<li><b>{statval(v)}</b><span>{e(l)}</span></li>' for v, l in t["stats"])
    svc = "".join(f'''<article class="card has-img"><img class="card-img" src="{d}assets/media/{img}.webp" width="800" height="500" alt="" loading="lazy" decoding="async"><div class="ico">{icon(k)}</div><h3>{e(h)}</h3><p>{e(p)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in li)}</ul><a class="card-link" href="{CARD_LINK[k]}">{e(F[lang]["see"] if k not in ("road",) else F[lang]["qualif_nav"])} {"←" if lang=="ar" else "→"}</a></article>''' for (k, h, p, li), img in zip(t["svc"], SVC_IMG))
    how = "".join(f'<div class="step"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["how"])
    refm = "".join(f'<div class="proj"><b>{e(n)}</b><span>{e(p)}</span></div>' for n, p in t["ref_main"])
    refn = "".join(f'<li><b>{e(n)}</b><span>{e(p)}</span></li>' for n, p in t["ref_nat"])
    badges = "".join(f'<span class="badge">{e(b)}</span>' for b in t["q_badges"])
    qmaps = ["Hydra, Alger, Algérie", "Saoula, Alger, Algérie"]
    qcards = "".join(f'<div class="card"><div class="ico">{icon("pin")}</div><h3>{e(h)}</h3><p>{e(p)}</p><a href="{maplink(m)}" target="_blank" rel="noopener">{e(t["map"])}</a></div>' for (h, p), m in zip(t["q_cards"], qmaps))
    v2 = t["v2"]
    pj = "".join(f'<article class="card pj"><div class="ico">{icon(ic)}</div><h3>{e(h)}</h3><p>{e(p)}</p></article>' for ic, h, p in v2["pj"])
    vip = "".join(f"<p>{e(x)}</p>" for x in v2["vi_p"])
    vig = "".join(f"<li>{e(x)}</li>" for x in v2["vi_goals"])
    fleet = "".join(f'<article class="card{" dark" if i==0 else ""}"><h3>{e(n)}</h3><p><b>{e(h)}</b></p><p>{e(p)}</p></article>' for i, (n, h, p) in enumerate(t["fleet_cards"]))
    f = t["f"]
    opts = "".join(f"<option>{e(o)}</option>" for o in t["f_opts"])
    data_attrs = f'data-title="{e(t["f_title"])}" ' + " ".join(f'data-l{k}="{e(v)}"' for k, v in [("nom",f["nom"]),("soc",f["societe"]),("tel",f["tel"]),("besoin",f["besoin"]),("lieu",f["lieu"]),("duree",f["duree"]),("details",f["details"])])
    gal = "".join(f'<figure class="gal-it"><img src="{d}assets/media/{g}.webp" width="1200" height="750" alt="{e(m["caps"][g])}" loading="lazy" decoding="async"><figcaption>{e(m["caps"][g])}</figcaption></figure>' for g in GALLERY)
    creds = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{e(n)}</a> · {e(a)} · ' + (f'<a href="{lu}" rel="noopener" target="_blank">{e(l)}</a>' if lu else e(l)) + '</li>' for n, u, a, l, lu in PHOTO_CREDITS)
    body = f'''{header(lang,"")}
<main id="main">
<section class="hero"><video class="hero-vid" autoplay muted loop playsinline preload="metadata" poster="{d}assets/media/hero-poster.jpg" aria-label="{e(MEDIA[lang]['video_alt'])}"><source src="{d}assets/media/hero-480.mp4" type="video/mp4" media="(max-width: 700px)"><source src="{d}assets/media/hero-720.mp4" type="video/mp4" media="(max-width: 1280px)"><source src="{d}assets/media/hero-1080.mp4" type="video/mp4"></video><div class="wrap">
<span class="tag">{e(t['tag'])}</span>
<h1>{t['h1']}</h1>
<p class="lead">{e(t['lead'])}</p>
<div class="ctas"><a class="btn btn-amber" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['cta'])}</a><a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a><a class="btn btn-ghost" href="materiel.html">{e(t['see_fleet'])}</a></div>
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

<section class="sec-alt" id="projets"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(v2['pj_k'])}</span><h2>{e(v2['pj_h'])}</h2><p>{e(v2['pj_p'])}</p></div>
<div class="grid g3">{pj}</div>
</div></section>

<section id="vision"><div class="wrap vision">
<div><span class="kicker">{e(v2['vi_k'])}</span><h2>{e(v2['vi_h'])}</h2>{vip}</div>
<div class="card dark"><h3>{e(v2['vi_goals_h'])}</h3><ul class="chk">{vig}</ul></div>
</div></section>

<section class="sec-alt" id="references"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['ref_k'])}</span><h2>{e(t['ref_h'])}</h2></div>
<div class="refs"><div class="ref-main"><h3>{e(t['ref_main_t'])}</h3>{refm}</div>
<div><h3>{e(t['ref_nat_t'])}</h3><ul class="ref-list">{refn}</ul></div></div>
</div></section>

<section id="terrain"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(m['gal_k'])}</span><h2>{e(m['gal_h'])}</h2><p>{e(m['gal_p'])}</p></div>
<div class="gal">{gal}</div>
<p class="gal-note">{e(m['note'])}</p>
<details class="credits"><summary>{e(m['credits'])}</summary><ul>{creds}</ul></details>
</div></section>

<section class="sec-alt" id="qualification"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(t['q_k'])}</span><h2>{e(t['q_h'])}</h2><p>{e(t['q_p'])}</p><div class="badges">{badges}</div></div>
<div class="loc">{qcards}</div>
</div></section>

<section id="contact"><div class="wrap contact">
<div><span class="kicker">{e(t['c_k'])}</span><h2>{e(t['c_h'])}</h2><p>{e(t['c_p'])}</p>
<ul class="c-list">
<li>{icon('phone')}<div>{e(t['c_tel'])}<br><a href="tel:{PHONE_INTL}" class="num">{PHONE}</a></div></li>
<li>{icon('wa')}<div>{e(t['c_wa'])}<br><a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="num">{PHONE}</a></div></li>
<li>{icon('mail')}<div>{e(t['c_mail'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
<li>{icon('pin')}<div>{e(t['c_addr'])}<br>{e(t['q_cards'][0][1])}</div></li>
</ul><p><b>{e(t['c_contact'])}</b></p></div>
<div class="devis devis-tally">
<iframe src="https://tally.so/embed/{TALLY[lang]}?alignLeft=1&amp;hideTitle=1&amp;transparentBackground=1&amp;dynamicHeight=1" loading="lazy" width="100%" height="760" frameborder="0" marginheight="0" marginwidth="0" title="{e(t['f_title'])}"></iframe>
<noscript><p><a class="btn btn-amber" href="{tally(lang)}">{e(t['cta'])}</a></p></noscript>
<div class="acts"><a class="btn btn-dark" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a><a class="btn btn-ghost-d" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['f_open'])}</a></div>
</div>
<script async src="https://tally.so/widgets/embed.js"></script>
</div></section>
</main>
{footer(lang,"")}'''
    return head(lang, "", t["title_home"], t["desc_home"]) + "\n" + body

def materiel(lang):
    t = T[lang]; li = LANGS.index(lang); v2 = t["v2"]; f = F[lang]
    th = v2["th_cat"]
    secs = []
    for fam in FAM_ORDER:
        rows = []
        for it in CAT[fam]:
            cap = it[3 + li] or "—"; mk = it[6] or "—"
            mob = v2["mob_mix"] if it[7] == "mix" else v2["mob_48"]
            rows.append(f'<tr><td class="cat" data-l="{e(th[0])}">{e(it[li])}</td><td data-l="{e(th[1])}">{e(cap)}</td><td data-l="{e(th[2])}">{e(mk)}</td><td data-l="{e(th[3])}">{e(mob)}</td></tr>')
        head_ = "".join(f'<th scope="col">{e(h)}</th>' for h in th)
        secs.append(f'<div class="fleet-sec"><div class="fleet-h"><h2>{icon(FAM_ICON[fam], "fam-ico")} {e(f["fam"][fam]["t"])}</h2><a class="card-link" href="{fam}.html">{e(f["see"])} {"←" if lang=="ar" else "→"}</a></div>'
                    f'<table class="tbl"><thead><tr>{head_}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
    body = f'''{header(lang,"materiel.html")}
<main id="main">
<section class="page-hero has-bg" style="padding:56px 0 48px;background-image:linear-gradient(90deg,rgba(23,24,23,.92),rgba(23,24,23,.65)),url({depth(lang)}assets/media/mat-banner.webp)"><div class="wrap"><span class="kicker" style="color:var(--amber)">{e(t['fleet_k'])}</span><h1>{e(t['mat_h1'])}</h1><p>{e(t['mat_lead'])}</p></div></section>
<section><div class="wrap">
{"".join(secs)}
<p class="legend">{e(v2['mat_note'])}</p>
<div class="card dark cta-row" style="margin-top:28px"><div><h3>{e(t['mat_cta_h'])}</h3><p style="margin:0">{e(t['mat_cta_p'])}</p></div><div class="ctas"><a class="btn btn-amber" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['cta'])}</a><a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a></div></div>
</div></section>
</main>
{footer(lang,"materiel.html")}'''
    return head(lang, "materiel.html", t["title_mat"], t["desc_mat"]) + "\n" + body


def fam_page(lang, k):
    t = T[lang]; f = F[lang]; fm = f["fam"][k]; li = LANGS.index(lang); d = depth(lang); page = k + ".html"
    v2 = t["v2"]
    fig = FAM_FIG[k]
    stats = f'<li><b>{statval(fig[0])}</b><span>{e(fig[1 + li])}</span></li>'
    stats += f'<li><b>{statval(t["stats"][1][0])}</b><span>{e(t["stats"][1][1])}</span></li>'
    stats += f'<li><b>{statval(t["stats"][2][0])}</b><span>{e(t["stats"][2][1])}</span></li>'
    cards = ""
    for it in CAT[k]:
        cap = it[3 + li]; mk = it[6]
        mob = v2["mob_mix"] if it[7] == "mix" else v2["mob_48"]
        meta = " · ".join(x for x in (cap, mk) if x)
        cards += f'<div class="unit"><span class="u-n">{icon(FAM_ICON[k])}</span><div><b>{e(it[li])}</b><span class="u-m">{e(meta) if meta else ""}</span><span class="pill">{e(mob)}</span></div></div>'
    gal = "".join(f'<figure class="pg-it"><img src="{d}assets/media/parc/{g}.webp" width="1000" height="650" alt="" loading="lazy" decoding="async"></figure>' for g in FAM_GAL[k])
    uses = "".join(f"<li>{e(x)}</li>" for x in fm["uses"])
    terms = "".join(f"<li>{e(x)}</li>" for x in f["terms"])
    import urllib.parse
    wa = "https://wa.me/" + WA + "?text=" + urllib.parse.quote(f["wa"] + fm["t"])
    faqs = fm["faq"] + f["faq_common"]
    faq_html = "".join(f'<details class="faq"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in faqs]}
    others = "".join(f'<a class="fam-chip" href="{o}.html">{icon(FAM_ICON[o])}{e(f["fam"][o]["short"])}</a>' for o in FAM_ORDER if o != k)
    body = f'''{header(lang,page)}
<main id="main">
<section class="fam-hero" style="background-image:linear-gradient(90deg,rgba(20,21,20,.9),rgba(20,21,20,.45)),url({d}assets/media/parc/{k}-hero.webp)"><div class="wrap">
<span class="kicker" style="color:var(--amber)">{e(f["menu"])}</span>
<h1>{e(fm["t"])}</h1><p class="lead">{e(fm["lead"])}</p>
<div class="ctas"><a class="btn btn-amber" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['cta'])}</a><a class="btn btn-ghost" href="{wa}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a><a class="btn btn-ghost" href="#detail">{e(f["list_h"])}</a></div>
</div></section>
<div class="stats"><div class="wrap"><ul class="s3">{stats}</ul></div></div>
<section><div class="wrap"><div class="pg pg-{len(FAM_GAL[k])}">{gal}</div><p class="gal-note">{e(f["photo_note"])}</p></div></section>
<section class="sec-alt" id="detail"><div class="wrap">
<div class="sec-head"><span class="kicker">{e(f["list_h"])}</span><h2>{e(fm["t"])}</h2></div>
<h3 class="u-h">{e(v2["prov_h"])}</h3><div class="units">{cards}</div>
<p class="legend">{e(v2["mat_note"])}</p>
</div></section>
<section><div class="wrap grid g2">
<div class="card"><h3>{e(f["uses_h"])}</h3><ul class="chk">{uses}</ul></div>
<div class="card"><h3>{e(f["terms_h"])}</h3><ul class="chk">{terms}</ul></div>
</div></section>
<section class="sec-alt"><div class="wrap">
<div class="sec-head"><h2>{e(f["faq_h"])}</h2></div><div class="faqs">{faq_html}</div>
<div class="card dark cta-row"><div><h3>{e(f["cta_h"])}</h3><p style="margin:0">{e(f["cta_p"])}</p></div><div class="ctas"><a class="btn btn-amber" href="{tally(lang)}" target="_blank" rel="noopener">{e(t['cta'])}</a><a class="btn btn-ghost" href="{wa}" target="_blank" rel="noopener">{icon('wa')} {e(t['cta_wa'])}</a></div></div>
<div class="fam-other">{others}<a class="fam-chip" href="materiel.html">{e(f["all"])}</a></div>
</div></section>
</main>
{footer(lang,page)}'''
    return head(lang, page, fm["title"], fm["desc"], [faq_ld]) + "\n" + body

def qualif_page(lang):
    t = T[lang]; q = F[lang]["q"]; d = depth(lang); page = "qualification.html"
    acts = "".join(f'<div class="q-act"><span class="q-code">{c}</span><b>{e(n)}</b><span>{e(r)}</span></div>' for c, n, r in q["acts"])
    why = "".join(f"<li>{e(x)}</li>" for x in q["why"])
    docs = "".join(f"<li>{e(x)}</li>" for x in q["docs"])
    import urllib.parse
    wa = "https://wa.me/" + WA + "?text=" + urllib.parse.quote(q["cta"] + " — ETPBH MAROUANE")
    body = f'''{header(lang,page)}
<main id="main">
<section class="fam-hero" style="background-image:linear-gradient(90deg,rgba(20,21,20,.92),rgba(20,21,20,.5)),url({d}assets/media/parc/qualif-hero.webp)"><div class="wrap">
<div class="q-badge"><span>{"الصنف" if lang=="ar" else ("Class" if lang=="en" else "Catégorie")}</span><b>IV</b></div>
<h1>{e(q["h1"])}</h1><p class="lead">{e(q["lead"])}</p>
<div class="ctas"><a class="btn btn-amber" href="{wa}" target="_blank" rel="noopener">{icon('wa')} {e(q["cta"])}</a></div>
</div></section>
<section><div class="wrap">
<div class="sec-head"><h2>{e(q["acts_h"])}</h2></div>
<div class="q-acts">{acts}</div>
</div></section>
<section class="sec-alt"><div class="wrap grid g2">
<div class="card"><h3>{e(q["why_h"])}</h3><ul class="chk">{why}</ul></div>
<div class="card"><h3>{e(q["docs_h"])}</h3><ul class="chk">{docs}</ul><p style="margin-top:14px"><a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">{e(q["cta"])}</a></p></div>
</div></section>
</main>
{footer(lang,page)}'''
    return head(lang, page, q["title"], q["desc"]) + "\n" + body

def notfound():
    blocks = "".join(f'<div class="card" lang="{l}" dir="{T[l]["dir"]}"><h2>{e(T[l]["notfound_h"])}</h2><p>{e(T[l]["notfound_p"])}</p><a class="btn btn-dark" href="/{T[l]["prefix"]}">{e(T[l]["home"])}</a></div>' for l in LANGS)
    h = head("fr", "", "Page introuvable — ETPBH MAROUANE", T["fr"]["notfound_p"]).replace('href="favicon.ico"','href="/favicon.ico"').replace('href="assets/','href="/assets/').replace('href="site.webmanifest','href="/site.webmanifest')
    h = h.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
    return h + f'\n<main id="main"><section><div class="wrap"><p style="text-align:center;margin-bottom:24px"><a href="/"><img src="/assets/img/logo-260.png" width="200" alt="ETPBH MAROUANE" style="margin:auto"></a></p><div class="grid g3">{blocks}</div></div></section></main></body></html>'

import re as _re
_LINK = _re.compile(r'((?:href|content)=")((?:https://etpbh-marouane\.dz/)?(?:\.\./|\./)?(?:[a-z]{2}/)?)([a-z0-9-]+)\.html((?:#[^"]*)?")')
def sans_ext(m):
    name = m.group(3)
    if name == "index": return m.group(1) + (m.group(2) or "./") + m.group(4)
    if name == "404": return m.group(0)
    return m.group(1) + m.group(2) + name + m.group(4)
def write(rel, content):
    if rel.endswith(".html") and not rel.endswith("404.html"):
        content = _LINK.sub(sans_ext, content)
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p) or OUT, exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

for l in LANGS:
    pre = T[l]["prefix"]
    write(pre + "index.html", home(l))
    write(pre + "materiel.html", materiel(l))
    for k in FAM_ORDER: write(pre + k + ".html", fam_page(l, k))
    write(pre + "qualification.html", qualif_page(l))
write("404.html", notfound())
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
urls = []
for page in ["", "materiel.html", "qualification.html"] + [k + ".html" for k in FAM_ORDER]:
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
# Aucune URL ne finit par index.html ni par .html (convention profitpilot.dz)
RewriteCond %{THE_REQUEST} \\s/+([^\\s?]*/)?index\\.html(?:\\?[^\\s]*)?\\s [NC]
RewriteRule ^ /%1 [R=301,L,NE]
RewriteCond %{THE_REQUEST} \\s/+([^\\s?]+)\\.html(?:\\?[^\\s]*)?\\s [NC]
RewriteCond %1 !(^|/)(index|404)$
RewriteRule ^ /%1 [R=301,L,NE]
# Sert /x en lisant x.html (réécriture interne)
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L]
AddType font/woff2 .woff2
AddType video/mp4 .mp4
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\\.(css|js|woff2|ico)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\\.(webp|png|jpg|svg|mp4)$">
    Header set Cache-Control "public, max-age=604800"
  </FilesMatch>
  <FilesMatch "\\.html$">
    Header set Cache-Control "public, max-age=600"
  </FilesMatch>
</IfModule>
""")
print("OK ->", os.path.abspath(OUT))
