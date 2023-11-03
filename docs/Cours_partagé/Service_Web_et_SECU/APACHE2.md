# Guide d'Installation et de Configuration d'un Site en HTML sur Apache (Debian)

## Installation d'Apache

```sh
sudo apt update
sudo apt install apache2
```

## Démarrage et Activation d'Apache

```sh
sudo systemctl start apache2
sudo systemctl enable apache2
```

## Vérification du Statut d'Apache

```sh
sudo systemctl status apache2
```

## Emplacement des Fichiers de Configuration et Contenus Web

- **/var/www/** : Répertoire racine pour les fichiers de contenu web.
- **/etc/apache2/apache2.conf** : Fichier de configuration principal d'Apache.
- **/etc/apache2/ports.conf** : Fichier pour définir les ports d'écoute.
- **/etc/apache2/sites-available/** : Fichiers de configuration pour les sites disponibles.
- **/etc/apache2/sites-enabled/** : Liens vers les configurations de sites actifs.
- **/etc/apache2/mods-available/** : Configurations pour tous les modules disponibles.
- **/etc/apache2/mods-enabled/** : Liens vers les configurations de modules actifs.
- **/var/log/apache2/** : Fichiers de logs pour le suivi des activités du serveur.

## Configuration des Hôtes Virtuels

1. Créer un fichier de configuration pour votre site :

   ```sh
   sudo nano /etc/apache2/sites-available/monsite.conf
   ```

2. Ajouter la configuration suivante :

   ```apache
   <VirtualHost *:80>
       ServerAdmin webmaster@monsite.com
       ServerName monsite.com
       ServerAlias www.monsite.com
       DocumentRoot /var/www/monsite
       ErrorLog ${APACHE_LOG_DIR}/error.log
       CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```

3. Activer le site :

   ```sh
   sudo a2ensite monsite.conf
   sudo systemctl reload apache2
   ```

## Test de la Configuration d'Apache

```sh
sudo apache2ctl configtest
```

## Permissions et Propriété des Fichiers

```sh
sudo chown -R www-data:www-data /var/www/monsite
sudo chmod -R 755 /var/www/
```

## Sécurisation d'Apache avec HTTPS

### Création d'un Certificat Auto-signé

1. Générer une clé privée et un certificat :

   ```sh
   sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
   ```

2. Ajouter les lignes suivantes dans votre fichier de configuration `/etc/apache2/sites-available/monsite.conf` :

   ```apache
   SSLEngine on
   SSLCertificateFile      /etc/ssl/certs/apache-selfsigned.crt
   SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
   ```

3. Activer le module SSL et redémarrer Apache :

   ```sh
   sudo a2enmod ssl
   sudo systemctl restart apache2
   ```

### Utilisation de Let's Encrypt pour un Certificat Signé

1. Installer `certbot` et le plugin Apache :

   ```sh
   sudo apt install certbot python3-certbot-apache
   ```

2. Obtenir et installer le certificat :

   ```sh
   sudo certbot --apache
   ```

Suivre les instructions de `certbot` pour compléter le processus.

## Exemples de Modules Apache

- **mod_ssl** : Fournit la prise en charge du cryptage SSL/TLS.
- **mod_rewrite** : Permet de réécrire les URL demandées.
- **mod_security** : Fournit des fonctions de pare-feu pour le web.
- **mod_headers** : Permet de personnaliser les en-têtes HTTP.

Pour activer un module, par exemple `mod_rewrite` :

```sh
sudo a2enmod rewrite
sudo systemctl restart apache2
```

## Redémarrage Final d'Apache

```sh
sudo systemctl restart apache2
```

## Surveillance et Maintenance

Consultez régulièrement les fichiers de logs pour détecter les problèmes éventuels.

- **Access Log** : `/var/log/apache2/access.log`
- **Error Log** : `/var/log/apache2/error.log`
