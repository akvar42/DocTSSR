# Petit guide de Scripting en Bash

## Table des matières
- [Petit guide de Scripting en Bash](#petit-guide-de-scripting-en-bash)
  - [Table des matières](#table-des-matières)
  - [Introduction](#introduction)
  - [Syntaxe de base](#syntaxe-de-base)
  - [Variables](#variables)
  - [Conditions](#conditions)
    - [if, elif, else](#if-elif-else)
    - [case](#case)
  - [Boucles](#boucles)
    - [For](#for)
    - [While](#while)
  - [Fonctions](#fonctions)
  - [Lire des entrées](#lire-des-entrées)
  - [Références](#références)

## Introduction
Le Bash (Bourne-Again SHell) est un shell Unix utilisé pour interagir avec le système d'exploitation. Il est également utilisé pour le scripting.

## Syntaxe de base
Le script commence souvent avec le shebang `#!` suivi du chemin vers le shell. Pour bash, il s'agirait de `#!/bin/bash`.

```bash
#!/bin/bash
echo "Bonjour, monde !"
```

## Variables
Les variables sont utilisées pour stocker des données qui peuvent être utilisées plus tard dans le script.

```bash
nom="Jean"
echo "Bonjour, $nom"
```

## Conditions

### if, elif, else
La structure `if` est utilisée pour exécuter du code basé sur des conditions.

```bash
nombre=10
if [ $nombre -eq 10 ]; then
  echo "Le nombre est 10."
elif [ $nombre -gt 10 ]; then
  echo "Le nombre est supérieur à 10."
else
  echo "Le nombre est inférieur à 10."
fi
```

### case
La structure `case` permet de comparer une variable à plusieurs valeurs.

```bash
choix="a"
case $choix in
  a) echo "Vous avez choisi A." ;;
  b) echo "Vous avez choisi B." ;;
  *) echo "Choix non valide." ;;
esac
```

## Boucles

### For
La boucle `for` est utilisée pour répéter des commandes.

```bash
for i in {1..5}; do
  echo "Ceci est l'itération numéro $i"
done
```

### While
La boucle `while` est utilisée pour exécuter une série de commandes tant qu'une condition est vraie.

```bash
compteur=1
while [ $compteur -le 5 ]; do
  echo "Compteur: $compteur"
  ((compteur++))
done
```

## Fonctions
Les fonctions permettent de regrouper des commandes et de les réutiliser.

```bash
function saluer {
  echo "Bonjour, $1"
}
saluer "Jean"
```

## Lire des entrées
La commande `read` est utilisée pour lire une ligne depuis l'entrée standard.

```bash
echo "Quel est votre nom ?"
read nom
echo "Bonjour, $nom"
```

## Références
- [Guide avancé de Bash](https://tldp.org/LDP/abs/html/)
- [Manuel de Bash](https://www.gnu.org/software/bash/manual/bash.html)
