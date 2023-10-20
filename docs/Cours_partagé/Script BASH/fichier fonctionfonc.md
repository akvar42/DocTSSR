## # contenue su fichier fonctions.fonc pour sauvegarder les fichiers .sh

```

#!/bin/bash

# contenue su fichier fonctions.fonc pour sauvegarder les fichiers .sh

backup_files() {
    for file in *.sh; do
        if [[ -f "$file" ]]; then
            cp "$file" "${file}.save"
        fi
    done
    echo "Sauvegarde terminée."
}

# Fonction pour supprimer les fichiers .save
delete_backup() {
    rm *.save 2>/dev/null
    echo "Tous les fichiers .save ont été supprimés."
}

# Fonction pour lister les fichiers
list_files() {
    for file in *; do
        if [[ "$file" == *.sh ]]; then
            if [[ -f "${file}.save" ]]; then
                echo -e "\e[32m$file\e[0m"
            else
                echo -e "\e[31m$file\e[0m"
            fi
        fi
    done
}

```

