# etpbh-marouane.dz

Site statique de l'EURL ETPBH MAROUANE — français à la racine, `ar/`, `en/`.

- `public_html/` : le site servi (Hostinger → Git → dossier racine `public_html`), derrière Cloudflare.
- `_build/` : générateur des pages (`strings.py` = textes, `contenu.py` = textes v2 prioritaires : ce que l'entreprise peut fournir sans nombre d'engins, grands projets, vision ; `data.py` = parc matériel interne, jamais affiché en nombre ; `build_site.py` = gabarits).

## Mettre à jour

    python _build/build_site.py
    git add -A
    git commit -m "Mise à jour du site"
    git push

git subtree push --prefix public_html origin deploy

La branche `deploy` ne contient que le contenu de public_html/ : c'est elle que Hostinger publie
(hPanel → Sites web → etpbh-marouane.dz → Avancé → Git, branche `deploy`). La branche `main` garde
les sources (_build/) et n'est pas publiée. Hostinger redéploie tout seul après le push ; sinon
cliquer « Redéployer » dans hPanel.
