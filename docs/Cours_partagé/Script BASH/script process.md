## Description: Script pour afficher la liste des processus basée sur un critère de recherche


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


