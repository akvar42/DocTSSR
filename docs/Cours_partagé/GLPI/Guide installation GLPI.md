# Guide d'Installation GLPI

## Prérequis
- Serveur Ubuntu avec Apache.
- PHP et MariaDB.

## Installation

### 1. Installation de MariaDB
```bash
sudo apt update
sudo apt install mariadb-server mariadb-client
sudo mysql_secure_installation
```

### 2. Configuration de MariaDB
```bash
sudo mysql -u root -p
CREATE DATABASE glpi;
CREATE USER 'glpiuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON glpi.* TO 'glpiuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 3. Installation du module PHP pour Apache et extensions PHP
```bash
sudo apt-get install libapache2-mod-php8.1
sudo apt-get install php-mysqli php-curl php-gd php-mbstring php-xml php-cli php-ldap php-imap php-apcu
sudo a2enmod php8.1
```

### 4. Téléchargement et Installation de GLPI
```bash
wget https://github.com/glpi-project/glpi/releases/download/9.5.6/glpi-9.5.6.tgz
tar -zxvf glpi-9.5.6.tgz -C /var/www/html/
sudo chown -R www-data:www-data /var/www/html/glpi
sudo chmod -R 755 /var/www/html/glpi
```

### 5. Configuration d'Apache
    Créer le fichier glpi.conf dans /etc/apache2/sites-available/ avec le contenu suivant :

```bash
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/glpi
    ServerName votre_serveur

    <Directory /var/www/html/glpi>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

    Ensuite, activer le site et redémarrer Apache :
```bash
sudo a2ensite glpi
sudo systemctl restart apache2
```

## Installation Web de GLPI
    Accéder à http://votre_serveur/glpi et suivre l'assistant d'installation.

## Configuration Post-Installation
    Sécuriser le fichier de configuration :
```bash
sudo chmod 400 /var/www/html/glpi/config/config_db.php
```

## Utilisation de GLPI
    Se connecter à GLPI avec les identifiants créés durant l'installation.
    Configurer l'environnement GLPI (entités, utilisateurs, matériels, etc.).
