## Utilisation du script de traitement de fichiers Markdown

Ce script utilise l'API OpenAI pour traiter des fichiers Markdown, en extrayant des données pertinentes du texte et en les mettant en page au format Markdown.

### Prérequis:

1. Python 3
2. Le module `openai`. Pour l'installer, utilisez la commande:
    ```
    pip install openai
    ```

3. Une clé API OpenAI. Une fois obtenue, remplacez `VOTRE_CLÉ_API` dans le script par votre clé personnelle.

### Comment utiliser le script:

1. Assurez-vous que tous les prérequis sont satisfaits.

2. Exécutez le script. Lors de l'exécution, il vous sera demandé :
    - Le chemin du dossier source contenant les fichiers `.md`.
    - Le chemin du dossier de destination où vous souhaitez sauvegarder les fichiers traités.

   Exemple :
   ```
   Entrez le chemin du dossier source contenant les fichiers .md : /chemin/vers/dossier/source
   Entrez le chemin du dossier de destination pour les fichiers traités : /chemin/vers/dossier/destination
   ```

3. Le script parcourra tous les fichiers `.md` dans le dossier source (et ses sous-dossiers) et sauvegardera les fichiers traités dans le dossier de destination.

### Caractéristiques:

- Le script conserve la structure des sous-dossiers du dossier source dans le dossier de destination.
- Les fichiers traités sont préfixés par "traité_" pour distinguer les fichiers originaux des fichiers traités.

### Recommandations:

- Avant d'exécuter le script sur un grand nombre de fichiers, testez-le d'abord sur un petit ensemble de données pour vous assurer qu'il fonctionne comme prévu.
- Gardez à l'esprit que l'API OpenAI est une ressource payante. Assurez-vous de comprendre les coûts associés avant d'exécuter le script sur un grand nombre de fichiers.
