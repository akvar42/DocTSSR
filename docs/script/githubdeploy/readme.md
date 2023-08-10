# Read me
#  petit script shell pour automatisé le deployement de MKdocs



## Mise en place et utilisation

### 1. Installation dans le dossier local Git


```
cd nom_du_dossier-local-Git-a-deployer
vi deploy.sh #coller le script et sauvegardé (:wq)
```

### 2. Création du fichier \`.gitignore\`

Pour éviter que le script soit suivis par Git crée le fichier \`.gitignore\` :

```
vi .gitignore
```

Ajoutez  deploy.sh pour ignorer notre script \`deploy.sh\` :

```
deploy.sh
```

Ensuite, ajoutez et validez ce fichier :
```
git add .gitignore
git commit -m 'build: add .gitignore'
```

### 3. Lancer le script

Après avoir rendu le script exécutable (avec \`chmod +x deploy.sh\`), lancez-le en utilisant:

```
./deploy.sh
```

le script vous demandera le nom du commit et le mdp.
c'est tout.

## Licence

Akvar42 libre

