
## tous les scritps :


``` 
#!/bin/bash

# Vérifie si l' utilisateur existe
check_user_exist() {
    if id "$1" &>/dev/null; then
        echo "Compte utilisateur de $1 EXISTE"
    else
        echo "Compte utilisateur de $1 INEXISTANT"
    fi
}

# Menu  des utilisateur + création de dossier (diférencié préferable pour les utilisateur de gestion)
menu() {
    echo "GESTION DES UTILISATEURS : $1"
    echo "--------------------------"
    echo "C - Créer le compte utilisateur"
    echo "D - Créer un dossier personnel pour l'utilisateur"
    echo "M - Modifier le mot de passe de l'utilisateur"
    echo "S - Supprimer le compte utilisateur"
    echo "V - Vérifier si le compte utilisateur existe"
    echo "Q - quitter"
    read -p "Votre choix : " CHOIX

    case $CHOIX in
        C|c)
            sudo useradd $1 && echo "Utilisateur $1 créé avec succès!" || echo "Erreur lors de la création de l'utilisateur $1."
            ;;
        D|d)
            DIR="/home/$1"
            if [[ -d $DIR ]]; then
                echo "Le dossier personnel pour l'utilisateur $1 existe déjà."
            else
                sudo mkdir $DIR
                sudo chown $1:$1 $DIR
                echo "Dossier personnel pour l'utilisateur $1 créé avec succès!"
            fi
            ;;
        M|m)
            sudo passwd $1
            ;;
        S|s)
            sudo userdel -r $1 && echo "Utilisateur $1 supprimé avec succès!" || echo "Erreur lors de la suppression de l'utilisateur $1."
            ;;
        V|v)
            check_user_exist $1
            ;;
        Q|q)
            exit 0
            ;;
        *)
            echo "Choix invalide!"
            ;;
    esac
}

# Saisie de l'identifiant utilisateur
read -p "Saisir l'identifiant utilisateur souhaité : " USER_ID

# Affichage du menu
menu $USER_ID

```

```
#!/bin/bash

# Script: get-process.sh
# Description: Script pour afficher la liste des processus basée sur un critère de recherche

# Si plus d'un argument est fourni
if [[ $# -gt 1 ]]; then
    echo "Utilisation : $0 [nom_process]"
    exit 3
fi

# Si aucun argument n'est fourni
if [[ $# -eq 0 ]]; then
    echo -n "Veuillez saisir un critère de recherche de processus : "
    read CRITERE
    # Si la saisie est vide, on utilise l'identifiant utilisateur comme critère
    if [[ -z "$CRITERE" ]]; then
        CRITERE=$USER
    fi
else
    CRITERE=$1
fi

# Affichage des processus
echo "-------------------------------------------------"
echo "Liste des processus contenant $CRITERE"
echo "-------------------------------------------------"
ps aux | grep -v "grep" | grep "$CRITERE" 

echo "-------------------------------------------------"
echo "$(date +"%H:%M:%S") - Fin de traitement"


```


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

```
#!/bin/bash

LOG_FILE="/var/log/createusers_fails.log"
SUCCESS_COUNT=0
FAIL_COUNT=0

# Fonction pour créer un utilisateur (utilisation de useradd plutôt que adduser car + de compatibilité )
create_user() {
    local USER_NAME="$1"
    echo "Creation du compte : $USER_NAME"
    sudo useradd "$USER_NAME"
    if [[ $? -eq 0 ]]; then
        echo "Creation de l'utilisateur : $USER_NAME OK"
        ((SUCCESS_COUNT++))
    else
        echo "ECHEC de creation de l'utilisateur : $USER_NAME"
        echo "$USER_NAME" >> "$LOG_FILE"
        ((FAIL_COUNT++))
    fi
}

# Corp principal du script
main() {
    if [[ -f "$LOG_FILE" ]]; then
        > "$LOG_FILE"
    fi

    read -p "Base de nom des comptes a créer : " BASE_NAME
    read -p "Nombre d'utilisateurs a créer :" COUNT
    read -p "Numero du premier utilisateur (défaut: 1) : " START_NUM
    START_NUM=${START_NUM:-1}

    for ((i=0; i<COUNT; i++)); do
        USER_NAME="${BASE_NAME}$(($START_NUM + $i))"
        create_user "$USER_NAME"
    done

    echo "----------------------------------------------"
    echo "$SUCCESS_COUNT utilisateurs ont été créés avec succès"
    echo "$FAIL_COUNT utilisateur(s) n'a/ont pas été créé(s)"
    echo "Les échecs de création ont été reportés dans : $LOG_FILE"
    echo "----------------------------------------------"
}

main


```

```
#!/bin/bash

LOG_FILE="/var/log/createusers_fails.log"
SUCCESS_COUNT=0
FAIL_COUNT=0
LIST_FILE="/tmp/listusers.txt"

# Fonction pour créer un utilisateur
create_user() {
    local USER_NAME="$1"
    echo "Création du compte : $USER_NAME"
    sudo useradd "$USER_NAME"
    if [[ $? -eq 0 ]]; then
        echo "Création de l'utilisateur : $USER_NAME OK"
        ((SUCCESS_COUNT++))
    else
        echo "ECHEC de création de l'utilisateur : $USER_NAME"
        echo "$USER_NAME" >> "$LOG_FILE"
        ((FAIL_COUNT++))
    fi
}

# Point d'entrée principal du script
main() {
    if [[ -f "$LOG_FILE" ]]; then
        > "$LOG_FILE"
    fi

    if [[ -f "$LIST_FILE" ]]; then
        echo "Utilisation de $LIST_FILE pour créer les utilisateurs"
        for USER_NAME in $(cat "$LIST_FILE"); do
            create_user "$USER_NAME"
        done
    else
        read -p "Base de nom des comptes à créer : " BASE_NAME
        read -p "Nombre d'utilisateurs à créer :" COUNT
        read -p "Numero du premier utilisateur (défaut: 1) : " START_NUM
        START_NUM=${START_NUM:-1}

        for ((i=0; i<COUNT; i++)); do
            USER_NAME="${BASE_NAME}$(($START_NUM + $i))"
            create_user "$USER_NAME"
        done
    fi

    echo "----------------------------------------------"
    echo "$SUCCESS_COUNT utilisateurs ont été créés avec succès"
    echo "$FAIL_COUNT utilisateur(s) n'a/ont pas été créé(s)"
    echo "Les échecs de création ont été reportés dans : $LOG_FILE"
    echo "----------------------------------------------"
    
    # Mise à jour de la liste pour ne contenir que les utilisateurs non créés
    if [[ -f "$LIST_FILE" ]]; then
        mv "$LIST_FILE" "${LIST_FILE}.bak"
        cp "$LOG_FILE" "$LIST_FILE"
    fi
}

main


```


```
#!/bin/bash

LOG_FILE="/var/log/createusers_fails.log"
SUCCESS_COUNT=0
FAIL_COUNT=0
LIST_FILE="/tmp/listusersmaj.txt"

# Fonction pour créer un utilisateur avec des V positionel
create_detailed_user() {
    local USER_NAME="$1"
    local USER_DIR="$2"
    local USER_SHELL="$3"

    # Vérifiez si le shell est valide ou non
    if [[ -z "$USER_SHELL" ]] || ! [[ -f "$USER_SHELL" ]]; then
        USER_SHELL="/bin/bash"
    fi

    echo "Création du compte : $USER_NAME avec le répertoire $USER_DIR et le shell $USER_SHELL"
    sudo useradd -m -d "$USER_DIR" -s "$USER_SHELL" "$USER_NAME"
    
    if [[ $? -eq 0 ]]; then
        echo "Création de l'utilisateur : $USER_NAME OK"
        ((SUCCESS_COUNT++))
    else
        echo "ECHEC de création de l'utilisateur : $USER_NAME"
        echo "$USER_NAME" >> "$LOG_FILE"
        ((FAIL_COUNT++))
    fi
}

# Menu du script
main() {
    if [[ -f "$LOG_FILE" ]]; then
        > "$LOG_FILE"
    fi

    if [[ -f "$LIST_FILE" ]]; then
        echo "Utilisation de $LIST_FILE pour créer les utilisateurs"
        
        while IFS=' ' read -r USER_NAME USER_DIR USER_SHELL; do
            create_detailed_user "$USER_NAME" "$USER_DIR" "$USER_SHELL"
        done < "$LIST_FILE"

    else
        echo "Fichier $LIST_FILE introuvable. Fin du script."
        exit 1
    fi

    echo "----------------------------------------------"
    echo "$SUCCESS_COUNT utilisateurs ont été créés avec succès"
    echo "$FAIL_COUNT utilisateur(s) n'a/ont pas été créé(s)"
    echo "Les échecs de création ont été reportés dans : $LOG_FILE"
    echo "----------------------------------------------"
}

main


```