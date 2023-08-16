# Modifier le masque de sous-réseau sous Debian

## Prérequis

Avant de commencer, assurez-vous d'avoir les droits d'administrateur (root) et d'avoir une sauvegarde de vos configurations actuelles.

## Étapes

### 1. Ouvrez le fichier de configuration du réseau

Utilisez votre éditeur de texte préféré. Nous utiliserons nano dans cet exemple :

```bash
sudo nano /etc/network/interfaces
```

### 2. Recherchez la configuration de l'interface réseau

Vous verrez des configurations pour différentes interfaces réseau, telles que `eth0`, `wlan0`, etc. Trouvez celle que vous souhaitez modifier.

Exemple :
```
iface eth0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
```

### 3. Modifiez le masque de sous-réseau

Remplacez la valeur actuelle de `netmask` par le nouveau masque de sous-réseau souhaité.

### 4. Enregistrez et fermez le fichier

Si vous utilisez nano :
- Appuyez sur `Ctrl + O` pour enregistrer
- Appuyez sur `Ctrl + X` pour quitter

### 5. Redémarrez le service réseau

Pour que les modifications prennent effet, redémarrez le service réseau :

```bash
sudo /etc/init.d/networking restart
```

## Vérification

Pour vous assurer que le masque de sous-réseau a bien été modifié, utilisez la commande suivante :

```bash
ifconfig eth0
```

Remplacez `eth0` par le nom de votre interface réseau si nécessaire. Vous devriez voir le nouveau masque de sous-réseau dans les résultats.

## Conseils

- Toujours sauvegarder vos configurations avant d'apporter des modifications.
- Modifiez le masque de sous-réseau uniquement si vous êtes sûr de ce que vous faites. Une mauvaise configuration peut vous déconnecter du réseau.

