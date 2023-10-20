

## script création d'utilisateur


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

