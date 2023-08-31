## Monter le partage « Support_Info » depuis Debian

### 1. Prérequis sur mon poste Windows 10

- **Activer le support du protocole SMB/CIFS** :
  - Je vais dans les "Fonctionnalités Windows" et je m'assure que la fonctionnalité "Support du partage de fichiers SMB 1.0/CIFS" est activée.
  - Note :  le protocole SMB1 est obsolète et peut présenter des risques de sécurité.

- **Configurer le partage "Support_Info"** :
  - Je m'assure que le partage "Support_Info" est accessible et n'est pas caché (le nom ne doit pas se terminer par un $).

### 2. Configuration sur Debian

- **Installer les outils nécessaires** :
  ```bash
  apt install cifs-utils
  ```

- **Créer le répertoire de montage** :
  ```bash
  mkdir /home/loxton/support_info
  ```

- **Attribuer les droits nécessaires sur le répertoire** :
  ```bash
  chown loxton:informatique /home/loxton/support_info
  chmod 770 /home/loxton/support_info
  ```

- **Configurer le montage automatique** :
  - J'édite le fichier `/etc/fstab` pour ajouter la ligne suivante :
    ```bash
    //172.16.63.253/support_info /home/loxton/support_info cifs username=loxton,password=TLP4$$VV0rI),file_mode=0777,dir_mode=0777 0 0
    ```

- **Monter le partage** :
  ```bash
  mount -a
  ```

> **Astuce** : Pour des raisons de sécurité, il vaut mieux que je ne stocke pas de mots de passe en clair dans `/etc/fstab`. Je devrais envisager d'utiliser des options de montage sécurisées ou des fichiers de credentials séparés.
