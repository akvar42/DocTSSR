# Résumé VIM

## Les modes

### Mode commande

- Effectuer des actions (copier, supprimer, enregistrer, ...)
- On peut pas écrire dans ce mode
- On revient en mode commande via ma touche `Esc`

### Mode insertion

- Utilisé pour écrire du contenu

Plusieurs touches pour passer dans ce mode:

- `i` : on **i**nsère avant le curseur
- `a` : on **a**joute après le curseur
- `I` : on **i**nsère en **début** de ligne
- `A` : on **a**joute en **fin** de ligne
- `o` : on crée une nouvelle ligne **en dessous**
- `O` : on crée une nouvelle ligne **au dessus**

### Mode visuel

- Permet de sélectionner du contenu, pour y apporter des modification ou effectuer certaines actions

Plusieurs touches :

- `v` : permet de sélectionner des lignes entières
- `Ctrl+v` : permet de sélectionner du contenu en mode bloc

## Les commandes

### De base

- `:e nom_du_fichier` : ouvrir un fichier existant, ou préparer un nouveau fichier
- `:q` : ferme le fichier, si pas de modifications. En cas de modifications non sauvegardées, utiliser `:q!` pour forcer la fermeture
- `:w` : sauvegarder les modifications. `:w nom_du_fichier` pour sauvegarder sous un nouveau nom
- `:wq` : sauvegarder et quitter, change forcément la date de dernière modif
- `:x` : sauvegarder si nécessaire et quitter, ne change la date de dernière modif qu'en cas de modification de contenu
- `:shell` : on ouvre un shell, sans fermer Vim, puis on retourne dans l'édition du fichier une fois tapé `Ctrl+d` ou `exit`
- `:terminal` : on ouvre un shell sous le contenu ouvert

    - on peut basculer du shell au contenu avec `Ctrl+ww`
    - on ferme le terminal avec `Ctrl+d` ou `exit` (en ayant le focus dedans)

- `:vs nom_du_fichier` : split verticalement et ouvre le fichier à droite
- `:sp` : split horizontalement et ouvre le fichier

    - on peut basculer du shell au contenu avec `Ctrl+ww`

- `set nu`: affiche les numéros de lignes

### De navigation

- `:numero_de_ligne` : se positionne sur la ligne souhaitée
- `/terme` : se positionne sur la prochaine occurence de *terme*

    - `n` : se positionner à la prochaine occurence
    - `N` : se positionner à l'occurence précédente

- `G` : se positionne sur la dernière ligne
- `gg` ou `:1` : se positionne sur la première ligne
- `$` : se positionne en fin de ligne
- `^^` : se positionne en début de ligne
- `w`: se positionne sur le mot suivant
- `10w`: se positionne sur au 10ème mot après le curseur
- `b`: se positionne sur le mot précédent
- `10b`: se positionne sur au 10ème mot précédent le curseur

### De manipulation de texte

- `dd` : supprime la ligne sous le curseur (`d` en mode visuel) et place le contenu en mémoire
- `10dd` : supprime les 10 lignes à partir de la ligne courrante et place le contenu en mémoire
- `yy` : copie la ligne sous le curseur (`d` en mode visuel) et place le contenu en mémoire
- `10yy` : copie les 10 lignes à partir de la ligne courrante et place le contenu en mémoire
- `p` : colle le contenu en mémoire (sous le curseur)
- `P` : colle le contenu en mémoire (au dessus du curseur)
- `cw` : supprimer le mot, place le contenu en mémoire et passe en mode insertion
- `20cw` : supprimer les 20 prochains mots, place le contenu en mémoire et passe en mode insertion
- `x` supprime le caractère sous le curseur
- `3x` supprime les 3 prochains caractères sous le curseur
- `d$` supprime tout ce qui suit le curseur, jusqu'à la fin de ligne
- `d^^` supprime tout ce qui précède le curseur, jusqu'à la fin de ligne
- `:s/foo/bar/` : **s**ubstitution de **la prochaine occurence** de *foo* par *bar* sur la ligne courrante
- `:s/foo/bar/g` : **s**ubstitution de toutes les occurences de *foo* par *bar* sur la ligne courrante
- `:.,.+10s/foo/bar/g` : **s**ubstitution de toutes les occurences de *foo* par *bar* sur les 10 prochaines lignes, dont la ligne courrante
- `:10,20s/foo/bar/g` : **s**ubstitution de toutes les occurences de *foo* par *bar* présentes entre les lignes 10 et 20
- `:%s/foo/bar/g` : **s**ubstitution de toutes les occurences de *foo* par *bar* présentes **dans le fichier entier** (%)
