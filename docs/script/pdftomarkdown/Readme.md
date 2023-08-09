readme de scriptpdftomarkdown.py Version 5
A vincent 03/08/2023  

# Description

Conversion de PDF en Markdown
Ce script permet de convertir des fichiers PDF en fichiers Markdown, y compris les images incluses dans les PDF. 
Il fonctionne sous Debian et d'autres systèmes Linux.



# Étapes d'installation 
(en root ou ajouter sudo)

### Installer Python
Assurez-vous que Python 3 est installé sur votre système. Vous pouvez l'installer en exécutant:


> apt update
> apt install python3



### Installer PIP (Gestionnaire de paquets Python)
Installez PIP pour faciliter l'installation des dépendances:


> apt install python3-pip




### Installer les Dépendances
Exécutez la commande suivante pour installer les dépendances requises:

> pip3 install PyPDF2 pdf2image tabulate mistune



### Installer Poppler (pour pdf2image)
La bibliothèque pdf2image nécessite Poppler pour fonctionner. Installez-le avec:


> apt install poppler-utils



# Utilisation du Script
Sauvegardé le script dans un emplacement accessible sur votre système.

Ouvrez un terminal et naviguez vers le répertoire où se trouve le script. 

Lancez-le avec:

> python3 scriptpdftomarkdown5.py

Spécifiez le chemin du dossier contenant les PDF: 
Le script vous demandera de spécifier le chemin du dossier où se trouvent les fichiers PDF à convertir. 
Vous pouvez spécifier un chemin absolu ou relatif.

Le script créera un dossier pour chaque fichier PDF et sauvegardera le fichier Markdown ainsi que les images associées dans ce dossier.

# Licence libre
Ce script est sans garantie.
si votre ordinateur explose et que vous vous blessiez gravement, si votre femme vous quitte, ou que le ciel vous tombe sur la tête:
Dans tout les cas: je ne suis pas responsable.