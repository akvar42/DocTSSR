## script sauvegarde de fichier variable de fonction exterieur au fichier (dans fonction.fonc)



```
#!/bin/bash

# Inclure les fonctions du fichier fonctions.fonc
source fonctions.fonc

# Menu pour le script
menu() {
    echo "-----------------------------------"
    echo "1 - Sauvegarder les fichiers .sh"
    echo "2 - Supprimer les fichiers .save"
    echo "3 - Lister les fichiers"
    echo "4 - Quitter"
    echo "-----------------------------------"
    read -p "Votre choix : " choice

    case $choice in
        1)
            backup_files
            ;;
        2)
            delete_backup
            ;;
        3)
            list_files
            ;;
        4)
            echo "Au revoir!"
            exit 0
            ;;
        *)
            echo "Choix non valide"
            ;;
    esac
}

# Boucle pour afficher le menu
while true; do
    menu
done



```

