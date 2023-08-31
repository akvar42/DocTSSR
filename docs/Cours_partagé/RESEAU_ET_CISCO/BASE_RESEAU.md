## Structure des adresses MAC

- 48 bits
- 24 bits pour l'ID unique du constructeur

- 24 bits pour l'ID unique du périphérique
- 1 bit pour définir si l'adresse est de diffusion ou unicast

- 1 bit pour définir si l'adresse est locale ou globale

## Structure de la trame Ethernet 802.3

- Préambule (7 octets)

- Délimiteur de début de trame (1 octet)
- Adresse MAC destination (6 octets)

- Adresse MAC source (6 octets)
- Longueur/Type (2 octets)
- Données (46 à 1500 octets)
- Séquence de contrôle de trame FCS (4 octets)

Le champ FCS permet de détecter des erreurs lors de la transmission. L'émetteur calcule un CRC avant l'envoi, le receveur recalcule le CRC à la réception et compare les deux résultats.

## Domaines de diffusion et de collision

- Domaine de diffusion : zone du réseau où un broadcast est reçu par toutes les interfaces. Délimité par routeur ou VLAN.
- Domaine de collision : zone du réseau où une trame envoyée par une interface peut entrer en collision avec celle d'une autre interface du domaine. Tous les ports d'un hub sont dans le même domaine, chaque port d'un switch est dans un domaine différent.

## Méthodes d'accès CSMA/CD et CSMA/CA

- CSMA/CD (Ethernet filaire) : écoute du support avant émission, en cas de collision détectée tous les périphériques arrêtent et réémettent plus tard.
- CSMA/CA (Ethernet sans fil) : écoute du support avant émission, envoi d'une notification d'intention d'émettre avant effectivement d'émettre une fois autorisé.

## Adressage IPv4

- Unicast : 1 émetteur vers 1 récepteur
- Multicast : 1 émetteur vers multiples récepteurs inscrits à un groupe

- Broadcast : 1 émetteur vers tous les récepteurs du réseau local

## Classes d'adresses IPv4

- Classe A : 0.0.0.0 à 127.255.255.255, masque /8, 16M d'adresses hôtes

- Classe B : 128.0.0.0 à 191.255.255.255, masque /16, 65k adresses hôtes
- Classe C : 192.0.0.0 à 223.255.255.255, masque /24, 254 adresses hôtes
- Classe D : 224.0.0.0 à 239.255.255.255, adresses multicast
- Classe E : 240.0.0.0 à 255.255.255.255, adresses réservées

## Adresses IPv4 privées (RFC 1918)

- Classe A : 10.0.0.0/8
- Classe B : 172.16.0.0/12
- Classe C : 192.168.0.0/16

## Adresses IPv4 réservées

- 127.0.0.0/8 : adresses de bouclage
- 169.254.0.0/16 : adresses APIPA

- 192.0.2.0/24 : adresses de test

## Structure d'une adresse IPv4

- 4 octets (32 bits)
- Séparés en réseau/sous-réseau/hôte selon le masque
- Exemple :
- Adresse : 192.168.54.147/27

- Masque : 255.255.255.224 (/27)
- Réseau : 192.168.54.128/27
- 1ère adresse hôte : 192.168.54.129
- Dernière adresse hôte : 192.168.54.158
- Broadcast : 192.168.54.159

## Adressage IPv6

### Types d'adresses

- GUA : globale, équivalent d'une publique IPv4
- LLA : locale au lien, équivalent APIPA 169.254.x.y/16

- ULA : locale unique, équivalent privé RFC1918
- Multicast : similaire à 224.0.0.0/8 en IPv4

### Règles de simplification

- Supprimer les 0 initiaux dans un groupe de 4 chiffres
- Remplacer un groupe de 0 par :: (une seule fois par adresse)

### Caractéristiques des annonces RA du routeur

- Envoyées toutes les 200 sec vers FF02::1 (All nodes)
- Incluent:
- Préfixe réseau
- Passerelle par défaut
- Hôte doit configurer seul:
- ID d'interface

- Adresse IPv6

## Tableaux récapitulatifs

- Numérotation binaire, hexadécimale et décimale
- Ports TCP/UDP courants
- Modèles OSI et TCP/IP
- Caractéristiques des équipements de couche 1 et 2