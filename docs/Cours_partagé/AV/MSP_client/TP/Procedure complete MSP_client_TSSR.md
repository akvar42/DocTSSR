# procedure complete msp_client

# 1.  Installation des systèmes

## 1 - installation

 - Aprés avoir installé les deux machines, avec des volumes logiques
 - je déactive windows update via services.msc
 -  je modifie les plages ip pour faire correspondre leur masques reseau puis je teste leur conectivité. (ping)
 -  sous windows 10 avec l'outils : **ncpa.cpl**
 -  sous debian en éditant **/etc/network/interfaces**
  Par soucis d'efficacité j'utilise le masque de sous reseau de l'hôte puisque les VM sont installé en bridge.

 - Pour pourvoir utiliser le presse papier de mon hôte vers ma VM j'installe Vmware Tools

![plan](plan_reseau.png)


# 2 – Configuration des utilisateurs et de l’environnement

- je crée un fichier .csv dans lequel j'ecris les utilisateur et les groupes auquel ils apartiennent. 

- La création de ce fichier va me simplifier la tache pour les étapes suivante. Dans ce fichier je précise si les utilisateur sont interne ou intérimaire ( car des droit spécifique seront atribué à ces diferentes classes)


```

 Prénom;Nom;login;mail;password;groupe;description
Rick;Grimes;rgrimes;rickgrimes@gmail.com;RGMDP2023!;Direction;Interne
Daryl;Dixon;ddixon;daryldixon@gmail.com;DDMDP2023!;Commercial;Interne
Gabriel;Stokes;gstokes;gabrielstokes@gmail.com;GSMDP2023!;Commercial;Interne
Maggie;Greene;mgreene;maggiegreene@gmail.com;MGMDP2023!;Commercial;Interne
Eugene;Porter;eporter;eugeneporter@gmail.com;EPMDP2023!;Comptable;Interne
Carol;Peletier;cpeletier;carolpeletier@gmail.com;CPMDP2023!;Comptable;intérimaire
Adrien;vincent;Avincent;avincent@mail.com;AVMDP2023!;informatique;Interne
Rosita;Espinosa;respinosa;rositaespinosa@gmail.com;REMDP2023!;Logistique;Interne
Morgan;Jones;mjones;morganjones@gmail.com;MJMDP2023!;Logistique;Interne

```

#  Creation des groupes et des Utilisateurs sur windows 10 via Powershell

- A l'aide de Chat GPT,  Je crée un script qui commencera par lire le fichier CSV.
Pour chaque ligne, il vérifiera si le groupe existe ou non. S'il n'existe pas, il le créera. Ensuite, il créera l'utilisateur avec les détails fournis.

- je modifie la politique d'execution de  powershell pour executer le script avec  ``` Set-ExecutionPolicy Unrestricted ```

- Je lance le script avec powershell en mode administrateur


```
# Chemin vers votre fichier CSV
$csvPath = "C:\Users\AV\Documents\script\users.csv"

# Importer les données du CSV
$usersData = Import-Csv -Path $csvPath -Delimiter ';'

# Parcourir chaque utilisateur et créer l'utilisateur
foreach ($data in $usersData) {
    # Créer le nom complet
    $FullName = "$($data.Nom) $($data.Prénom)"

    # Convertir le mot de passe en SecureString
    $securePassword = ConvertTo-SecureString -AsPlainText $data.password -Force

    # Créer l'utilisateur
    try {
        New-LocalUser -FullName $FullName -Description $data.description -Name $data.login -Password $securePassword -ErrorAction Stop
        Write-Host "Utilisateur $FullName créé avec succès."
    } catch {
        Write-Warning "Erreur lors de la création de l'utilisateur $FullName. Détails : $_"
    }

    # Ajouter l'utilisateur au groupe si nécessaire
    if ($data.groupe) {
        try {
            # Si le groupe n'existe pas, le créer
            if (-not (Get-LocalGroup -Name $data.groupe -ErrorAction SilentlyContinue)) {
                New-LocalGroup -Name $data.groupe -Description "Groupe créé par script"
                Write-Host "Groupe $($data.groupe) créé avec succès."
            }

            # Ajouter l'utilisateur au groupe
            Add-LocalGroupMember -Group $data.groupe -Member $data.login
            Write-Host "Utilisateur $FullName ajouté au groupe $($data.groupe) avec succès."
        } catch {
            Write-Warning "Erreur lors de l'ajout de l'utilisateur $FullName au groupe $($data.groupe). Détails : $_"
        }
    }
}





```

## création utilisateurs et groupes pour Debian

En suite je peux reutilisé mon fichier csv pour debian. En utilisant ce script bash que je rend executable avec la commande ```chmod +x utilisateur_et_group.csv```
- j'execute le script avec ```./ scriptusergp.sh```



```

#!/bin/bash

# Chemin vers le fichier CSV
csvPath="/chemin/vers/fichier.csv"

# Vérifie si le fichier CSV existe
if [ ! -f "$csvPath" ]; then
    echo "Le fichier CSV n'existe pas au chemin spécifié."
    exit 1
fi

# Lire chaque ligne du fichier CSV
while IFS=';' read -r prenom nom login mail password groupe description; do
    # Vérifier l'existence du groupe
    if ! grep -q "^$groupe:" /etc/group; then
        # Créer le groupe s'il n'existe pas
        groupadd "$groupe"
        echo "Groupe $groupe créé."
    fi

    # Créer l'utilisateur
    useradd -m -g "$groupe" -c "$description" -s /bin/bash "$login"
    echo "$password" | passwd --stdin "$login"

    echo "Utilisateur $prenom $nom créé et ajouté au groupe $groupe."
done < "$csvPath"

echo "Tous les utilisateurs et groupes ont été créés."


```


## Ajouter un dossier procedure avec le réglement interieur.

- je crée le dossier sur ma session avec le fichier réglement interieur, puis j'execute ce script afin d'évité de faire manuelement la procedure


 ``` Chemin de destination pour le nouveau dossier sur le bureau de chaque utilisateur
$destinationPath = "C:\Users\*\Desktop\Procédures"

# Chemin du fichier "Règlement intérieur" que vous avez préparé
$sourceFile = "C:\temp\Règlement intérieur.txt"

# Création du dossier "Procédures" sur le bureau de chaque utilisateur
Get-ChildItem -Path "C:\Users\*" -Directory | ForEach-Object {
    $folderPath = Join-Path $_.FullName "Desktop\Procédures"
    if (-not (Test-Path $folderPath)) {
        New-Item -Path $folderPath -ItemType Directory
    }
}

# Copie du fichier "Règlement intérieur" dans le dossier "Procédures" de chaque utilisateur
$sourceFile = "C:\temp\Règlement_intérieur.txt"

Get-ChildItem -Path "C:\Users\*" -Directory | ForEach-Object {
    $folderPath = Join-Path $_.FullName "Desktop\Procédures"
    if (Test-Path $sourceFile) {
        Copy-Item -Path $sourceFile -Destination $folderPath
    }
}
```

ou avec le script de bard

```
$Users = Get-LocalUser
foreach ($User in $Users) {
    New-Item -Path "C:\Users$User\Desktop\Procedure" -ItemType Directory
    New-Item -Path "C:\Users$User\Desktop\Procedure\Reglement interieur" -ItemType File
}

```

### pour le prestataire et son shell ksh

```
# useradd -c "Préstataire" prestataire -m -g informatique --shell /bin/ksh -
p PMDP2023!
```




## Contrainte suplémentaire windows 10 :
## Securité mot de passe

- dans l'invite de commande je lance ```secpol.msc```
- dans "strategie mot de passe" j'active "exigence de complexité"
- dans longeur minimal je fixe à 12

### Ajout nouveau compte administrateur pour le directeur
- je lance powershell en administrateur puis
- je fait 
```net user admin rgrimes /add```

```net user rgrimes * ```

puis tape le nouveaux mot de passe

### Intégration du service informatique au groupe Administrateur
-aprés avoir crée le groupe "Administrateurs"

```Add-LocalGroupMember -Group "Administrateurs" -Member "Avincent"```

### Forçage du changement de mot de passe:
- sur **windows 10** :sans la console MMC, dans utilisateur et groupe: clique droit sur l'utilisateur puis dans l'onglet général "l'utilisateur doit changer le mot de passe à la prochaine ouverture de session"
- dans **Debian** 
```
chage Avincent -d 0

 ```


 ### restriction d'utilisation de périphérique windows 10
 - Pour restreindre l'utilisation de périphérique, j'utilise le logitiel enfichagle disponible dans la console MMC: "éditeur d'objet et stratégie de groupe"

- Dans "objet de stratégie de groupe" je séléctione "NON-adminstrateurs"

- Sous "Configuration utilisateur" - "Modèles d'administration" - "Accès au stockage
amovible » : j'active "CD et DVD : refuser l'accès en lecture/écriture"

- Sous "Composant Windows" - "Windows Store", je  désactive l'application 

- Sous "Modèles d'administration" - "Système", j'active "Empêche l'accès aux outils de modifications du Registre"

- Sous "Modèle d'administration" - "Bureau" -"Bureau", je configure "Papier peint du Bureau", j'ajoute le chemin d'accés à l'image de fond d'écran (fond noir)

- Sous "Configuration ordinateur" - "Paramètres de sécurité" - "Pare-feu Windows
Defender" - "Propriétés du Pare-feu Windows" **J'active** le Pare-feux sur tous les profils (domaine, privé, public)

### vérification

pour mettre a joour les mdoficication systeme
```gpupdate```
pour afficher les informations de résultat de stratégie de groupe (Group Policy) avec \r comme arguments pour resumé
```gpresult \r```


# Ajout des depots Debian et supression de commentaire avec VIM

- Directement depuis bash shell avec l'éditeur de flux sed:
```
sed -i '/^# deb-src/s/^# //' /chemin/vers/votre/sources.list
```

- Ou depuis vim avec la fonction g :

- ```vim /etc/pat/sources.list```
en mode commande
- ```:g:/^deb-src/s/^/#/gc```
- ```:wq ``` pour quitter et sauvegarder


- on peut ajouter le depot ftp
- ```deb-src http://ftp.fr.debian.org/debian/ main contrib non-free```

- on met à jour la liste des depot et paquets
-```apt update```


# 3 Configuration du stockage et des ressources

## création d'une partition DATA avec DISKPART sur windows 10

- Lancement de diskpart dans powershell en mode administrateur

```diskpart```

- listage des disques

```list disk```

- selection du disque à partitioner

```select disk 1```

- on deconect le disque pour s'assuré qu'aucun service ne soit en train de l'utiliser

```offline disk```

- on reconecte

```online disk```

- on crée une table de partition mbr
  
``` convert MBR```
  
- on crée une partion de 15000 Mega octet (15 Giga)

``` create partition primary size=15000```

- on formate en ntfs en appellant la partion DATA
  
```create partition primary size=15000 ```

- on attribue la lettre D au disque

```assign letter=D```

- En faisant ``` list disk ``` on peut voir la modification qui s'est correctement effectué.



## création de partitions sur Debian avec fdisk

- On commence par lister les disques:
```fdisk -l```

- on selectionne le disque à partitionner
```fdisk /dev/sdb```

***on fait trois partitions:***
  
- 1ère partition :
· n : créer une nouvelle partition
· p : type de partition primaire
· Laisser le numéro de partition par défaut
· Laisser le premier secteur par défaut
· +15G pour ajouter 15Go

- 2ème partition:
· n : créer une nouvelle partition
· p : type de partition primaire
· Laisser le numéro de partition par défaut
· Laisser le premier secteur par défaut
· +15G pour ajouter 15Go

- 3ème partition:
· n : créer une nouvelle partition
· p : type de partition primaire
· Laisser le numéro de partition par défaut
· Laisser le premier secteur par défaut
· Laisser le dernier secteur par défaut pour occuper tout l'espace restant


- on quitte fdisk avec ```w```

### Formatage des partitions avec mkfs
- Pour formater la partion en xfs il faut installer xfsprogs

``` apt install xfsprogs ```

- puis on formate avec mkfs en nomant les partitions en donnant un label avec l'argument -L
```mkfs.ext4 -L PROFILS /dev/sdb1```
```mkfs.ext4 -L DATA /dev/sdb2 ```
 ```mkfs.xfs -L LOGS /dev/sdb3```


### Extention du dossier home
  ### methode 1  LVM: 
  il reste de la place sur le groupe de volume logique et j'étend /home
 -on verifie la place disponible:
  ```vgs```
  -on etend le volume logique *LGV est le noms du groupe de volume, (-l +100%FREE) utilise tout l'espace libre du VG.*
 ``` lvextend -l +100%FREE /dev/LGV/HOME```


 

### - Methode 2 - Mise à jour du répertoire `/home`

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

## Mise en commun du volume DATA et dossier service sur le client Debian

- on crée l'arborescence /services puis les dossiers la composant *l'argument -p permet de cre des repertoire parents*

```mkdir -p /service/{commercial,comptabilite,direction,informatique,logistique}```

- on fait correspondre la propriété de chaque dossier avec son groupe

 Dans le repertoire service on tape

 ```
 chown :commercial commercial
 chown :comptabilite comptabilite
 chown :direction direction
 chown :informatique informatique
 chown :logistique logistique
 ```



- Puis on donne aux propriétaires et au groupe propriétaire le droit de lire, écrire et exécuter tous les fichiers et répertoires du répertoire:

``` chmod g+x *```

## Modification des accés au dossier Sur le poste Windows 10

- Ces étapes garantissent que seul le groupe commercial (et le compte système pour des raisons d'administration) peut accéder au dossier « Commerciaux » et que toutes les autres autorisations sont supprimées.


1. On commence par créer un dossier nommé « D:\données\ ». 
2. À l'intérieur de « D:\données\ », on crée un sous-dossier appelé « Commerciaux ».
3. Une fois le dossier créé, on fait un clic-droit dessus et on choisit l'option "Propriétés".
4. Dans la fenêtre des propriétés qui s'ouvre, on se rend à l'onglet "Sécurité" puis on clique sur le bouton "Avancé".
5. Dans la nouvelle fenêtre, on désactive l'option "héritage". Cela empêchera le dossier d'hériter des autorisations des dossiers parents.
6. On supprime ensuite toutes les autorisations héritées pour s'assurer qu'aucun autre groupe ou utilisateur ne peut accéder au dossier.
7. On valide les changements.
8. On retourne à l'onglet "Sécurité", puis on clique sur "Ajouter..." suivi de "Sélectionnez un principal".
9. Dans la liste, on choisit l'option “modification” ainsi que l'option “Appliquer ces autorisations...” avant de valider avec "OK".
10. Enfin, on supprime tous les utilisateurs et groupes listés dans la fenêtre des autorisations, à l'exception du groupe L_commercial_W et du compte système. De cette façon, seuls les membres du groupe L_commercial_W auront accès au dossier, garantissant ainsi que l'accès est interdit à toute personne étrangère au service.




## Creation de partage reseau:
### méthode graphique:
1. On commence par sélectionner le dossier nommé « Support_Info » pour le partager.
2. Afin de le rendre invisible aux autres utilisateurs pour des raisons de sécurité, on ajoute un « $ » à la fin du nom du partage.
3. On effectue un clic gauche sur le dossier et on choisit "Propriétés" dans le menu contextuel.
4. Dans la fenêtre des propriétés, on se dirige vers l'onglet "Partage".
5. On clique ensuite sur "Partage avancé...".
6. Dans la zone "Nom du partage", on ajoute le symbole "$" à la fin pour rendre le partage caché.
7. On clique sur le bouton "Autorisations" pour définir les droits d'accès souhaités.
8. Une fois les autorisations correctement définies, on valide en cliquant sur "OK".
9. Pour confirmer la mise en place du partage, on ouvre l'invite de commande (`cmd`) et on liste les partages disponibles.
10. En préparation pour des déploiements futurs, on recherchera l'équivalent des actions effectuées sous la forme de commandes PowerShell. Ces commandes seront conservées dans un fichier script PowerShell avec l'extension ".ps1".

### En ligne de commande:

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



- Pour testé l'accés le binôme crée un lecteur U qui pointe sur le dossier: (avec l'ip de la VM)

```net use U: \\10.107.200.80\Support_info$ /persistent:yes```


# Gestion des imprimantes

### Installation et partage de l'imprimante HP LaserJet M9050 MFP

1. **Démarrage du gestionnaire d'ajout d'imprimante** :
   - On se rend dans `Panneau de configuration` > `Matériel et audio` > `Périphériques et imprimantes`.
   - On clique sur `Ajouter une imprimante`.

2. **Choix du type d'imprimante** :
   - Lorsqu'on est interrogé sur la manière d'installer l'imprimante, on choisit `Ajouter une imprimante en utilisant une adresse IP ou un nom d'hôte`.
   - On clique sur `Suivant`.

3. **Renseignement de l'adresse IP** :
   - Dans le champ `Nom d'hôte ou adresse IP`, on inscrit `l'IP de l'imprimante`.
   - On s'assure que l'option `Interroger l'imprimante et sélectionner automatiquement le pilote à utiliser` est activée.
   - On clique sur `Suivant`.

4. **Sélection du pilote** :
   - Si Windows reconnaît l'imprimante, il peut proposer un pilote par défaut. Sinon, on va sur le site d'[HP](https://support.hp.com/fr-fr/drivers/)
  et on cherche dans la liste des pilotes.
   - Si le pilote n'est pas listé dans windows, il faudra peut-être le télécharger depuis le site officiel de HP et l'installer manuellement.
   - On clique sur `Suivant`.

1. **Nom de l'imprimante** :
   - On donne un nom à l'imprimante, par exemple : "HP LaserJet M9050 MFP".
   - On clique sur `Suivant`.

2. **Options de partage** :
   - Quand l'option de partage est présentée, on coche `Partager cette imprimante`.
   - Dans le champ `Nom de partage`, on indique un nom qui sera utilisé sur le réseau pour accéder à cette imprimante. Par exemple, "HPM9050_Shared".
   - On clique sur `Suivant`.

3. **Finalisation** :
   - Une page récapitulative est présentée. On vérifie toutes les informations.
   - On clique sur `Terminer`.

4. **Test** :
   - Pour confirmer que tout est bien configuré, on imprime une page test.

5. **Accès depuis un autre poste** :
   - Depuis un autre ordinateur du réseau, on va dans `Périphériques et imprimantes`, puis on ajoute une imprimante.
   - On recherche l'imprimante partagée par nom et l'ajoute à la liste des imprimantes de l'ordinateur.
 

### Configuration des permissions pour l'imprimante

1. **Accès aux propriétés de l'imprimante** :
   - On ouvre le menu `Démarrer`, puis on clique sur `Périphériques et imprimantes`.
   - On trouve l'imprimante "HP LaserJet M9050 MFP" et on fait un clic droit dessus, puis on choisit `Propriétés`.

2. **Modification des permissions** :
   - Dans la fenêtre des propriétés de l'imprimante, on se rend dans l'onglet `Sécurité`.

3. **Permissions pour tous les utilisateurs** :
   - On clique sur `Ajouter` et saisit "Utilisateurs" (ou le groupe qui représente tous les utilisateurs sur le système).
   - On coche la permission `Imprimer`.
   - On clique sur `Appliquer`.

4. **Permissions pour le service Comptabilité** :
   - On clique sur `Ajouter` et saisit le nom du groupe ou de l'utilisateur représentant le service Comptabilité.
   - On coche les permissions `Imprimer` et `Gérer les documents` (ce qui permettra de supprimer des impressions bloquées).
   - On clique sur `Appliquer`.

5. **Permissions pour le service Informatique** :
   - On clique sur `Ajouter` et saisit le nom du groupe ou de l'utilisateur représentant le service Informatique.
   - On coche `Contrôle total` (qui accorde toutes les permissions).
   - On clique sur `Appliquer`.

6. **Validation** :
   - Une fois que toutes les permissions sont correctement configurées, on clique sur `OK` pour fermer les propriétés de l'imprimante.

### Création d'un pool d'impression pour deux imprimantes Xerox Office Color

1. **Installation des imprimantes individuelles** :
   - **Accès au menu Ajouter une imprimante** :
     - On ouvre le menu `Démarrer`, puis on clique sur `Périphériques et imprimantes`.
     - On choisit `Ajouter une imprimante`.
   - **Ajout de la première imprimante (ip1)** :
     - On choisit `Ajouter une imprimante en utilisant une adresse IP ou un nom d'hôte`.
     - On saisit l'adresse IP "ip1" et on suit les étapes pour installer l'imprimante avec le pilote approprié.
   - **Répétition pour la deuxième imprimante (ip2)** :
     - On répète les mêmes étapes pour ajouter la deuxième imprimante en utilisant l'adresse IP "ip2".

2. **Création du pool d'impression** :
   - On retourne à `Périphériques et imprimantes`.
   - On fait un clic droit sur l'une des deux imprimantes Xerox que nous venons d'ajouter, et on choisit `Propriétés de l'imprimante`.
   - Dans l'onglet `Ports`, on coche les ports correspondant aux adresses IP "ip1" et "ip2" pour les ajouter au pool.
   - On confirme en cliquant sur `Appliquer` ou `OK`.

3. **Configuration des paramètres de pool** :
   - Dans les `Propriétés de l'imprimante`, on se dirige vers l'onglet `Avancé`.
   - On coche l'option `Activer le pool d'impression`.
   - On s'assure que les ports correspondant aux deux imprimantes sont sélectionnés.

4. **Validation** :
   - Pour tester le pool d'impression, on envoie un document à imprimer sur l'imprimante poolée.
   - On vérifie que le document est imprimé par l'une des deux imprimantes Xerox.
   - Si tout fonctionne correctement, le pool d'impression est prêt à être utilisé.


### Configuration des permissions pour les imprimantes sur Windows 10

1. **Accéder aux propriétés de l'imprimante** :
    - On ouvre `Périphériques et imprimantes` depuis le Panneau de configuration.
    - On fait un clic droit sur l'imprimante concernée, puis on sélectionne `Propriétés de l'imprimante`.

2. **Ajustement des permissions** :
    - On va dans l'onglet `Sécurité`.
    - On supprime le groupe `Tout le monde` en le sélectionnant et en cliquant sur `Supprimer`.
    - On clique sur `Ajouter` pour ajouter le groupe ou les utilisateurs du service Comptabilité. Après avoir ajouté, on leur coche `Imprimer` dans la liste des permissions.
    - On répète l'ajout pour le service `Informatique` et on leur accorde le `Contrôle total`.

3. **Configurer les horaires d'utilisation** :
    - Sous l'onglet `Avancé`, on coche l'option `Disponible de`.
    - On définit la tranche horaire de `19:00` à `03:00`.
  
4. **Configuration des administrateurs** :
    - Retour dans l'onglet `Sécurité`.
    - On sélectionne le groupe ou les utilisateurs du service `Informatique`.
    - On coche `Contrôle total` dans la liste des permissions.

5. **Validation** :
    - On valide les modifications en cliquant sur `OK`.
    - Après avoir configuré les permissions et horaires, on teste pour s'assurer que tout fonctionne correctement.
    - On essaie d'imprimer depuis un compte du service `Comptabilité` hors des horaires définis pour confirmer que la restriction fonctionne.
    - On répète le test pendant les horaires définis pour s'assurer qu'ils peuvent imprimer.
    - Enfin, on se connecte avec un compte du service `Informatique` pour s'assurer qu'ils ont un contrôle total sur l'imprimante.

### Configuration de deux files d'attente pour la Xerox Office Color et deplacement du pool dans D:

1. **Création de la première file d'attente**:
    - On ouvre `Périphériques et imprimantes` depuis le Panneau de configuration.
    - On choisit `Ajouter une imprimante` puis on suit l'assistant pour ajouter la Xerox Office Color. Nommez cette file d'attente par exemple "Xerox Office Color - Directeurs".
  
2. **Création de la deuxième file d'attente**:
    - On répète le processus d'ajout d'une nouvelle imprimante. Cette fois, on nomme la file d'attente, par exemple, "Xerox Office Color - Général".
  
3. **Attribution de la priorité aux directeurs**:
    - Dans `Périphériques et imprimantes`, on fait un clic droit sur "Xerox Office Color - Directeurs", puis on sélectionne `Propriétés de l'imprimante`.
    - Dans l'onglet `Avancé`, on modifie la `Priorité` en mettant une valeur élevée, par exemple 10.
    - Pour "Xerox Office Color - Général", on répète le processus, mais on définit la priorité à une valeur plus basse, par exemple 5.

4. **Déplacer le spool d'impression**:
    - Toujours dans `Périphériques et imprimantes`, on clique sur `Serveur d'impression` en haut de la fenêtre, puis on ouvre les `Propriétés`.
    - Dans l'onglet `Avancé`, on repère l'option `Emplacement du spool`.
    - On change le chemin actuel de "C:\Windows\System32\spool\PRINTERS" à "D:\spool\PRINTERS" 
    - crée le dossier "D:\spool\PRINTERS"  avant d'effectuer le changement.

5. **Redémarrer le service d'impression**:
    - Pour que les modifications prennent effet, on doit redémarrer le service Spouleur d'impression. Pour ce faire, on peut ouvrir le `Gestionnaire de services` et redémarrer le service `Spouleur d'impression`, ou simplement redémarrer l'ordinateur.


 # 4 - Configuration avancée des systems
 ## Modification du chargeur d'amorçage du grub à 2 seconde:

- on modifie GRUB_TIMEOUT avec valeur : 2

``` vim  /etc/default/grub ```

- puis on met à jour le Grub:

```update-grub```



### Redimensionnement et configuration du swap sur Debian

**Remarque**: Faire Snapshot avant la procedure !!!

1. **Désactivation du swap**:
    - Avant d'apporter des modifications à l'espace de swap, on s'assure qu'il est désactivé.
    ```
    swapoff /dev/sda2
    ```

2. **Modification du partitionnement avec `fdisk`**:
    - On utilise l'outil `fdisk` pour ajuster le partitionnement de la partition `/dev/sda`.
    ```
    fdisk /dev/sda
    ```

    - Une fois dans `fdisk`:
        - On choisit `p` pour afficher la table des partitions.
        - On choisit `d` pour supprimer la partition de swap actuelle.
        - On choisit `n` pour créer une nouvelle partition.
        - On suit les invites pour spécifier la taille et le type (swap).

3. **Formatage de la partition en tant que swap**:
    - Une fois la partition correctement dimensionnée, on la formate pour le swap.
    ```
    mkswap /dev/sda2
    ```

4. **Mise à jour du fichier `/etc/fstab`**:
    - Ce fichier permet au système de savoir où trouver les systèmes de fichiers lors du démarrage.
    ```
    nano /etc/fstab
    ```

    - Dans l'éditeur:
        - On repère la ligne existante pour le swap et la commente en ajoutant un `#` au début de la ligne.
        - On ajoute ensuite la nouvelle configuration pour le swap:
        ```
        /dev/sda2 swap swap defaults 0 0
        ```

5. **Activation du swap**:
    - Avec la nouvelle configuration en place, on active le swap.
    ```
    swapon /dev/sda2
    ```

6. **Mise à jour de Debian**:
    - Maintenant que le swap est correctement configuré, on procède à la mise à jour du système Debian.
    ```
    apt update
    apt upgrade
    ```

>

### Activation et configuration du bureau à distance sur Windows 10

1. **Accéder au panneau de configuration**:
    - On ouvre le menu "Démarrer", on recherche "Panneau de configuration" et on le sélectionne.

2. **Naviguer vers les paramètres du Bureau à distance**:
    - Dans le panneau de configuration, on clique sur "Système et sécurité", puis sur "Autoriser l'accès à distance" sous la section "Système".

3. **Activer le Bureau à distance**:
    - On coche la case "Autoriser les connexions à distance à cet ordinateur".
    - On s'assure que "Autoriser uniquement les connexions à partir d'ordinateurs exécutant le Bureau à distance avec authentification au niveau du réseau (recommandé)" est également coché.

4. **Ajouter le groupe des informaticiens aux utilisateurs du Bureau à distance**:
    - On ouvre l'invite de commandes PowerShell avec des droits administratifs. Pour ce faire, on clique droit sur le menu Démarrer et on choisit "Windows PowerShell (admin)".
    - On saisit la commande suivante pour ajouter le groupe "informatique" aux utilisateurs autorisés du Bureau à distance :
      ```powershell
      net localgroup "utilisateurs du bureau à distance" informatique /add
      ```
    - On peut vérifier si l'opération a été réussie en entrant :
      ```powershell
      net localgroup "utilisateurs du bureau à distance"
      ```
      On s'attend à voir "informatique" dans la liste des membres.

5. **Vérification du numéro de port RDP**:
    - Pour connaître le numéro de port utilisé par le Bureau à distance, on utilise la commande :
      ```powershell
      netstat -an | find "3389"
      ```
      Si le port 3389 apparaît dans les résultats, cela signifie que le Bureau à distance est correctement configuré pour utiliser ce port par défaut.

6. **Finalisation**:
    - Une fois toutes ces étapes effectuées, on redémarre l'ordinateur pour que les modifications prennent effet. On teste ensuite la connexion à distance pour s'assurer que tout fonctionne correctement.

>

# 5 – Installation d’applications
## sur windows 10
## Installation silencieuse de 7-Zip

1. **Téléchargement du logiciel**:
   - On se rend sur le site officiel de 7-Zip pour télécharger l'installateur du logiciel, soit en version 32 bits (x86) ou 64 bits (x64), en fonction de la version de Windows sur laquelle on souhaite installer.

2. **Préparation de l'installation silencieuse**:
   - On s'assure d'avoir les droits administratifs sur la machine. Si ce n'est pas le cas, on doit exécuter l'installateur avec des droits élevés.

3. **Lancement de l'installation silencieuse**:
   - On ouvre l'invite de commandes (CMD) en tant qu'administrateur.
   - On navigue vers l'emplacement où se trouve l'installateur téléchargé à l'étape 1. Par exemple, si l'installateur est sur le bureau, on utilise la commande : 
     ```
     cd %AV%\Desktop
     ```
  
     
   - Pour la version 64 bits (nom de fichier par défaut : `7zXXXX-x64.msi`):
     ```
     msiexec /i 7zXXXX-x64.msi /qn
     ```
     On remplace `XXXX` par le numéro de version approprié.

4. **Vérification**:
   - Après l'installation, on vérifie que 7-Zip est correctement installé. On peut le faire en ouvrant le menu Démarrer et en recherchant 7-Zip. Si l'application est présente, cela signifie que l'installation a été réussie.

> **Note** : Le commutateur `/qn` signifie "quiet no UI". Il permet une installation silencieuse sans interface utilisateur. L'alerte UAC (Contrôle de compte utilisateur) pourrait toujours s'afficher pour demander l'autorisation d'installer le logiciel. 


## Connexion RDP à un poste Windows depuis Debian/Linux

### 1. Recherche d'applications gérant le protocole RDP avec NLA:
- Avant d'installer tout logiciel, on vérifie les solutions disponibles dans les dépôts officiels pour gérer le protocole RDP :
```
apt search rdp
apt search bureau à distance
```
ou
```
apt search remote desktop
```

### 2. Installation de Remmina:
- Suite à la recherche, on détermine que `Remmina` est l'outil adapté à nos besoins, en particulier pour gérer l'authentification NLA.
  
Pour installer Remmina :
```
apt install remmina
```

### 3. Configuration et utilisation de Remmina:
- On ouvre l'interface graphique et lance `Remmina`.
- Dans Remmina, on clique sur l'option pour créer une nouvelle connexion.
- On sélectionne `RDP` comme protocole.
- On renseigne les informations nécessaires pour la connexion :
  - Serveur: Adresse IP ou nom d'hôte du poste Windows.
  - Nom d'utilisateur: Nom d'utilisateur pour la connexion.
  - Mot de passe: Mot de passe associé.
  - Domaine: Si nécessaire, on spécifie le domaine de connexion.
  
Une fois les informations renseignées, on clique sur `Connexion` pour initier la session RDP.

## Installation de Webmin pour la gestion via une interface web

### 1. Installation en ligne :
On suit le guide disponible sur le site officiel de Webmin : [Guide d'installation de Webmin](https://www.webmin.com/deb.html)

### 2. Gestion des dépendances manquantes :
Si des dépendances sont manquantes, on les installe en utilisant les commandes appropriées, par exemple :
```
apt install [nom_de_la_dépendance]
```

### 3. Réparation de Webmin si nécessaire :
Dans le cas où Webmin serait endommagé après l'installation, on utilise la commande suivante pour le réparer :
```
apt install --fix-broken
```

### 4. Accès à l'interface de Webmin :
Après l'installation, on ouvre un navigateur et se rend à l'adresse suivante : `https://[adresse_ip_du_serveur]:10000`
Si une alerte de sécurité apparaît en raison du certificat SSL auto-signé, on choisit de "continuer" ou "accepter le risque" pour accéder à l'interface.

### 5. Authentification :
À la page de connexion, on s'authentifie en tant que `root` ou tout autre utilisateur disposant des droits d'administration.

### 6. Vérification :
Une fois connecté, on peut voir l'interface de Webmin. Tout est en ordre si l'on peut naviguer sans problème.

# 6 – Sauvegarde et restauration

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

## Sauvegarde sur les postes Windows 10

### 1. Ajout d'un nouveau disque dur :
- Si l'espace de stockage est insuffisant, on commence par ajouter un disque dur de 60 Go.
  - On suit la procédure déjà fournie d’ajout de disque sous Vmware workstation.

### 2. Création d'une image système :
- Aller dans **Démarrer** > **Paramètres** > **Système** > **Stockage** > **Gestion des disques**.
- Une fois dans le gestionnaire de disques :
  - On repère le nouveau disque de 60 Go qui devrait apparaître comme "Non alloué".
  - Faire un clic-droit sur ce disque puis choisir "Nouveau volume simple".
  - Suivre l'assistant : choisir la taille maximale pour le volume, attribuer une lettre au disque, puis formater le volume avec le format NTFS et attribuer un nom de votre choix.
- Pour créer une image :
  - Aller dans **Panneau de configuration** > **Système et sécurité** > **Sauvegarder et restaurer**.
  - Dans le volet de gauche, choisir **Créer une image système**.
  - Suivre l'assistant, choisir le disque nouvellement créé pour stocker l'image.

### 3. Planification d'une sauvegarde journalière :
- Retourner dans **Panneau de configuration** > **Système et sécurité** > **Sauvegarder et restaurer**.
  - Cliquer sur "Configurer la sauvegarde".
  - Dans la nouvelle fenêtre, choisir "Enregistrer sur un réseau...".
  - Une boîte de dialogue s'ouvre pour demander l'emplacement réseau. Entrer `\@ip_du_binôme\Support_Info` et fournir les informations d'identification nécessaires.
  - Une fois l'emplacement réseau choisi, sélectionner "Me laisser choisir" pour choisir les dossiers à sauvegarder.
  - Cocher uniquement le dossier "Support_Info" et décocher l'option "Inclure une image système de lecteurs".
  - Passer à l'étape suivante et choisir "Modifier la planification". Choisir une sauvegarde quotidienne et régler l'heure sur 13:00.

### 4. Ajustement de l'heure de sauvegarde :
- Pour une planification précise à 12h45, ouvrir le **Planificateur des tâches** à partir du menu Démarrer.
  - Dans la fenêtre du Planificateur des tâches, chercher dans le volet central la tâche nommée "AutomaticBackup".
  - Faire un double-clic dessus pour l'ouvrir.
  - Aller dans l'onglet "Déclencheurs" et modifier le déclenchement existant.
  - Régler l'heure sur 12h45 et confirmer.

## Conclusion :
Avec ces étapes, on assure que le système Windows 10 est correctement sauvegardé et que les données importantes sont sécurisées régulièrement.

## Paramétrage des points de restauration sur le volume « C: » sous Windows 10

### 1. Accès à la gestion des points de restauration système:

- On commence par ouvrir le **Panneau de configuration**. 
  - Pour ce faire, on clique sur le bouton **Démarrer**, tape "Panneau de configuration" dans la barre de recherche et sélectionne l'application correspondante parmi les résultats.

- Une fois dans le **Panneau de configuration**, on clique sur **Système et sécurité**.

- Dans la fenêtre suivante, on clique sur **Système**.

- Sur le volet de gauche, on sélectionne **Protection du système**. Cela ouvre une fenêtre nommée "Propriétés système", avec l'onglet "Protection du système" actif.

### 2. Configuration des points de restauration pour le lecteur C:

- Sous l'onglet **Protection du système**, dans la section "Protection des paramètres", on repère le lecteur **C:**.

- Si la protection est désactivée pour le lecteur **C:**, on le sélectionne puis clique sur **Configurer...**.

- Dans la fenêtre qui s'affiche :
  - On coche **Activer la protection du système**.
  
  - Dans "Utilisation maximale", on définit l'espace disque à utiliser pour la protection du système à **8%**.

  - On confirme les modifications en cliquant sur **Appliquer** puis **OK**.

### 3. Création d'un point de restauration système:

- Toujours dans l'onglet **Protection du système**, avec le lecteur **C:** sélectionné, on clique sur **Créer...**.

- On nomme le point de restauration (par exemple, "Point initial") et clique sur **Créer**.

- Une fois le point de restauration créé, un message de confirmation apparaît.

- On ferme toutes les fenêtres ouvertes pour terminer la procédure.

## note:
On a désormais paramétré la protection du système pour le lecteur **C:** en réservant 8% de sa capacité pour les points de restauration et créé un point de restauration initial.
