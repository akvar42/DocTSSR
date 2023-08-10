```
#!/bin/bash

# Construire le site MkDocs
mkdocs build

# Ajouter toutes les modifications à git
git add .

# Commiter les modifications
read -p "Entrez le message de commit : " commitMessage
git commit -m "$commitMessage"

# Pousser vers la branche principale (ou master) !!! ATENTION modifier instruction si deployement sur MAIN
git push origin master

# Déployer sur GitHub Pages
mkdocs gh-deploy
```
