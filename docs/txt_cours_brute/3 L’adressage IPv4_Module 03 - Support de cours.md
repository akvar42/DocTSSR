au de classe C , l’ID_Réseau est compris entre :
•Classe entière : 191et 223
•Classe utilisable : 192et 22310 255 . . .Conf1 255 . . .250 255 . . .255
1•Réseau de 65 555 hôtes possibles
Id2 100x
xxxx xxxx xxxx xxxx xxxx 1 0
914230 61104un réseau
Réseau logique 192.168.76.0
•Identifier l’hôte
192.168.76.150,octet3 place les bits à 1
•Masque : 255.255.255.240
•Catherine 13h39min 27/04/09
Octet 1 Octet 2 Octet 3 Octet 4

Identifier un réseau
Decompositionlogique
Ré1 1..[ 1111 1111 1111 11..]11111 1111 1100..[.11111 .. .101100 .. .0000010 ..1100 0000 1010111111 1111 11.>> 1115001001111111111111111111111111 >>>
Octet 1 Octet 2 Octet 3 Octet 4

101000 1000 000 0 000 000 000 000 000 0
10101 0100 1000 0000 0011000001000 0110100AAA gggg aaaa:
1 2 3 4 5 6 7 000 011... Octet 1 : 255.255.248.0 0 000 0... Octet 2 : 255. 0... Octet 3 : 255. 0 000 ... Octet 4 : 255. 0 0+Additionner ensemble les bits à « 0» qui sont marqués au tableauCompte des bits à tolérer 3 21Résumé 23 24
La notation CIDR
Calcul du0.010.255.255.25410.0.0.0 /810.0.0.010.255.255.255255.0.0.0 10.0.0.0 /8Liste des adresses privéesRFC 1918Français29
La manière de dériver les adresses IPv4 3 étapes
I. Restricted CIDR notation( RFC 1918 ) : Masque d’adress2 0 0 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
Masque du sous -réseau
192 168 0
0 0 0 0 0 0
sous-réseau
2 0 0 1 1 0
64
0 0 0 0 0 0
96

0 0 0 0 0 0 0
124

0 0 0 4 124
128

Le![Image](image21.png)

![Image](image0.png)
![Image](image1.png)
![Image](image2.png)
![Image](image3.png)
![Image](image4.png)
![Image](image5.png)
![Image](image6.png)
![Image](image7.png)
![Image](image8.png)