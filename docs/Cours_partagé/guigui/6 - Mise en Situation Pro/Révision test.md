# LINUX

## FHS linux : arborescence ?

Le FHS (Filesystem Hierarchy Standard) est un ensemble de normes et de conventions utilisées dans les systèmes d'exploitation Linux et d'autres systèmes Unix-like pour organiser la structure des répertoires et des fichiers sur le système de fichiers. Cette structure normalisée permet de garantir la cohérence et la compatibilité entre différentes distributions Linux et d'assurer que les applications et les services fonctionnent de manière prévisible.

L'arborescence du FHS est basée sur plusieurs répertoires principaux, chacun ayant un rôle spécifique. Voici les répertoires les plus importants dans l'arborescence du FHS :

1. **/bin** : Contient les fichiers binaires (programmes exécutables) nécessaires au démarrage du système et à la maintenance de base. Ces programmes sont essentiels, même si le système de fichiers principal n'est pas monté.

2. **/sbin** : Similaire à `/bin`, mais contient des programmes exécutables réservés à l'administration système. Ces programmes nécessitent souvent des privilèges administratifs.

3. **/usr** : Contient la majorité des programmes et des fichiers utilisés par les utilisateurs, y compris les bibliothèques partagées, la documentation et les en-têtes de développement.

   - **/usr/bin** : Programmes et exécutables pour les utilisateurs.
   - **/usr/sbin** : Programmes exécutables réservés à l'administration système dans l'arborescence `/usr`.
   - **/usr/lib** : Bibliothèques partagées pour les programmes dans `/usr/bin` et `/usr/sbin`.
   - **/usr/include** : Fichiers d'en-tête utilisés pour le développement.
   - **/usr/share** : Données partagées utilisées par différentes applications.

4. **/etc** : Contient les fichiers de configuration du système et des applications. Les fichiers dans ce répertoire permettent de personnaliser le comportement du système et des logiciels.

5. **/var** : Contient des données variables qui peuvent être modifiées pendant l'exécution du système. Cela inclut des fichiers de journaux, des bases de données, des spools d'impression, etc.

6. **/tmp** : Un répertoire temporaire où les programmes et les utilisateurs peuvent stocker des fichiers temporaires. Les fichiers dans ce répertoire sont généralement supprimés au redémarrage.

7. **/home** : Les répertoires personnels des utilisateurs sont généralement situés ici. Chaque utilisateur a un répertoire séparé pour stocker ses fichiers personnels.

8. **/root** : Le répertoire personnel de l'utilisateur root, l'administrateur du système.

9. **/boot** : Contient les fichiers nécessaires au démarrage du système, tels que les fichiers du chargeur de démarrage (bootloader) et le noyau du système d'exploitation.

10. **/lib** : Contient les bibliothèques partagées nécessaires au démarrage du système.

Il existe de nombreux autres répertoires dans l'arborescence du FHS, chacun ayant un but spécifique. Cette structure standardisée facilite le développement, la maintenance et la portabilité des applications et des systèmes entre différentes distributions Linux.



## Linux : comment compter des mots, lignes ?

Sur un système Linux, il existe plusieurs commandes en ligne que vous pouvez utiliser pour compter des mots, des lignes et d'autres statistiques dans un fichier texte. Voici quelques-unes des commandes les plus couramment utilisées à cette fin :

1. **wc** : La commande "wc" (word count) est très polyvalente et peut compter les mots, les lignes et les caractères dans un fichier. Voici comment l'utiliser :

   - Pour compter le nombre de lignes, de mots et de caractères dans un fichier :
     ```
     wc fichier.txt
     ```

   - Pour compter uniquement le nombre de lignes :
     ```
     wc -l fichier.txt
     ```

   - Pour compter uniquement le nombre de mots :
     ```
     wc -w fichier.txt
     ```

   - Pour compter uniquement le nombre de caractères :
     ```
     wc -c fichier.txt
     ```

2. **grep et wc** : Vous pouvez combiner la commande "grep" avec "wc" pour compter des occurrences spécifiques dans un fichier. Par exemple, pour compter le nombre de lignes contenant un mot particulier "motif" dans un fichier :

   ```
   grep -c "motif" fichier.txt
   ```

3. **cat et wc** : Si vous voulez compter le nombre de lignes dans un fichier sans afficher son contenu, vous pouvez utiliser la commande "cat" en combinaison avec "wc" :

   ```
   cat fichier.txt | wc -l
   ```

4. **sed et wc** : Pour compter le nombre de lignes correspondant à un certain critère (par exemple, lignes vides) dans un fichier, vous pouvez utiliser "sed" avec "wc" :

   ```
   sed '/^$/d' fichier.txt | wc -l
   ```

Ces commandes sont très utiles pour obtenir des statistiques rapides sur les fichiers texte. Assurez-vous de remplacer "fichier.txt" par le chemin et le nom de fichier réel que vous souhaitez analyser.


## Linux : gestion utilisateur et mdp

La gestion des utilisateurs et des mots de passe est un aspect important de la sécurité et de l'administration d'un système Linux. Linux propose des outils et des commandes pour créer, modifier, supprimer et gérer les comptes d'utilisateurs ainsi que les mots de passe associés. Voici comment cela fonctionne :

1. **Création d'utilisateurs** :
   Pour créer un nouvel utilisateur, vous pouvez utiliser la commande `useradd` suivie du nom d'utilisateur. Par exemple, pour créer un utilisateur nommé "john", vous pouvez saisir :
   ```
   sudo useradd john
   ```
   Cela créera un compte utilisateur avec les paramètres par défaut.

2. **Définition de mots de passe** :
   Une fois qu'un utilisateur est créé, vous devez définir un mot de passe pour ce compte. Utilisez la commande `passwd` suivie du nom d'utilisateur pour définir un mot de passe :
   ```
   sudo passwd john
   ```
   Vous serez invité à saisir et confirmer le nouveau mot de passe.

3. **Modification d'utilisateurs et de mots de passe** :
   Pour modifier les informations d'un utilisateur existant, vous pouvez utiliser la commande `usermod`. Par exemple, pour changer le nom d'utilisateur de "john" en "jane", vous pouvez saisir :
   ```
   sudo usermod -l jane john
   ```
   Pour modifier le mot de passe d'un utilisateur, utilisez à nouveau la commande `passwd` suivie du nom d'utilisateur.

4. **Suppression d'utilisateurs** :
   Pour supprimer un utilisateur, utilisez la commande `userdel` suivie du nom d'utilisateur. Par exemple, pour supprimer l'utilisateur "jane" :
   ```
   sudo userdel jane
   ```
   Notez que cela supprimera également le répertoire personnel de l'utilisateur, sauf si vous utilisez l'option `-r`.

5. **Gestion des groupes** :
   Les utilisateurs peuvent être regroupés en groupes, ce qui facilite la gestion des permissions. Utilisez la commande `groupadd` pour créer un groupe et la commande `usermod` pour ajouter un utilisateur existant à un groupe.

6. **Utilisation de sudo** :
   Les tâches d'administration nécessitent souvent des privilèges élevés. La commande `sudo` permet à un utilisateur autorisé d'exécuter des commandes avec ces privilèges. L'ajout d'un utilisateur au groupe "sudo" permet généralement l'utilisation de cette commande.

7. **Gestion des fichiers et des permissions** :
   Chaque utilisateur possède un répertoire personnel dans `/home` où il peut stocker ses fichiers. Les permissions sur les fichiers et les répertoires sont gérées par des attributs comme le propriétaire, le groupe propriétaire et les permissions de lecture, écriture et exécution.

La gestion des utilisateurs et des mots de passe est un aspect crucial de l'administration système, et une bonne compréhension de ces concepts est essentielle pour maintenir la sécurité et l'efficacité d'un système Linux.


## Gestion des archives avec tar

La commande `tar` (pour "tape archive") est utilisée pour créer et manipuler des archives dans les systèmes Unix et Linux. Une archive est un fichier unique contenant un ou plusieurs fichiers ou répertoires, généralement compressés pour économiser de l'espace disque ou faciliter le transfert. Voici comment fonctionne la gestion des archives avec `tar` :

**Créer une archive :**
La commande de base pour créer une archive est la suivante :
```bash
tar -cvf archive.tar fichier1 fichier2 dossier1 dossier2
```
- `-c` : Créer une nouvelle archive.
- `-v` : Afficher le détail des fichiers ajoutés à l'archive (verbose).
- `-f` : Spécifier le nom de l'archive.

Vous pouvez également ajouter des options de compression pour créer une archive compressée. Par exemple, pour créer une archive compressée au format gzip :
```bash
tar -czvf archive.tar.gz fichier1 fichier2 dossier1 dossier2
```

**Extraire une archive :**
Pour extraire le contenu d'une archive, utilisez la commande suivante :
```bash
tar -xvf archive.tar
```
- `-x` : Extraire le contenu de l'archive.
- Les autres options sont les mêmes que lors de la création d'une archive.

Si l'archive est compressée, vous devez spécifier l'option de décompression correspondante. Par exemple, pour extraire une archive au format gzip :
```bash
tar -xzvf archive.tar.gz
```

**Lister le contenu d'une archive :**
Pour afficher la liste des fichiers contenus dans une archive sans extraire son contenu, utilisez l'option `-t` :
```bash
tar -tvf archive.tar
```

**Ajouter des fichiers à une archive existante :**
Si vous souhaitez ajouter des fichiers à une archive existante, utilisez l'option `-r` :
```bash
tar -rvf archive.tar nouveau_fichier
```

**Supprimer des fichiers d'une archive :**
La suppression de fichiers d'une archive est un peu plus complexe. Vous devez extraire l'archive, supprimer les fichiers nécessaires et ensuite recréer l'archive mise à jour. Voici un exemple :
```bash
tar -xvf archive.tar
rm fichier_a_supprimer
tar -cvf archive.tar fichier1 fichier2 dossier1 dossier2
```

La commande `tar` offre de nombreuses autres options pour gérer les archives, telles que la spécification de répertoires de travail, l'exclusion de certains fichiers, etc. Vous pouvez en savoir plus en consultant la page de manuel avec la commande `man tar` ou en consultant des ressources en ligne.


## Afficher le contenu d'un fichier, y compris le debut ou la fin

Pour afficher le contenu d'un fichier, y compris le début ou la fin, sous Linux, vous avez plusieurs options. Voici quelques commandes couramment utilisées pour effectuer cette tâche :

**1. Afficher tout le contenu d'un fichier :**
Pour afficher le contenu complet d'un fichier, vous pouvez utiliser la commande `cat` :
```bash
cat nom_fichier
```

**2. Afficher le début d'un fichier :**
La commande `head` permet d'afficher les premières lignes d'un fichier. Par défaut, elle affiche les 10 premières lignes, mais vous pouvez spécifier un nombre différent en utilisant l'option `-n` :
```bash
head -n 20 nom_fichier  # Affiche les 20 premières lignes du fichier
```

**3. Afficher la fin d'un fichier :**
La commande `tail` affiche les dernières lignes d'un fichier. Par défaut, elle affiche les 10 dernières lignes, mais comme avec `head`, vous pouvez spécifier un nombre différent avec `-n` :
```bash
tail -n 15 nom_fichier  # Affiche les 15 dernières lignes du fichier
```

**4. Afficher le début ou la fin avec `less` :**
La commande `less` permet de visualiser le contenu d'un fichier de manière paginée, ce qui signifie que vous pouvez faire défiler le contenu vers le haut et vers le bas. Pour voir le début du fichier, vous pouvez simplement lancer `less` suivi du nom du fichier :
```bash
less nom_fichier
```
Une fois dans l'interface `less`, vous pouvez utiliser les touches fléchées ou d'autres commandes pour naviguer. Par exemple, appuyez sur la touche "G" pour aller à la fin du fichier et sur "q" pour quitter.

**5. Afficher le début ou la fin avec `more` :**
La commande `more` est similaire à `less`, mais elle est moins interactive. Pour afficher le début d'un fichier avec `more` :
```bash
more nom_fichier
```
Pour naviguer, utilisez la touche Espace pour faire défiler une page à la fois et la touche "q" pour quitter.

Ces commandes sont utiles pour afficher différentes parties d'un fichier, que ce soit le début, la fin ou le contenu complet, en fonction de vos besoins.


## gestion des droits avec chmod

### Exemple de la commande : `chmod 664 /home/hk1/fic.txt`

La commande `chmod` est utilisée pour modifier les permissions (droits) d'accès aux fichiers et aux répertoires sous les systèmes Unix et Linux. Les permissions sont divisées en trois catégories principales : le propriétaire (user), le groupe (group) et les autres utilisateurs (others). Chaque catégorie a des droits spécifiques qui peuvent être activés ou désactivés. Voici comment comprendre et interpréter la commande `chmod 664 /home/hk1/fic.txt` :

- `chmod` : Commande pour modifier les permissions.
- `664` : Les trois chiffres représentent les droits d'accès pour différentes catégories, dans l'ordre : propriétaire, groupe, autres.
  - Le premier chiffre (6) représente les droits du propriétaire.
  - Le deuxième chiffre (6) représente les droits du groupe.
  - Le troisième chiffre (4) représente les droits des autres utilisateurs.

Les droits d'accès sont représentés par des combinaisons de trois chiffres (ou bits) :
- 4 : Lecture (r)
- 2 : Écriture (w)
- 1 : Exécution (x)

Dans l'exemple (`chmod 664 /home/hk1/fic.txt`), les droits sont définis comme suit :

- Propriétaire : Lecture (r) + Écriture (w) = 6
- Groupe : Lecture (r) + Écriture (w) = 6
- Autres utilisateurs : Lecture (r) = 4

Cela signifie que le propriétaire et le groupe ont la permission de lire et d'écrire le fichier `fic.txt`, tandis que les autres utilisateurs ont uniquement la permission de le lire.

Il est important de noter que les chiffres dans la commande `chmod` sont généralement octaux, ce qui signifie qu'ils sont basés sur la notation en base 8. Les combinaisons de 3 chiffres (4, 2, 1) sont utilisées pour représenter les droits de lecture, écriture et exécution. Pour calculer les chiffres, additionnez les valeurs correspondantes (4 pour lecture, 2 pour écriture, 1 pour exécution).

L'exemple donné (`chmod 664 /home/hk1/fic.txt`) est un exemple courant où les droits de lecture et d'écriture sont accordés au propriétaire et au groupe, tandis que les autres utilisateurs ont seulement le droit de lecture.


## grep et find, différence et utilisation

`grep` et `find` sont deux commandes largement utilisées dans les systèmes Unix et Linux pour rechercher des fichiers ou des lignes de texte dans des fichiers. Bien qu'ils soient tous les deux des outils de recherche, ils ont des utilisations légèrement différentes.

**1. `grep` :**

`grep` est utilisé pour rechercher des motifs spécifiques (chaînes de caractères) dans le contenu des fichiers texte. Il est principalement utilisé pour rechercher des lignes de texte correspondant à un modèle donné.

**Syntaxe de base :**
```bash
grep motif fichier
```

Exemple :
```bash
grep "motif" fichier.txt
```

`grep` peut également être utilisé avec des options pour des recherches plus avancées, comme ignorer la casse (`-i`), afficher le numéro de ligne (`-n`), rechercher récursivement dans les répertoires (`-r`), etc.

**2. `find` :**

`find` est utilisé pour rechercher des fichiers et des répertoires en fonction de critères tels que le nom du fichier, la taille, la date de modification, etc. Il permet de trouver des fichiers en fonction de leurs attributs.

**Syntaxe de base :**
```bash
find répertoire -options critères
```

Exemple :
```bash
find /chemin/vers/repertoire -name "nom_du_fichier.txt"
```

`find` peut être combiné avec plusieurs options pour effectuer des recherches complexes. Par exemple, vous pouvez rechercher des fichiers de taille spécifique, des fichiers modifiés dans une plage de temps donnée, etc.

**Différences et utilisations :**

- `grep` est principalement utilisé pour rechercher du contenu dans les fichiers texte. Il se concentre sur les motifs à l'intérieur des fichiers.
- `find` est utilisé pour rechercher des fichiers en fonction de leurs attributs, comme le nom du fichier, la taille, les permissions, etc. Il est utile pour trouver des fichiers qui correspondent à certains critères.

En résumé, utilisez `grep` lorsque vous souhaitez rechercher des lignes de texte correspondant à un motif particulier à l'intérieur des fichiers. Utilisez `find` lorsque vous voulez rechercher des fichiers en fonction de leurs attributs tels que le nom, la taille ou la date de modification.


## Vim : faire des recherches de mots ?

Dans l'éditeur de texte Vim, vous pouvez effectuer des recherches de mots à l'aide de la commande `/`. Voici comment faire des recherches de mots dans Vim :

1. **Ouvrir un fichier dans Vim :**
   Pour ouvrir un fichier dans Vim, ouvrez votre terminal et entrez :
   ```bash
   vim nom_du_fichier
   ```

2. **Rechercher un mot :**
   Une fois dans Vim, vous pouvez commencer une recherche en mode normal (c'est-à-dire en appuyant sur la touche `Esc` si vous n'êtes pas déjà en mode normal) et en utilisant la commande `/`. Ensuite, saisissez le mot que vous souhaitez rechercher et appuyez sur `Entrée`. Par exemple, pour rechercher le mot "recherche", entrez :
   ```
   /recherche
   ```

   Vim va mettre en surbrillance la première occurrence du mot "recherche" dans le fichier.

3. **Naviguer dans les résultats :**
   Une fois que vous avez effectué une recherche, vous pouvez utiliser les touches `n` et `N` pour naviguer entre les résultats. La touche `n` vous emmène vers la prochaine occurrence du mot recherché, tandis que la touche `N` vous emmène vers l'occurrence précédente.

4. **Quitter le mode de recherche :**
   Pour quitter le mode de recherche et revenir au mode normal, appuyez sur `Esc`.

5. **Rechercher et remplacer :**
   En plus de rechercher des mots, Vim permet également de remplacer des mots dans un fichier. Pour ce faire, vous pouvez utiliser la commande `:%s/ancien_mot/nouveau_mot/g`, où "ancien_mot" est le mot que vous souhaitez remplacer et "nouveau_mot" est le mot de remplacement. Le `g` à la fin de la commande signifie que le remplacement doit être effectué globalement (pour toutes les occurrences du mot).

   Par exemple, pour remplacer toutes les occurrences du mot "vieux" par "nouveau", utilisez la commande :
   ```
   :%s/vieux/nouveau/g
   ```

6. **Rechercher en arrière :**
   Pour rechercher en arrière dans un fichier, utilisez la commande `?` au lieu de `/`. Par exemple, pour rechercher le mot "recherche" en arrière, entrez :
   ```
   ?recherche
   ```

Ces commandes de recherche sont très utiles pour naviguer et éditer efficacement dans Vim.


## Vim : afficher les numéros de lignes ?

Pour afficher les numéros de lignes dans l'éditeur de texte Vim, vous pouvez activer cette fonctionnalité en utilisant la commande `:set number` ou son équivalent court `:set nu`.

Voici comment faire pour afficher les numéros de lignes dans Vim :

1. Ouvrez un fichier dans Vim en utilisant la commande suivante dans votre terminal :
   
   ```bash
   vim nom_du_fichier
   ```

2. Une fois dans Vim, assurez-vous d'être en mode normal en appuyant sur la touche `Esc`.

3. Pour activer l'affichage des numéros de lignes, tapez l'une des commandes suivantes dans le mode normal et appuyez sur `Entrée` :

   ```bash
   :set number
   ```
   ou
   
   ```bash
   :set nu
   ```

   Les numéros de lignes seront affichés à gauche de chaque ligne du fichier.

4. Pour désactiver l'affichage des numéros de lignes, vous pouvez utiliser la commande `:set nonumber` ou `:set nonu`.

   ```bash
   :set nonumber
   ```
   ou
   
   ```bash
   :set nonu
   ```

   Cela supprimera les numéros de lignes de l'affichage.

5. Pour enregistrer vos modifications et quitter Vim, appuyez sur `Esc` pour passer en mode normal, puis tapez `:wq` suivi de la touche `Entrée`.

L'affichage des numéros de lignes dans Vim est particulièrement utile pour se repérer dans un fichier et pour référencer des lignes spécifiques lors de l'édition.


# WINDOWS

## Gestion carte réseau sous workstation pro, nat, bridge, host only...

Dans VMware Workstation Pro, vous pouvez configurer différentes méthodes de gestion de la carte réseau de vos machines virtuelles (VMs) pour les connecter au réseau physique et aux autres machines virtuelles. Les trois modes principaux de gestion de la carte réseau dans VMware Workstation Pro sont : NAT, Bridge et Host-Only.

1. **NAT (Network Address Translation)** :
   Dans le mode NAT, votre machine virtuelle est connectée à un réseau privé virtuel. La machine virtuelle partage l'adresse IP de votre ordinateur hôte via un processus de traduction d'adresse (NAT). Cela permet à la machine virtuelle d'accéder à Internet et aux ressources du réseau local de votre hôte. Cependant, les autres machines de votre réseau ne peuvent pas accéder directement à la machine virtuelle.

   Ce mode est utile lorsque vous souhaitez fournir un accès à Internet à vos VMs, mais vous ne voulez pas qu'elles soient directement visibles sur le réseau.

2. **Bridge (Pont)** :
   Dans le mode Bridge, la machine virtuelle utilise la carte réseau physique de votre ordinateur hôte pour se connecter directement au réseau local. Cela signifie que la machine virtuelle obtient sa propre adresse IP sur le réseau local et peut être vue par d'autres machines du réseau comme si elle était un ordinateur physique distinct.

   Le mode Bridge est utile lorsque vous voulez que vos VMs soient directement accessibles sur le réseau local, comme si elles étaient des machines physiques.

3. **Host-Only (Hôte seulement)** :
   Le mode Host-Only crée un réseau virtuel isolé entre toutes les machines virtuelles et l'hôte. Les VMs peuvent communiquer entre elles et avec l'hôte, mais elles n'ont pas accès au réseau local ni à Internet.

   Ce mode est utile pour des scénarios où vous voulez créer un environnement isolé pour le développement ou les tests.

Chaque mode de gestion de carte réseau a ses avantages et ses cas d'utilisation spécifiques. Le choix dépend de vos besoins et de la manière dont vous souhaitez configurer vos machines virtuelles dans votre environnement. Lorsque vous créez ou configurez une VM dans VMware Workstation Pro, vous pouvez sélectionner le mode de gestion de carte réseau approprié en fonction de vos besoins spécifiques.


## Licence oem, retail, KMS/MAK, c'est quoi ?

Les termes mentionnés - licence OEM, licence Retail, KMS (Key Management Service) et MAK (Multiple Activation Key) - sont tous liés à la manière dont les licences logicielles sont gérées et distribuées dans le contexte du système d'exploitation Windows de Microsoft. Chacun de ces types de licences a ses propres caractéristiques et conditions d'utilisation. Voici ce que chacun d'entre eux signifie :

1. **Licence OEM (Original Equipment Manufacturer)** :
   Une licence OEM est généralement fournie avec un nouvel ordinateur lors de l'achat. Elle est liée au matériel spécifique sur lequel elle a été préinstallée par le fabricant (OEM). Ces licences ne peuvent pas être transférées d'un ordinateur à un autre. Elles sont généralement moins chères que les autres types de licences, mais elles sont également plus restrictives en termes de transférabilité.

2. **Licence Retail** :
   Une licence Retail est conçue pour les utilisateurs finaux individuels. Elle peut être achetée séparément et installée sur un ordinateur. Contrairement à une licence OEM, elle peut être transférée d'un ordinateur à un autre, mais uniquement sur un seul ordinateur à la fois. Si vous achetez un nouvel ordinateur, vous ne pouvez pas transférer la licence Retail de l'ancien ordinateur vers le nouveau et continuer à utiliser les deux en même temps.

3. **KMS (Key Management Service)** :
   Le KMS est un service de gestion de clés utilisé par les grandes organisations pour activer un grand nombre de machines sous Windows. Plutôt que d'activer chaque machine individuellement, le KMS permet d'activer automatiquement les machines en se connectant périodiquement au serveur KMS de l'organisation. Cette méthode est couramment utilisée pour les déploiements en entreprise.

4. **MAK (Multiple Activation Key)** :
   Le MAK est une autre méthode d'activation en volume pour les organisations. Contrairement au KMS, où les machines se connectent au serveur KMS, un MAK utilise une clé d'activation spécifique pour chaque machine. Chaque clé MAK a un nombre limité d'activations autorisées, généralement lié au contrat de licence.

En résumé, ces différents types de licences et méthodes d'activation sont utilisés pour gérer la distribution et l'utilisation légale du système d'exploitation Windows. Les licences OEM et Retail sont plus adaptées aux utilisateurs individuels, tandis que les méthodes KMS et MAK sont conçues pour les organisations qui gèrent un grand nombre de machines. Il est important de respecter les termes de licence appropriés pour chaque type de licence afin de rester en conformité avec les règles de Microsoft.


## Quel outil pour voir le journal des événements système ?

Pour afficher le journal des événements système dans Windows, vous pouvez utiliser l'outil "Observateur d'événements" (Event Viewer). Cet outil est intégré à Windows et vous permet de visualiser et d'analyser les journaux d'événements enregistrés par le système d'exploitation et les applications.

Voici comment ouvrir l'Observateur d'événements et accéder au journal des événements système :

1. **Ouverture de l'Observateur d'événements** :
   Vous pouvez ouvrir l'Observateur d'événements de plusieurs manières, dont les suivantes :
   
   - Appuyez sur les touches `Windows + R` pour ouvrir la boîte de dialogue "Exécuter". Tapez `eventvwr.msc` et appuyez sur Entrée.
   - Recherchez "Observateur d'événements" dans le menu Démarrer et cliquez dessus pour lancer l'application.

2. **Navigation vers le journal des événements système** :
   Une fois l'Observateur d'événements ouvert, vous verrez une structure arborescente dans la colonne de gauche. Développez "Journaux Windows" pour voir différents types de journaux, dont "Système".

3. **Affichage des événements système** :
   Cliquez avec le bouton droit sur "Système" dans la colonne de gauche et choisissez "Toutes les tâches" > "Afficher les journaux" pour afficher les événements enregistrés dans le journal des événements système.

   Vous verrez la liste des événements système enregistrés, tels que les erreurs, les avertissements et les informations.

4. **Filtrage et recherche d'événements** :
   Vous pouvez utiliser les options de filtrage et de recherche pour cibler des événements spécifiques en fonction de la date, du type d'événement, des sources, etc.

5. **Visualisation des détails de l'événement** :
   Double-cliquez sur un événement pour afficher ses détails, y compris la description, la source, la date et l'heure, etc.

L'Observateur d'événements est un outil puissant pour diagnostiquer les problèmes système, surveiller les performances et suivre les activités du système. Cependant, la compréhension des événements peut nécessiter une certaine expertise, car certains messages peuvent être techniques et complexes.


## Dans quel fichier sont stockés les utilisateurs locaux ?

Sous Windows, les informations sur les utilisateurs locaux sont stockées dans une base de données appelée le "Registre" (Registry). Le Registre est une base de données hiérarchique utilisée par Windows pour stocker les paramètres, les configurations et les informations système.

Plus précisément, les détails des utilisateurs locaux, tels que les noms d'utilisateur, les mots de passe hachés (en utilisant des mécanismes de hachage et de chiffrement), les groupes auxquels ils appartiennent et d'autres paramètres associés, sont stockés dans le Registre sous la clé :

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList
```

Il est important de noter que les informations stockées dans le Registre sont généralement cryptées et protégées pour des raisons de sécurité. L'accès au Registre nécessite généralement des privilèges administratifs, car la modification incorrecte des données peut avoir un impact important sur le système.

Si vous cherchez à gérer les utilisateurs locaux, il est recommandé d'utiliser les outils et les interfaces utilisateur fournis par Windows, tels que l'interface graphique de gestion des utilisateurs dans le Panneau de configuration ou la console de gestion des utilisateurs "``lusrmgr.msc``". Ces outils permettent de gérer les comptes utilisateurs de manière plus sécurisée et conviviale.

## Comment activer le bureau a distance puis autoriser un utilisateur nommé "hk" (par exemple) a se connecter dessus ?

### Via l'interface graphique :

Pour activer le Bureau à distance et autoriser un utilisateur spécifique à s'y connecter sur un ordinateur Windows, suivez ces étapes :

1. **Activer le Bureau à distance :**

   a. Cliquez avec le bouton droit sur l'icône "Ce PC" (ou "Ordinateur" sur les versions plus anciennes de Windows) sur le bureau ou dans le menu Démarrer, puis sélectionnez "Propriétés".

   b. Dans la fenêtre "Propriétés système", cliquez sur "Paramètres système avancés" dans le volet de gauche.

   c. Dans l'onglet "Avancé", sous la section "Performances", cliquez sur "Paramètres...".

   d. Dans l'onglet "Avancé", sous la section "Utilisation à distance", cochez l'option "Autoriser les connexions Bureau à distance vers cet ordinateur".

2. **Autoriser un utilisateur à se connecter via le Bureau à distance :**

   a. Après avoir activé le Bureau à distance, cliquez sur le bouton "Sélecteurs distants" dans la section "Utilisation à distance" de la fenêtre "Propriétés système".

   b. Dans la fenêtre "Sélecteurs distants", cliquez sur "Ajouter..." pour sélectionner les utilisateurs qui sont autorisés à se connecter via le Bureau à distance.

   c. Tapez le nom d'utilisateur dans la zone de texte, cliquez sur "Vérifier noms" pour vous assurer que le nom d'utilisateur est correct, puis cliquez sur "OK" pour fermer la fenêtre de sélection d'utilisateurs.

   d. Dans la fenêtre "Sélecteurs distants", le nom d'utilisateur que vous avez ajouté apparaîtra dans la liste. Assurez-vous qu'il est coché, puis cliquez sur "OK" pour fermer la fenêtre.

3. **Appliquer les changements et redémarrer si nécessaire :**

   Après avoir ajouté l'utilisateur et activé le Bureau à distance, assurez-vous d'enregistrer les modifications et redémarrez l'ordinateur si cela vous est demandé pour que les modifications prennent effet.

Une fois ces étapes terminées, l'utilisateur "hk" sera autorisé à se connecter au Bureau à distance de l'ordinateur. Assurez-vous que l'utilisateur possède un mot de passe sécurisé, car les connexions Bureau à distance impliquent des problèmes de sécurité importants.

### En ligne de commande :

Voici comment activer le Bureau à distance et autoriser un utilisateur à s'y connecter en utilisant des commandes en ligne de commande dans Windows. Assurez-vous d'exécuter ces commandes avec des privilèges d'administrateur.

1. **Activer le Bureau à distance :**

   Pour activer le Bureau à distance, vous pouvez utiliser la commande `reg add` pour modifier la base de registre. Ouvrez une fenêtre de commande avec des privilèges d'administrateur et exécutez la commande suivante :

   ```bash
   reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
   ```

2. **Autoriser un utilisateur à se connecter via le Bureau à distance :**

   Pour autoriser un utilisateur spécifique à se connecter via le Bureau à distance, vous pouvez utiliser la commande `net localgroup` pour ajouter cet utilisateur au groupe "Utilisateurs du Bureau à distance". Exécutez la commande suivante :

   ```bash
   net localgroup "Utilisateurs du Bureau à distance" "nom_du_computer\nom_utilisateur" /add
   ```

   Remplacez "nom_du_computer" par le nom de votre ordinateur et "nom_utilisateur" par le nom de l'utilisateur que vous souhaitez autoriser.

3. **Redémarrer le service de Bureau à distance :**

   Pour que les modifications prennent effet, vous devrez peut-être redémarrer le service de Bureau à distance. Exécutez la commande suivante pour redémarrer le service :

   ```bash
   net stop termservice && net start termservice
   ```

Une fois ces étapes terminées, l'utilisateur spécifié sera autorisé à se connecter via le Bureau à distance sur l'ordinateur. Assurez-vous de suivre les bonnes pratiques de sécurité en matière de configuration du Bureau à distance et de gestion des utilisateurs.


## Pare-feu Windows : comment autoriser un ping ?

Pour autoriser les requêtes Ping (ICMP) à travers le pare-feu Windows, vous pouvez utiliser les commandes en ligne de commande ou l'interface utilisateur du Pare-feu Windows. Voici comment faire :

**Méthode 1 : Utilisation de l'interface utilisateur du Pare-feu Windows**

1. Ouvrez le Panneau de configuration.
2. Accédez à la section "Système et sécurité", puis cliquez sur "Pare-feu Windows".
3. Dans le volet de gauche, cliquez sur "Paramètres avancés".
4. Dans la fenêtre "Pare-feu Windows avec fonctions de sécurité avancées", cliquez sur "Règles de trafic entrant".
5. Dans le volet de droite, cliquez sur "Nouvelle règle..." pour démarrer l'Assistant Nouvelle règle de sécurité.
6. Sélectionnez "Personnalisée" et cliquez sur "Suivant".
7. Cochez la case "Ce programme de chemin d'accès", puis cliquez sur "Suivant".
8. Dans la page "Quels programmes voulez-vous autoriser ?", laissez les options par défaut ou spécifiez "Tous les programmes" si vous souhaitez autoriser le Ping depuis n'importe quel programme. Cliquez sur "Suivant".
9. Sélectionnez "Cela protocole : ICMPv4" et cochez la case "Autoriser la connexion". Cliquez sur "Suivant".
10. Choisissez "Quels types de sources de port voulez-vous autoriser ?", laissez l'option par défaut "Tous" ou spécifiez les sources de votre choix. Cliquez sur "Suivant".
11. Donnez un nom à la règle (par exemple, "Autoriser le Ping") et ajoutez une description si nécessaire. Cliquez sur "Suivant".
12. Révisez les paramètres de la règle et cliquez sur "Terminer" pour créer la règle.

**Méthode 2 : Utilisation de commandes en ligne de commande**

Ouvrez une fenêtre de commande avec des privilèges d'administrateur et exécutez la commande suivante pour autoriser le Ping à travers le pare-feu :

```bash
netsh advfirewall firewall add rule name="Autoriser le Ping" protocol=icmpv4:8,any dir=in action=allow
```

Cela ajoute une règle au pare-feu pour autoriser les requêtes Ping entrantes.

Après avoir suivi l'une de ces méthodes, les requêtes Ping devraient être autorisées à travers le pare-feu Windows, et vous devriez pouvoir Pinguer votre ordinateur à partir d'autres appareils du réseau. Assurez-vous toujours de prendre en compte les considérations de sécurité appropriées lors de la configuration de règles de pare-feu.

## Une ip en 169.254, c'est bon signe ?

Non, une adresse IP en plage ``169.254.x.x`` n'est généralement pas un bon signe. Les adresses IP dans la plage 169.254.x.x sont automatiquement attribuées par le système d'exploitation lorsqu'il ne peut pas obtenir une adresse IP valide via un serveur DHCP (Dynamic Host Configuration Protocol).

Cette plage d'adresses IP est connue sous le nom d'"``APIPA``" (Automatic Private IP Addressing) et est utilisée lorsque votre appareil tente de se connecter à un réseau mais ne parvient pas à obtenir une adresse IP valable. Cela peut se produire lorsque le serveur DHCP est indisponible ou que la configuration réseau est incorrecte.

En bref, une adresse IP en plage 169.254.x.x indique que votre appareil n'a pas réussi à obtenir une adresse IP valide via le réseau, ce qui peut entraîner des problèmes de connectivité. Pour résoudre ce problème, vous devrez généralement vérifier votre configuration réseau, vous assurer que le serveur DHCP est accessible et fonctionne correctement, et que votre appareil est correctement configuré pour obtenir une adresse IP automatiquement via DHCP.


## Une gateway c'est vraiment utile ?

Oui, une passerelle (gateway en anglais) est un élément essentiel dans une infrastructure réseau et joue un rôle crucial pour permettre la connectivité entre différents réseaux. Voici pourquoi une passerelle est vraiment utile :

1. **Routage entre réseaux :** Une passerelle permet de faire transiter les données entre différents réseaux, qu'il s'agisse de réseaux locaux (LAN) ou de réseaux étendus (WAN). Elle joue un rôle clé dans le routage des paquets de données d'un réseau à un autre.

2. **Accès à Internet :** Dans un réseau domestique ou professionnel, la passerelle est souvent utilisée pour fournir un accès à Internet. Toutes les données provenant des dispositifs connectés passent par la passerelle avant d'atteindre Internet et vice versa.

3. **Gestion du trafic :** Les passerelles peuvent prendre en charge des fonctionnalités de gestion du trafic, telles que le contrôle de bande passante, la priorisation du trafic et la mise en place de règles de sécurité pour filtrer ou bloquer certaines données.

4. **Sécurité :** Les passerelles peuvent inclure des pare-feu, des systèmes de détection d'intrusion (IDS) et d'autres mécanismes de sécurité pour protéger le réseau local contre les menaces provenant d'Internet ou d'autres réseaux.

5. **Interconnexion de réseaux d'entreprise :** Dans le contexte des entreprises, les passerelles sont utilisées pour interconnecter des réseaux locaux distincts, tels que différents bureaux, succursales ou centres de données. Elles permettent aux employés de différents sites de communiquer et d'accéder aux ressources partagées.

6. **VPN (Virtual Private Network) :** Les passerelles VPN permettent de créer des connexions sécurisées entre des réseaux distants ou des utilisateurs éloignés. Cela permet un accès sécurisé aux ressources internes de l'entreprise, même à partir de réseaux publics comme Internet.

En résumé, une passerelle est un élément fondamental pour assurer la connectivité, la communication et la sécurité entre différents réseaux. Elle joue un rôle central dans la gestion du trafic, la sécurité des données et la facilitation de l'accès à Internet et aux ressources réseau.


## Droit de sécurité sur un repertoire, acl

Les droits de sécurité sur un répertoire, également connus sous le nom de contrôle d'accès (ACL - Access Control List en anglais), sont utilisés pour définir les niveaux d'accès et les permissions que les utilisateurs et les groupes ont sur ce répertoire et son contenu. Les ACL permettent de spécifier qui peut lire, écrire, exécuter ou effectuer d'autres opérations sur les fichiers et les sous-répertoires à l'intérieur du répertoire en question.

Voici comment fonctionnent les ACL et comment elles sont gérées :

1. **Liste de contrôle d'accès (ACL) :**
   Une ACL est une liste structurée qui associe des utilisateurs et des groupes avec des permissions spécifiques sur un objet, comme un répertoire. Chaque entrée dans l'ACL (appelée une "entrée ACL") répertorie un utilisateur ou un groupe et les permissions qui leur sont attribuées.

2. **Permissions :**
   Les permissions typiques incluent :
   - Lecture (Read) : Autorise la consultation du contenu des fichiers et répertoires.
   - Écriture (Write) : Autorise la modification ou la création de nouveaux fichiers et répertoires.
   - Exécution (Execute) : Autorise l'exécution de fichiers ou l'accès à des répertoires.
   - Listage (List) : Autorise la visualisation du contenu d'un répertoire.

3. **Gestion des ACL :**
   Les ACL peuvent être gérées à l'aide d'outils de ligne de commande ou d'interfaces graphiques, en fonction du système d'exploitation que vous utilisez. Par exemple, sur Linux, la commande `chmod` peut être utilisée pour gérer les ACL, tandis que sur Windows, l'interface graphique des propriétés de fichiers permet de gérer les autorisations.

4. **Héritage des autorisations :**
   Les autorisations d'un répertoire peuvent être transmises aux fichiers et aux sous-répertoires qu'il contient, dans le cas de l'héritage des autorisations. Cela signifie que les autorisations définies au niveau d'un répertoire parent peuvent être automatiquement appliquées aux éléments enfants, sauf si elles sont explicitement modifiées.

5. **Meilleures pratiques de sécurité :**
   Il est important de suivre les meilleures pratiques de sécurité lors de la configuration des ACL. Cela implique de donner des autorisations strictement nécessaires aux utilisateurs et aux groupes, de limiter l'accès aux ressources sensibles et de mettre en œuvre une politique de moindre privilège.

Les ACL sont un moyen puissant de gérer la sécurité des fichiers et répertoires, permettant un contrôle fin sur qui peut accéder à quelles ressources et ce qu'ils peuvent faire avec ces ressources.


