Installation :


Installer Python via le microsoft store (important)


Installer la bibliothèque PyMuPDF :
Ouvrez une invite de commande (CMD) en recherchant "cmd" dans la barre de recherche de Windows, puis exécutez la commande suivante pour installer la bibliothèque PyMuPDF :

Dans un terminal, entrez ce code :

pip install PyMuPDF

Préalablement, créez deux dossiers :
> un dossier pour les pdf à transformer
> un dossier pour les .md de sortie

Préparer les chemins des fichiers :

Ouvrez le fichier pdf_to_md_converter.py que vous venez d'enregistrer dans un éditeur de texte, et modifiez les variables pdf_input_path et md_output_path en remplaçant les chemins par les chemins réels de vos dossiers PDF d'entrée et du dossier Markdown de sortie.

Enregistrez les modifications. 

Exécuter le script :
Ouvrez une invite de commande (CMD) et naviguez jusqu'au répertoire où vous avez enregistré le fichier .py. Utilisez la commande cd pour vous déplacer dans le bon répertoire. Ensuite, exécutez le script en tapant :

python pdf_to_md_converter.py

Assurez-vous que vous êtes dans le même répertoire que le fichier .py lors de l'exécution de cette commande.

(ou clic droit > executer avec Python  ;) )

Vérifier le résultat :
Après avoir exécuté le script, vous devriez voir des messages dans la console indiquant que la conversion est terminée et que le(s) fichier(s) Markdown a/ont été créé(s). Vous trouverez le(s) fichier(s) Markdown converti(s) au chemin que vous avez spécifié dans la variable md_output_path.

C'est tout ! Vous avez maintenant installé et exécuté le script de conversion de PDF en Markdown.