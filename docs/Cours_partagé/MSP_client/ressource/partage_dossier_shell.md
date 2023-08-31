1. On commence par créer le partage en utilisant la commande PowerShell suivante :
   ```powershell
   New-smbshare support_info$ -path d:support_info -changeaccess “utilisateurs authentifiés”
   ```
   
2. Pour modifier les autorisations sur ce partage, on suit les étapes ci-dessous :

   a. On récupère les autorisations actuelles (Access Control List, ou ACL) du dossier avec :
   ```powershell
   $acl = get-acl D:support_info
   ```
   
   b. On définit une nouvelle règle (Access Control Entry, ou ACE) pour donner au groupe informatique le droit de modification :
   ```powershell
   $ace = New-Object security.accesscontrol.filesystemaccessrule("L_informatique_RW", "Modify", "Allow")
   ```

   c. On applique cette nouvelle règle à la liste d'autorisations :
   ```powershell
   $acl.addaccessrule($ace)
   ```

   d. On met à jour les autorisations du dossier avec la liste modifiée :
   ```powershell
   set-acl D:support_info $acl
   ```

3. Pour voir la liste des dossiers partagés via la ligne de commande, on tape :
   ```
   net share
   ```
