# Guide Avancé sur les Informations Système sur GNU/Linux

Ce guide couvre diverses méthodes et outils pour obtenir des informations détaillées sur votre système Linux.

## 1. Architecture et OS

- **Obtenir des informations sur l'architecture du système** :
  ```
  uname -m
  ```

- **Afficher des informations détaillées sur le système d'exploitation** :
  ```
  uname -a
  ```

## 2. Disque Dur et Partitions

- **Lister les partitions et leur taille** :
  ```
  fdisk -l
  ```

- **Afficher l'espace utilisé et disponible pour chaque partition** :
  ```
  df -h
  ```

## 3. RAM et SWAP

- **Voir l'utilisation actuelle de la mémoire RAM et SWAP** :
  ```
  free -h
  ```

## 4. Processeur

- **Afficher des informations détaillées sur le CPU** :
  ```
  lscpu
  ```

## 5. Périphériques

- **Lister tous les périphériques connectés** :
  ```
  lspci
  ```

- **Afficher les périphériques USB connectés** :
  ```
  lsusb
  ```

## 6. Réseau

- **Afficher toutes les interfaces réseau actives** :
  ```
  ifconfig
  ```

- **Vérifier les connexions réseau actives** :
  ```
  netstat -tuln
  ```

## 7. Informations sur la Distribution

- **Vérifier la version de la distribution** (pour les distributions basées sur Debian) :
  ```
  lsb_release -a
  ```

## 8. Journaux Système

- **Afficher les dernières entrées du journal système** :
  ```
  dmesg | tail
  ```

- **Suivre le journal système en temps réel** :
  ```
  tail -f /var/log/syslog
  ```

## Conclusion

consulter les pages de manuel (`man <commande>`) pour chaque outil pour obtenir des détails et des options supplémentaires.

AV2023
