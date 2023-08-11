# Guide d'Utilisation de Crontab sur GNU/Linux

`Crontab` est un outil utilisé pour planifier des tâches (communément appelées "cron jobs") sur votre système Unix/Linux. Ces tâches peuvent être planifiées pour s'exécuter à des intervalles réguliers.

## 1. Bases de Crontab

### a. Afficher la Crontab

- Pour afficher la crontab actuelle de l'utilisateur : 
  ```
  crontab -l
  ```

### b. Éditer la Crontab

- Pour éditer la crontab de l'utilisateur actuel : 
  ```
  crontab -e
  ```

## 2. Syntaxe des Tâches Planifiées

Une entrée typique de crontab a le format suivant : 

```
* * * * * /chemin/vers/la/commande
```

Chaque champ est représenté par une étoile ou une valeur :

1. Minute (0 - 59)
2. Heure (0 - 23)
3. Jour du mois (1 - 31)
4. Mois (1 - 12)
5. Jour de la semaine (0 - 7) où 0 et 7 représentent tous deux le dimanche.

## 3. Exemples d'Utilisation

### a. Exécution d'un script tous les jours à minuit

```
0 0 * * * /chemin/vers/le/script.sh
```

### b. Exécution d'une commande tous les lundis à 7h30

```
30 7 * * 1 /chemin/vers/la/commande
```

### c. Exécution d'une tâche toutes les heures

```
0 * * * * /chemin/vers/la/tâche
```

## 4. Astuces Supplémentaires

### a. Redirection de la sortie vers un fichier

Si vous souhaitez enregistrer la sortie de votre tâche planifiée, vous pouvez rediriger la sortie vers un fichier :

```
0 0 * * * /chemin/vers/le/script.sh > /chemin/vers/fichier.log
```

### b. Supprimer une Crontab

Pour supprimer la crontab de l'utilisateur actuel :

```
crontab -r
```

AV2023

