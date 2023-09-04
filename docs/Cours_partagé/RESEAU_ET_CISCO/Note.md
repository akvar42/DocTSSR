# Résumé des Commandes pour la Configuration du Matériel Cisco

## Modes de la CLI Cisco
- Mode Utilisateur
- Mode Privilège
- Mode Configuration Globale
- Mode Configuration d'Interfaces
- Mode Configuration du Routage
- Mode Configuration de Ligne

### Commandes de Base
```bash
exit
```

## Configuration du Routeur

### Ajout d'un Hostname
```bash
hostname NomduRouteur
```

### Vérification de la Configuration
```bash
show running-config
```

## Fonctionnalités de la CLI
- Autocomplétion
- Historique de Commandes
- Aide en Ligne

## Configuration des Interfaces
```bash
interface nom_de_l_interface
ip address XXX.XXX.XXX.XXX XXX.XXX.XXX.XXX
no shutdown
```

## Sauvegarde de Configuration
```bash
copy running-config startup-config
```

## Switchs et VLANs

### Configuration de VLAN
```bash
vlan vlan-id
name vlan-name
switchport access vlan vlan-id
show running-config vlan [ vlan_id ]
show vlan brief
```

## Configuration des Protocoles
- DHCP
- NTP
- NAT

### DHCP
```bash
ip dhcp pool nomDuPool
network adresse masque
default-router adresseDeLInterface
```

### NTP
```bash
ntp server adresseNTPServeur
```

### NAT
```bash
ip route 0.0.0.0 0.0.0.0 adresseGateway
```

## Spanning Tree Protocol (STP)
```bash
show spanning-tree
```

## Protocoles de Routage
- OSPF
- EIGRP

### Configuration d'EIGRP
```bash
interface gi0/0/0
ip address 192.168.0.254 255.255.255.0
no shutdown
```
## Lancer OSPF

Pour initialiser OSPF, utilisez la commande suivante :

```bash
routeur(config)# router ospf n°DeProcess  
```
**Note :** Ne pas confondre avec le numéro d’area.

Ensuite, pour chaque routeur, ajoutez tous les réseaux qui doivent être gérés par OSPF :

```bash
routeur2(config-router)# network adresseIP masqueInversé area n°Area  
```
> Seuls les réseaux privés ne doivent pas être communiqués à OSPF.

### Vérifier la Configuration OSPF

Pour voir l'ID du routeur et les réseaux sur lesquels il est configuré, utilisez :

```bash
sh ip protocols  
```

Pour voir les voisins OSPF et l'état des liaisons, utilisez :

```bash
show ip ospf neighbor  
```

## Configurer un ABR (Area Border Router)

Un ABR est un routeur qui fait le lien entre deux zones OSPF. Ajoutez les réseaux et les zones auxquels il est connecté :

```bash
routeur(config-router)# network adresseIP masqueInversé area n°Area
```

> Tous les ABR doivent être reliés à la zone 0.

## Configurer un ASBR (Autonomous System Border Router)

Un ASBR est un routeur qui relie deux AS différents, que ce soit OSPF ou un autre protocole. Ce lien est établi via BGP.

```

