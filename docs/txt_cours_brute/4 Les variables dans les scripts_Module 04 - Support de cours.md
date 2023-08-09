symbole $
•Si le script vient d’être chargé, les variables locales n’existent pas encore!
13647
6

Scripting Shell
Affectation d’un contenu
Variablede la shell
Naplus valeneticeauCecéeFonctionnement d’une variable
Une variable peut recevoir un contenu à l’action 12er le contenu de 	argument à la variable.
conf=/etc/leserveurs.conf	 # votre fichier de paramètres 	 files=`cat $conf | grep $TARG`# qui va chercher dans le fichier 	 # entre les lignes qui contiennent l’expression 	 # “$TARG” & afficher le contenu au shell![Image](image11.png)
![Image](image12.png)
![Image](image13.png)
![Image](image0.png)![Image](image1.png)![Image](image2.png)![Image](image3.png)
![Image](image4.png)![Image](image5.png)![Image](image6.png)![Image](image7.png