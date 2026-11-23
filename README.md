# etpbh-marouane.dz

Site statique de l'EURL ETPBH MAROUANE — français à la racine, `ar/`, `en/`.

- `public_html/` : le site servi (Hostinger → Git → dossier racine `public_html`), derrière Cloudflare.
- `_build/` : générateur des pages (`strings.py` = textes, `data.py` = parc matériel, `build_site.py` = gabarits).

## Mettre à jour

    python _build/build_site.py
    git add -A
    git commit -m "Mise à jour du site"
    git push

Puis hPanel → Sites web → etpbh-marouane.dz → Avancé → Git → « Redéployer ».
