## Découverte réseau avec CDP/LLDP

```
#show {cdp | lldp}
(config-if)#cdp enable
#show cdp interface
(config-if)#lldp {transmit | receive}

(config)#{cdp | lldp} run
#show {cdp | lldp} neighbors [detail]
```

Activer/désactiver CDP globalement ou sur une interface
Activer la transmission/réception LLDP sur une interface
Voir infos de voisinage détaillées
## NTP (Network Time Protocol)

```
#clock set hh:mm:ss {month | month day} year
#show clock [detail]

(config)#ntp server ip-address
#show ntp associations
#show ntp status
```

Définir date/heure du périphérique
Voir date/heure courante
Configurer un serveur NTP
Vérifier association NTP
## SNMP (Simple Network Management Protocol)

Manager (NMS) : console de gestion
Agents : présents sur les équipements gérés
Protocoles : SNMPv1/v2c (communauté) , SNMPv3 (chiffrement)
## Syslog

```
(config)#service timestamps log

(config)#logging console
(config)#logging buffered
(config)#logging trap severity

(config)#logging source-interface interface

#show logging
```

Horodater les logs
Envoyer les logs à la console
Stocker les logs en mémoire tampon
Envoyer certains logs à un serveur distant
Définir une interface source pour joindre le serveur Syslog
## Cloud computing

IaaS : machine virtuelle complète

PaaS : environnement de développement

SaaS : service clé en main (messagerie, stockage...)

## SDN et contrôleurs

Séparation plan de données / plan de contrôle
Contrôleur SDN centralise tout ou partie du plan de contrôle
Exemples : OpenDaylight, Cisco ACI, Cisco DNA Center
## Outils de gestion de configuration

Automatisation et orchestration des tâches
Modèles déclaratifs vs impératifs
Agentless avec protocole SSH
Propriétés : idempotence, convergence...