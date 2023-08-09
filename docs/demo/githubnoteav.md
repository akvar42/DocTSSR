# mini site avec github et mkdocs

## Initialisation de Git

1. Initialiser le répertoire actuel avec Git:
 > git init

2. Configurer votre nom d'utilisateur et votre adresse e-mail pour Git :
  > git config user.name "mon prenom"
  > git config user.email "monemail@mail.com"

3. Vérifier le statut du répertoire :
  > git status

4. Ajouter un dossier pour le commit :
  > git add mondossier/

5. Créer un commit :
> git commit -m 'nomducommit'

6. Consulter l'historique des commits :
  > git log

### Publier sur GitHub

1. Créer un nouveau dépôt sur GitHub. Donner un nom + options appropriées.

2. Une fois le dépôt créé, liez-le à votre projet local :
   > git remote add origin "adresse du dépôt"
   > git push -u origin main

### Création du site avec MkDocs

Configuration de l'environnement

1. Installez python3-pip et python3-venv.

2. Créez un environnement virtuel :
   > python3 -m venv .venv

3. Pour éviter que Git suive le dossier .venv, créez un fichier .gitignore dans le dossier racine du projet avec le contenu suivant : 
4. >.venv/

   Ensuite, ajoutez et validez ce fichier :
  > git add .gitignore
  > git commit -m 'build: add .gitignore'

5. Activez l'environnement virtuel :
  > source .venv/bin/activate

### Installation et utilisation de MkDocs

1. Installez MkDocs :
   >pip install mkdocs

2. Créez un nouveau projet MkDocs dans le répertoire courant :
   > mkdocs new .

3. Lancer la documentation en local :
   > mkdocs serve

4. Modifier le fichier de configuration mkdocs.yml pour y indiquer le nom de votre site :
   > sitename: monsite

5. Ajouter modifications locales au dépôt :
   > git add .
   > git commit -m "Description du commit"
   > git push origin main

6. Déployer documentation sur GitHub Pages :
   > mkdocs gh-deploy

Pour trouver le site aller dans "Settings" -> "General" -> "Pages" pour consulter le lien vers votre documentation hébergée.
