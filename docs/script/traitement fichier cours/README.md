# Readme

# Traitement de Texte avec OpenAI

Ce script Python permet de traiter du contenu texte à partir de fichiers Markdown (.md) en utilisant l'API OpenAI. Il découpe les textes en morceaux, formule la demande à OpenAI pour chaque morceau, puis assemble le résultat final.

## Prérequis

- Python 3.x
- Bibliothèque openai (à installer via pip install openai)

## Configuration

Avant d'exécuter le script, remplacez 'VOTRE_CLÉ_API' par votre clé API OpenAI.

## Utilisation

!!! avant de l'executer modifier le prompt selon votre besoin dans la valeur prompt=f du script!!!

1. Exécutez le script.
2. Lorsque vous y êtes invité, entrez le chemin du dossier source contenant les fichiers .md que vous souhaitez traiter.
3. Ensuite, entrez le chemin du dossier de destination où vous souhaitez que les fichiers traités soient enregistrés.

Les fichiers traités seront enregistrés dans le dossier de destination avec le préfixe traité_ ajouté à leur nom.

## Note

Ce script conserve la structure des sous-dossiers du dossier source lors de l'enregistrement des fichiers dans le dossier de destination.

Akvar42 2023 version 2 libre
