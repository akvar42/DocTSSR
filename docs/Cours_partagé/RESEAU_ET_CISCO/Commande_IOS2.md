## Configuration des annonces RA du routeur IPv6

Annonces RA envoyées toutes les 200 sec vers FF02::1 (All nodes)

Flags A, O et M :

- A : activation de SLAAC pour l'adresse GUA

- O : disponibilité d'infos via DHCPv6 sans état
- M : demande de DHCPv6 avec état pour l'adresse GUA

## Méthodes d'attribution d'adresses IPv6

Sans état

- Méthode 1 : SLAAC seule

- Méthode 2 : SLAAC + DHCPv6 sans état

Avec état

- Méthode 3 : DHCPv6 avec état

## Routeur en tant que routeur IPv6

```
(config)#ipv6 unicast-routing

(config-if)#ipv6 address ipv6-address/prefix
```

## Routeur en tant que serveur DHCPv6

Sans état

```

(config)#ipv6 dhcp pool nom

(dhcpv6-config)#dns-server ipv6-addr
(dhcpv6-config)#domain-name domaine

(config-if)#ipv6 dhcp server nom
```

Avec état

```
(config)#ipv6 dhcp pool nom

(dhcpv6-config)#address prefix ipv6-prefix/length

(dhcpv6-config)#dns-server ipv6-addr

(dhcpv6-config)#domain-name domaine
(config-if)#ipv6 dhcp server nom
```

## Routeur en tant que client DHCPv6

```
(config)#ipv6 unicast-routing

(config-if)#ipv6 enable
(config-if)#ipv6 address dhcp
```

## Routeur en tant qu'agent relais DHCPv6

```
(config)#ipv6 dhcp relay destination [interface]
```

## VLAN

Plage normale : 1-1005
Plage étendue : 1006-4094
```
(config)#vlan numero

(config-vlan)#name nom
#show vlan [id/name/summary]
```

## Ports d'accès VLAN

```
(config-if)#switchport mode access

(config-if)#switchport access vlan numero
```

## Ports voix (téléphonie sur IP)

```
(config-if)#switchport voice vlan numero

(config-if)#mls qos trust cos
```

## Ports Trunk VLAN

```
(config-if)#switchport mode trunk
(config-if)#switchport trunk native vlan numero
(config-if)#switchport trunk allowed vlan numero
```

## Protocole DTP (négociation de trunks)

Modes : trunk, desirable, auto, nonegotiate
## Routage inter-VLAN

Routeur-on-a-stick

```
(config-subif)#encapsulation dot1q vlan-id
(config-subif)#ip address adresse masque
```

Routeur de couche 3

```
(config)#ip routing

(config)#interface vlan vlan-id

(config-if)#ip address adresse masque
```

## Spanning Tree Protocol (STP)

```
#show spanning-tree [summary | vlan vlan-id]
(config-if)#spanning-tree portfast

(config)#spanning-tree portfast default
(config-if)#spanning-tree bpduguard enable
(config)#spanning-tree portfast bpduguard default
(config)#spanning-tree vlan vlan-id root primary
(config)#spanning-tree vlan vlan-id priority valeur
(config-if)#spanning-tree cost valeur
```

## EtherChannel

```
(config-if-range)#channel-group num mode {on | active | passive}

(config-if-range)#channel-group num mode {auto | desirable}
(config)#interface port-channel num

#show etherchannel [num] {brief | port-channel | summary}
#show interfaces port-channel num
```

## DHCPv4

```
(config)#ip dhcp excluded-address debut [fin]
(config)#ip dhcp pool nom

(dhcp-config)#network adr. reseau [masque]
(dhcp-config)#default-router adr. passerelle

(dhcp-config)#dns-server adr. serveurDNS
(config-if)#ip helper-address adr. serveurDHCP

#show ip dhcp binding
#show ip dhcp server statistics
```

## Sécurité de ports

```
(config-if)#switchport port-security
(config-if)#switchport port-security mac-address adrMAC
(config-if)#switchport port-security maximum valeur
(config-if)#switchport port-security violation {protect | restrict | shutdown}

#show port-security [interface intf]
#show port-security address
```

## DHCP Snooping

```
(config)#ip dhcp snooping
(config)#ip dhcp snooping vlan vlan-list
(config-if)#ip dhcp snooping trust

#show ip dhcp snooping

#show ip dhcp snooping binding
```

## Dynamic ARP Inspection (DAI)

```
(config)#ip arp inspection vlan vlan-list
(config-if)#ip arp inspection trust
(config)#ip arp inspection validate {dst-mac | src-mac | ip}
```

## WiFi 802.11

Standards : 802.11a/b/g/n/ac/ax
Fréquences : 2.4 GHz et 5 GHz
Débits théoriques max
Modes : infrastructure et ad hoc
Sécurité : WEP, WPA, WPA2, WPA3