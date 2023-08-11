# Guide de Veille et Journalisation sur GNU/Linux

La capacité à surveiller et à journaliser l'activité d'un système est cruciale pour sa sécurité et sa maintenance. Dans ce guide, nous couvrirons les bases de la collecte d'informations sur le système et des techniques de veille et de journalisation.

## 1. Informations sur le système

### a. Mémoire et Charge Système
- Utilisez `free -h` pour afficher des informations sur la RAM et la mémoire SWAP.
- `top` ou `htop` (si installé) montrent la charge du système et les processus en cours.

### b. Informations sur le processeur
- `lscpu` affiche des détails sur le(s) processeur(s).

### c. Espace disque
- `df -h` montre l'espace disque utilisé et disponible pour tous les systèmes de fichiers montés.
  
## 2. Veille système

### a. Journaux système avec `journalctl`

- `journalctl` est l'outil principal pour interroger le journal système `systemd`.
- Pour afficher tous les journaux: `journalctl`
- Pour afficher les journaux pour une unité spécifique: `journalctl -u nom_du_service`

### b. Audit du système avec `auditd`

- `auditd` est le démon d'audit des utilisateurs et des processus. Il est essentiel pour surveiller l'accès aux fichiers et d'autres activités suspectes.
- Pour vérifier les journaux d'audit: `ausearch` et `aureport`.

### c. Logs de connexion et d'authentification
- Vérifiez `/var/log/auth.log` ou `/var/log/secure` pour les tentatives de connexion et les activités d'authentification.

## 3. Journalisation

### a. Configurer `rsyslog`

- La plupart des distributions Linux utilisent `rsyslog` pour la journalisation.
- Les configurations sont généralement trouvées dans `/etc/rsyslog.conf` et `/etc/rsyslog.d/`.

### b. Rotation des journaux avec `logrotate`

- La rotation des journaux est essentielle pour gérer l'espace disque et organiser les fichiers de journal.
- Les configurations sont dans `/etc/logrotate.conf` et `/etc/logrotate.d/`.

## 4. Surveillance en temps réel

### a. Utilisez `tail`

- `tail -f /chemin/vers/le/journal` permet de surveiller en temps réel les entrées d'un fichier journal.

### b. Outils de surveillance

- Considérez des outils comme `Nagios`, `Prometheus`, ou `Zabbix` pour une surveillance en temps réel du système et des services.

AV2023

---


