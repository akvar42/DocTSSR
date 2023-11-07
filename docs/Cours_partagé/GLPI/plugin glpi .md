# Introduction aux plugins de GLPI

GLPI est une application de gestion de services informatiques qui offre la possibilité d'étendre ses fonctionnalités à l'aide de plugins. Ces extensions sont conçues pour ajouter de nouvelles capacités ou améliorer les fonctionnalités existantes.

## Démonstration - Le site https://plugins.glpi-project.org/

Pour découvrir et obtenir des plugins pour GLPI, on visite le site officiel des plugins GLPI. Voici comment on procède :

1. On se rend sur [https://plugins.glpi-project.org/](https://plugins.glpi-project.org/).
2. On explore les différentes catégories ou utilise la fonction de recherche pour trouver un plugin spécifique.
3. Lorsqu'on trouve un plugin intéressant, on lit attentivement la documentation et les notes de mise à jour associées.
4. On télécharge le plugin et on le sauvegarde sur le système où GLPI est installé.

## Le plugin FusionInventory : partie serveur

FusionInventory est un plugin destiné à la gestion de l'inventaire et au télédéploiement au sein de GLPI. Il facilite l'inventaire automatique des composants matériels et logiciels des postes clients.

### Démonstration - Installer le plugin sur les postes à inventorier et forcer l'inventaire

Pour installer le plugin FusionInventory sur des postes clients et initier un inventaire, on suit ces étapes :

1. On télécharge le plugin FusionInventory depuis le site des plugins GLPI.
2. On extrait le fichier téléchargé dans le répertoire `plugins` de l'installation GLPI.
3. On se connecte à l'interface web de GLPI, on va dans le menu "Configuration" > "Plugins", et on installe FusionInventory.
4. Sur les postes clients, on installe l'agent FusionInventory et on configure celui-ci pour communiquer avec le serveur GLPI.
5. Pour forcer l'inventaire, on exécute manuellement l'agent sur les postes clients ou on planifie une tâche dans GLPI.

### Démonstration - Modifier le paramétrage de l'agent

Pour ajuster le paramétrage de l'agent FusionInventory sur les postes clients, on procède comme suit :

1. On accède au fichier de configuration de l'agent généralement situé dans le répertoire d'installation de l'agent.
2. On modifie les paramètres selon les besoins, par exemple, la fréquence des inventaires ou l'adresse du serveur GLPI.
3. On enregistre les modifications et on redémarre le service de l'agent pour appliquer les changements.

### Démonstration - Installer et utiliser le plugin Data-Injection avec un fichier CSV

Le plugin Data-Injection est conçu pour importer des données dans GLPI en utilisant des fichiers CSV. Voici comment on l'utilise :

1. On télécharge le plugin Data-Injection depuis le site des plugins GLPI.
2. On place le plugin dans le répertoire `plugins` de GLPI et on l'installe via l'interface web.
3. On prépare un fichier CSV contenant les données à importer en respectant le format requis par le plugin.
4. On utilise l'interface du plugin Data-Injection pour mapper les colonnes du fichier CSV avec les champs de GLPI.
5. On lance l'importation des données et on vérifie que l'opération s'est déroulée avec succès.
