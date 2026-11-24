# etpbh-marouane.dz

Site statique de l'EURL ETPBH MAROUANE — français à la racine, `ar/`, `en/`.

- `public_html/` : le site servi (Hostinger → Git → dossier racine `public_html`), derrière Cloudflare.
- `_build/` : générateur des pages (`strings.py` = textes, `contenu.py` = textes v2 prioritaires : ce que l'entreprise peut fournir sans nombre d'engins, grands projets, vision ; `data.py` = parc matériel interne, jamais affiché en nombre ; `build_site.py` = gabarits).

## Mettre à jour

    python _build/build_site.py
    git add -A
    git commit -m "Mise à jour du site"
    git push

Hostinger déploie la branche `main` (hPanel → Sites web → etpbh-marouane.dz → Avancé → Git).
Le fichier `.htaccess` à la racine du dépôt sert le contenu de public_html/ sans changer l'URL et
bloque _build/ et README.md. Après le push, Hostinger redéploie ; sinon cliquer « Redéployer ».
