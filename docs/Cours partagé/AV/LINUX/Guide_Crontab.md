# Guide Avancé pour l'Utilisation de `crontab` sous Linux

Le système `cron` est un planificateur de tâches qui permet aux utilisateurs de Linux d'exécuter des commandes ou des scripts à des moments prédéfinis ou à des intervalles réguliers.

## 1. Syntaxe de base

Le format d'une entrée `crontab` est le suivant :
```
* * * * * /chemin/vers/la/commande arguments
```
Chaque champ est détaillé ci-dessous :
- Minute (0 - 59)
- Heure (0 - 23)
- Jour du mois (1 - 31)
- Mois (1 - 12)
- Jour de la semaine (0 - 7) (0 et 7 sont tous les deux pour dimanche)

## 2. Exemples d'utilisation

- **Exécuter un script tous les jours à 2h30 du matin** :
```
30 2 * * * /chemin/vers/le/script.sh
```

- **Exécuter une tâche toutes les 5 minutes** :
```
*/5 * * * * /chemin/vers/la/commande
```

## 3. Commandes utiles

- **Éditer le fichier crontab pour l'utilisateur actuel** :
```
crontab -e
```

- **Afficher le contenu du crontab pour l'utilisateur actuel** :
```
crontab -l
```

- **Supprimer le crontab de l'utilisateur actuel** :
```
crontab -r
```

## 4. Gestion des logs avec `logrotate`

Lorsque vos scripts ou tâches génèrent des logs, ceux-ci peuvent rapidement consommer tout l'espace disque disponible. `logrotate` est un utilitaire pour simplifier l'administration des logs. 

### a. Configuration

`logrotate` utilise un fichier de configuration pour définir la manière dont les logs doivent être tournés.

Exemple de fichier de configuration :
```
/chemin/vers/les/logs/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 user group
    postrotate
        /chemin/vers/un/script/après/rotation
    endscript
}
```

Explication des directives :
- `daily` : Faire tourner les logs chaque jour.
- `rotate 7` : Conserver 7 archives des logs.
- `compress` : Compresser les logs.
- `delaycompress` : Compresser le log une fois que la prochaine rotation est terminée.
- `missingok` : Ne pas émettre d'erreur si un log est manquant.
- `notifempty` : Ne pas faire tourner le log s'il est vide.
- `create` : Créer un nouveau fichier log avec les permissions spécifiées.
- `postrotate`/`endscript` : Exécuter le script spécifié après avoir fait tourner les logs.

### b. Exécution

Bien que `logrotate` puisse être exécuté manuellement, il est généralement exécuté via `cron`. Une tâche typique pourrait ressembler à :

```
0 0 * * * /usr/sbin/logrotate /etc/logrotate.conf
```

Cette commande exécuterait `logrotate` chaque jour à minuit en utilisant la configuration spécifiée dans `/etc/logrotate.conf`.

### ressource
https://crontab.guru/
Éditeur rapide et simple pour les expressions de planification cron - by Cronitor


