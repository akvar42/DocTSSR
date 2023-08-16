## Montage permanent de la partition « LOGS » dans le dossier « /var/log » sur Debian

### 1. Redémarrage en mode maintenance:
Je commence par redémarrer en mode maintenance pour m'assurer qu'aucun processus n'utilise le dossier `/var/log` pendant le déplacement. 
```bash
init 1
```

### 2. Création d'un dossier temporaire et copie des logs:
Une fois en mode maintenance, je crée un dossier temporaire pour stocker les logs existants et je copie le contenu de `/var/log` dans ce dossier tout en conservant les permissions.
```bash
mkdir /tmp/logs
cp -rp /var/log/* /tmp/logs/
```

### 3. Modification du fichier `/etc/fstab`:
Je modifie ensuite le fichier `/etc/fstab` pour y ajouter la partition « LOGS ». Cela permettra de monter cette partition automatiquement au démarrage.
```bash
echo "LABEL=LOGS /var/log xfs defaults 0 0" >> /etc/fstab
```
Je vérifie ensuite que le montage se fait correctement avec la commande :
```bash
mount -a
```

### 4. Recopie des logs dans la nouvelle partition:
Je copie maintenant les logs du dossier temporaire vers la nouvelle partition.
```bash
cp -rp /tmp/logs/* /var/log/
```

### 5. Vérification du contenu:
Je vérifie que le contenu des deux dossiers est identique pour m'assurer que tout a été copié correctement.
```bash
ls -al /var/log/
ls -al /tmp/logs/
```

### 6. Redémarrage de la machine:
Je redémarre la machine pour que les changements prennent effet.
```bash
reboot
```

### 7. Vérification des nouvelles inscriptions dans les journaux:
Après le redémarrage, je m'assure que de nouvelles données ont été inscrites dans les journaux pendant ou après le démarrage du système.
```bash
tail /var/log/syslog
```

## Conclusion:
J'ai maintenant déplacé avec succès le dossier `/var/log` vers la partition « LOGS » tout en conservant l'intégrité des logs. Cette partition sera montée automatiquement à chaque démarrage, permettant de soulager la partition initialement utilisée pour stocker les logs.
