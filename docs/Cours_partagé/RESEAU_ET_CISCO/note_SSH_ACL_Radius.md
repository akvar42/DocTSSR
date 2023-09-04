## En résumé

### Sécurisation des Routeurs avec Mots de Passe

Il est possible de créer des mots de passe pour sécuriser l’accès de vos routeurs. Ces mots de passe peuvent être uniques ou différents pour chaque utilisateur.

#### Types de lignes (line) d'entrée du routeur

1. **CTY** pour les ports console.
2. **AUX** pour les ports auxiliaires.
3. **TTY** pour les ports asynchrones.
4. **VTY** pour les ports virtuels (SSH).

#### Créer un Mot de Passe Unique

Pour créer un mot de passe unique, entrez en mode configuration-line :

```bash
routeur1(config)#line con 0
routeur1(config-line)#password motDePasse
routeur1(config-line)#login
```

#### Créer un Mot de Passe pour un Utilisateur Spécifique

Pour créer un mot de passe associé à un utilisateur :

```bash
routeur1(config)#username root secret motDePasse
routeur1(config)#line con 0
routeur1(config-line)#login local
```

### Utilisation de SSH pour une Connexion Sécurisée

La façon la plus sécurisée de se connecter aux routeurs est d'utiliser SSH.

1. **Créer un nom de domaine :**

    ```bash
    routeur1(config)#ip domain-name mondomain.lan
    ```

2. **Générer une paire de clés publiques/privées :**

    ```bash
    routeur1(config)#crypto key generate rsa
    ```

3. **Spécifier la version de SSH :**

    ```bash
    routeur1(config)#ip ssh version 2
    ```

4. **Configurer les lignes VTY pour utiliser SSH :**

    ```bash
    routeur1(config)#line vty 0 4
    routeur1(config-line)#transport input ssh
    routeur1(config-line)#login local
    ```
## Les ACL (Listes de Contrôle d'Accès)

Les ACL vous permettent de créer des règles autorisant ou interdisant l'accès à un réseau.

### Types d'ACL

1. **Standards** : Ces ACL permettent de configurer la source et doivent être placées au plus près de la destination.
2. **Étendues** : Ces ACL permettent de renseigner la source, la destination, ainsi que le port et doivent être placées au plus près de la source.

### Règles des ACL

- Les ACL peuvent soit autoriser, soit interdire un réseau.
- Une fois créée, l'ACL doit être associée à une interface.
- Les règles se lisent de haut en bas, l'ordre a donc une importance.
- Les règles les plus précises doivent être placées en haut et les plus générales en bas.

#### Création d'une ACL Standard

Pour créer une ACL standard :

```bash
routeur(config)#access-list n°1-99 deny/permit réseau masqueInversé
```

#### Création d'une ACL Étendue

Pour créer une ACL étendue :

```bash
routeur(config)#access-list n°100-199 deny/permit protocole réseauSource masqueInversé réseauDestination masqueInversé n°port
```

### ACL avec Nom

Ces deux types d’ACL peuvent être renseignés par un nom au lieu d’utiliser un numéro :

```bash
routeur(config)#ip access-list standard/extended Nom
routeur(config-ext-nacl)#deny/permit protocol réseauSource masqueInversé réseauDestination masqueInversé n°port
```
## RADIUS (Remote Authentication Dial-In User Service)

RADIUS vous permet de centraliser vos identifiants et mots de passe. Il s’agit d’un protocole client/serveur où le serveur RADIUS gère les authentifications pour ses clients comme les routeurs et les switchs.

### Caractéristiques de RADIUS

RADIUS est un protocole AAA, ce qui signifie :

1. **Authentification** : vérification des identités.
2. **Autorisation** : détermination des ressources accessibles.
3. **Accounting (compte)** : suivi de l'utilisation des ressources.

### Configuration de RADIUS sur un serveur

Pour configurer RADIUS, il faut créer sur le serveur :

- Un client
- Un utilisateur

### Configuration de RADIUS sur les appareils CISCO

#### Activer AAA

Pour activer AAA :

```bash
routeur2(config)# aaa new-model
```

#### Configurer le serveur RADIUS

Pour configurer le serveur RADIUS :

```bash
routeur2(config)# radius-server host 223.0.2.8 key Cisco1234
```

#### Créer un groupe RADIUS

Pour créer un groupe RADIUS :

```bash
routeur2(config)# aaa authentication login default group radius local
```

#### Associer le groupe à une ligne

Pour associer le groupe à une ligne :

```bash
routeur2(config)# line vty 0 15
routeur2(configure-line)# login authentication default
```
