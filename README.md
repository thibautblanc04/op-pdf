# OP PDF

Ouvrir, annoter et organiser des PDF au stylet, gratuitement. L'app s'exécute entièrement dans le navigateur : les PDF restent sur l'ordinateur et ne sont jamais envoyés en ligne.

**Ouvrir l'app :** https://thibautblanc04.github.io/op-pdf/

Pour l'installer, ouvrez ce lien dans Edge ou Chrome, puis cliquez sur « Installer » dans la barre d'adresse. Elle marche ensuite hors ligne et apparaît dans « Ouvrir avec… » pour les PDF.

## Fichiers

- `src/app.html` : le code de l'app.
- `build.py` : génère `index.html` et change la version du cache hors ligne. À lancer avec `python3 build.py` après chaque modification.
- `manifest.webmanifest`, `sw.js`, les icônes : ce qui rend l'app installable et utilisable hors ligne.
