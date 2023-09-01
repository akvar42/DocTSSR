# Base des réseaux

## Objectifs

- Expliquer la communication entre ordinateurs
- Présenter le routage
- Calculer des adresses de sur-réseaux

### La communication 

La communication entre ordinateurs se fait via des interfaces réseau (cartes réseau) qui possèdent une adresse physique (MAC) et une adresse logique (IP).

### Domaine de diffusion

Les ordinateurs sont regroupés en domaines de diffusion (broadcast). Toutes les machines d'un même domaine de diffusion peuvent communiquer directement entre elles sans passerelle.

![Alt text](image.png)

### Délimitation des domaines 

Un domaine de diffusion est délimité par des routeurs. Les routeurs possèdent deux (ou plusieurs) interfaces, chacune dans un domaine différent. Ils font le lien entre les domaines.

### Théorie

![Alt text](image-1.png)

### Communication entre deux PC (ping) 

![Alt text](image-2.png)

![Alt text](image-3.png)

### Pratique

![Alt text](image-4.png)

![Alt text](image-5.png)

![Alt text](image-6.png)

![Alt text](image-7.png)

![Alt text](image-8.png)

## Le routage  

### La couche réseau

![Alt text](image-9.png)

## Le sur-réseau

### Création de sur-reseaux (RFC 1519)

- Dans une infrastructure routée
- Diminuer le nombre de routes à créer sur les routeurs
- Diminuer l’utilisation des ressources sur les routeurs
  - Moins de mémoire utilisée
  - Moins de temps processeur
- Routage plus rapide
- Augmenter la stabilité du réseau  

### Le calcul de sur-réseau 

![Alt text](image-10.png)

- Indiquer à R1 quels sont les réseaux présents
  - En une seule route
  - En faisant l’agrégation des réseaux
 - Création d’un sur-réseau  

### Calcul de l'adresse de sur-réseau

![Alt text](image-11.png)

![Alt text](image-12.png)

- Rajout de la route ``192.168.64.0 /18`` en passant par ``R2``  

## En complément :

[Télécharger la fiche demo](fiche_démo_la_communication_réseau.pdf "La communication réseau")