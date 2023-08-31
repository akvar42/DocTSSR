## Commandes IOS utiles

```

#show ip arp
#ping [ip | ipv6] {ip ou hostname}
#traceroute [ip | ipv6] {ip ou hostname}
#show cdp neighbors [detail]
```

- et bien d'autres commandes détaillées dans le PDF...

## Configuration de base

```
(config)#hostname nom

(config)#banner motd #message#
(config)#no ip domain-lookup
(config-line)#logging synchronous
```

- Définir le nom d'hôte
- Définir une bannière de connexion
- Désactiver la résolution DNS des noms inconnus
- Synchroniser l'affichage des logs

## Gestion des fichiers

```
#show version
#show file systems
#show {startup-config | running-config}
#erase {nvram: | startup-config}
(config)#boot system {flash: | rom}
#reload
```

- Afficher infos matérielleslogicielles
- Lister les systèmes de fichiers
- Afficher les configs en cours ou de démarrage
- Effacer le fichier de config de démarrage
- Choisir l'image à charger au démarrage
- Redémarrer le périphérique

## Interface réseau

```
#show interfaces [int-type int-num]
(config)#interface int-type int-num
(config-if)#{no} {ip | ipv6} address
(config-if)#description texte

(config-if)#{no} shutdown
```

- Voir infosconfig d'une interface

- Entrer dans le mode de config d'une interface
- Configurersupprimer une adresse IP
- Ajouter une description
- Activerdésactiver une interface

## Sécurité

```
(config)#line {console | vty}

(config-line)#password motdepasse
(config-line)#login
(config)#enable secret motdepasse
(config)#service password-encryption
(config)#security passwords min-length valeur
```

- Accéder à la config des lignes consoleVTY
- Définir des mots de passe
- Activer la demande de login
- Définir un enable secret

- Chiffrer les mots de passe en clair
- Imposer une longueur minimale pour les mots de passe

## Diagnostic et débogage

```

#debug ip icmp
#undebug {all | ip icmp}
#terminal {monitor | no monitor}
```

- Activer le débogage ICMP
- Désactiver le débogage ICMP ou tous
- Affichermasquer les messages de débogage sur TelnetSSH
- ## Configuration du commutateur

```
(config-if)#duplex {full | half | auto}

(config-if)#speed {10 | 100 | 1000 | auto}
(config-if)#mdix auto
#show controllers ethernet-controller intf phy
```

- Définir le mode duplex d'un port

- Définir la vitesse en Mbps d'un port
- Activer la détection auto MDIXMDI d'un port
- Afficher les paramètres physiques d'un port

## Types de commutation

- Store and forward : stocke les trames entières et vérifie le FCS avant retransmission
- Cut through : retransmet sans vérifier le FCS, réduit la latence mais risque d'erreurs

- Fragment free : ne stocke que les 64 premiers octets et vérifie le FCS

## Adressage IP d'un commutateur

```
(config)#interface vlan vlan-id
(config-if)#ip address adresse masque
(config)#ip default-gateway adresse
#show running-config interface [int-type int-num]
```

- Créer l'interface SVI d'un VLAN

- Configurer l'adresse IP (et masque) de la SVI
- Définir la passerelle par défaut
- Voir la config détaillée d'une interface

## Routage IPv6 sur un commutateur

```
(config)#sdm prefer dual-ipv4-and-ipv6 default
(config)#ipv6 unicast-routing

(config-if)#ipv6 address autoconfig
#show ipv6 routers
```

- Activer la pile IPv6

- Activer le routage IPv6 et envoyer des RA
- Config auto d'une adresse GUA par SLAAC
- Voir les infos RA reçues

## Sécurisation d'un commutateur

```
(config)#no cdp run

(config-if)#no cdp enable
#auto secure [management | forwarding]
#show ip ports all
#show control-plane host open-ports
```

- Désactiver CDP globalement
- Désactiver CDP sur une interface
- Activer AutoSecure
- Voir les ports TCP ouverts (IOS-XE ou IOS)