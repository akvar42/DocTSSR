## Planification d'une sauvegarde quotidienne et duplication des fichiers

### 1. Création du script de sauvegarde :

- On commence par créer un script pour réaliser la sauvegarde des données :
```
vim /root/script.sh
```
- Dans ce script, on insère les commandes suivantes :
```
#!/bin/bash
tar cf /root/HomeBack.tar /home
tar cf /root/ServicesBack.tar /services
```
- Ensuite, on modifie les permissions pour permettre l'exécution du script :
```
chmod u+x /root/script.sh
```

### 2. Planification de la sauvegarde :

- On planifie ensuite la sauvegarde à l'aide de `crontab` :
```
crontab -e
```
- Puis, on ajoute la ligne suivante pour exécuter le script tous les jours de la semaine à 12h30 :
```
30 12 * * 1-5 /root/script.sh
```

### 3. Duplication des fichiers avec `scp` :

- On vérifie si `scp` est installé sur le système :
```
apt-cache search scp
```
- Si nécessaire, on installe le paquet correspondant.
- Dans `crontab`, on ajoute une ligne pour copier les sauvegardes vers une machine distante :
```
32 12 * * 1-5 scp /root/*.tar utilisateur@adresse_ip_du_binôme:/dossier_de_destination/
```
> **Note**: Pensez à utiliser une clé SSH pour une authentification sans mot de passe avec `scp`.



Avec cette configuration, les données seront sauvegardées quotidiennement à 12h30 et dupliquées sur une autre machine à 12h32.
