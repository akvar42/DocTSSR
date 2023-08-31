## Mise à jour du répertoire `/home`

### Préparation

1. **Sauvegarde** : 
   - On s'assure d'avoir une sauvegarde complète de toutes les données, en particulier du répertoire `/home`.

2. **Information des utilisateurs**:
   - On informe tous les utilisateurs qu'une maintenance est prévue. On précise la durée estimée de cette maintenance.

3. **Désactivation de l'accès des utilisateurs**:
   - Pour empêcher les connexions pendant la transition, on passe en mode de maintenance:
   ```
   systemctl isolate rescue.target
   ```
   - Si le système est accessible via SSH, on désactive le service:
   ```
   systemctl stop sshd
   ```
   - On crée un fichier `/etc/nologin` pour empêcher les utilisateurs non-root de se connecter:
   ```
   echo "Maintenance en cours, veuillez réessayer plus tard." > /etc/nologin
   ```

### Processus de transition

1. **Copie temporaire de `/home`** :
   ```
   cp -rp /home /tmp/home-backup
   ```

2. **Modification du fichier `/etc/fstab`** :
   ```
   vim /etc/fstab
   ```
   - On commente la ligne concernant `/home` en ajoutant un `#` devant :
   ```
   #UUID=4b59933b-136a-4287-8658-c97b2ec93603 /home ext4 defaults 0 2
   ```
   - On ajoute ensuite la ligne pour monter la partition `PROFILS` à `/home` :
   ```
   LABEL=PROFILS /home ext4 defaults 0 2
   ```

3. **Montage des partitions** :
   ```
   mount -a
   ```

4. **Copie des données du backup vers le nouveau `/home`** :
   ```
   cp -rp /tmp/home-backup/* /home/
   ```

### Vérifications post-transition

1. **Réactivation de l'accès des utilisateurs**:
   - On repasse en mode normal:
   ```
   systemctl isolate default.target
   ```
   - Si le service SSH a été désactivé, on le réactive:
   ```
   systemctl start sshd
   ```
   - On supprime le fichier `/etc/nologin` pour permettre aux utilisateurs de se reconnecter:
   ```
   rm /etc/nologin
   ```

2. **Vérification de la copie** :
   - On s'assure que toutes les données et permissions sont correctement copiées sur le nouveau volume.

3. **Nettoyage** :
   - Après s'être assuré que tout est en ordre, on peut supprimer le répertoire de backup pour récupérer l'espace :
   ```
   rm -rf /tmp/home-backup
   ```

4. **Test final** :
   - On se connecte en tant qu'utilisateur pour s'assurer que tout est opérationnel.
