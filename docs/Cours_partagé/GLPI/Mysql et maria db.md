# Guide des Bases de Données MySQL/MariaDB

## Rappel sur les SGBD et le langage SQL

Je me sers des Systèmes de Gestion de Bases de Données (SGBD) comme MySQL ou MariaDB pour gérer et interroger des données structurées. Le langage que j'emploie pour ces opérations est le SQL, qui me permet de créer, récupérer, modifier et supprimer les données.

## Les commandes de base MySQL/MariaDB

```
SHOW DATABASES; -- Je liste toutes les bases de données.
CREATE DATABASE ma_base_de_donnees; -- Je crée une nouvelle base de données.
USE ma_base_de_donnees; -- Je sélectionne la base de données pour mes opérations.
SHOW TABLES; -- Je montre toutes les tables dans la base de données actuelle.
CREATE TABLE ma_table (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(100)); -- Je crée une nouvelle table avec une colonne ID et une colonne nom.
DESCRIBE ma_table; -- Je consulte la structure de ma table.
INSERT INTO ma_table (nom) VALUES ('Exemple'); -- J'insère une nouvelle entrée dans ma table.
SELECT * FROM ma_table; -- Je sélectionne et affiche toutes les données de ma table.
UPDATE ma_table SET nom = 'Nouveau' WHERE id = 1; -- Je mets à jour une entrée spécifique de ma table.
DELETE FROM ma_table WHERE id = 1; -- Je supprime une entrée de ma table.
DROP TABLE ma_table; -- Je supprime la table entière.
DROP DATABASE ma_base_de_donnees; -- Je supprime la base de données entière.
```

## Démonstration - Connexion à la base MariaDB de GLPI et affichage de tables et structures

```sql
mysql -u mon_utilisateur -p -- Je me connecte à la base de données MariaDB.
SHOW DATABASES; -- J'affiche les bases de données disponibles.
USE glpi; -- Je sélectionne la base de données de GLPI pour utilisation.
SHOW TABLES; -- J'affiche les tables de la base de données GLPI.
DESCRIBE glpi_users; -- Je consulte la structure de la table des utilisateurs.
```

## Manipulation de la base de données

```sql
INSERT INTO glpi_users (name, password) VALUES ('utilisateur', 'motdepasse'); -- J'ajoute un nouvel utilisateur.
SELECT name, password FROM glpi_users; -- Je récupère les noms d'utilisateur et les mots de passe.
UPDATE glpi_users SET password = 'nouveaumotdepasse' WHERE name = 'utilisateur'; -- Je mets à jour le mot de passe d'un utilisateur.
DELETE FROM glpi_users WHERE name = 'utilisateur'; -- Je supprime un utilisateur de la base de données.
```

## Démonstration - Affichage de la liste des comptes utilisateurs de GLPI

```sql
SELECT * FROM glpi_users; -- J'affiche tous les utilisateurs enregistrés dans GLPI.
```

## Requête sur plusieurs tables : les clés et les jointures

```sql
SELECT u.name, t.name
FROM glpi_users AS u
INNER JOIN glpi_tickets AS t ON u.id = t.user_id; -- Je récupère les noms des utilisateurs et les tickets associés.
```

## Les Clés et les Jointures en SQL

Lorsque je travaille avec des bases de données relationnelles, je me sers des clés pour établir des relations entre différentes tables. Une clé est une colonne ou un ensemble de colonnes utilisées pour identifier de manière unique les lignes dans une table. Les types de clés les plus courants sont :

- **Clé primaire (`PRIMARY KEY`)**: Une colonne ou un groupe de colonnes qui identifie de manière unique chaque ligne de la table. Il ne peut y avoir qu'une seule clé primaire par table et aucune des colonnes ne peut avoir de valeurs nulles.

```sql
CREATE TABLE personnes (
    id INT AUTO_INCREMENT,
    nom VARCHAR(100),
    PRIMARY KEY (id)
);
```

- **Clé étrangère (`FOREIGN KEY`)**: Une colonne ou un ensemble de colonnes qui fait référence à la clé primaire d'une autre table. Cela permet de maintenir l'intégrité référentielle entre les deux tables.

```sql
CREATE TABLE commandes (
    commande_id INT,
    utilisateur_id INT,
    PRIMARY KEY (commande_id),
    FOREIGN KEY (utilisateur_id) REFERENCES personnes(id)
);
```

Les jointures sont utilisées pour récupérer des données de plusieurs tables et les combiner en fonction des relations définies par les clés. Les types de jointures en SQL comprennent :

- **INNER JOIN**: Sélectionne les enregistrements qui ont des valeurs correspondantes dans les deux tables.

```sql
SELECT personnes.nom, commandes.commande_id
FROM personnes
INNER JOIN commandes ON personnes.id = commandes.utilisateur_id;
```

- **LEFT JOIN (ou LEFT OUTER JOIN)**: Sélectionne tous les enregistrements de la table de gauche (table principale), avec les enregistrements correspondants de la table de droite. Les résultats incluent toutes les lignes de la table de gauche, même s'il n'y a pas de correspondance dans la table de droite.

```sql
SELECT personnes.nom, commandes.commande_id
FROM personnes
LEFT JOIN commandes ON personnes.id = commandes.utilisateur_id;
```

- **RIGHT JOIN (ou RIGHT OUTER JOIN)**: Sélectionne tous les enregistrements de la table de droite, avec les enregistrements correspondants de la table de gauche. Les résultats incluent toutes les lignes de la table de droite, même s'il n'y a pas de correspondance dans la table de gauche.

```sql
SELECT personnes.nom, commandes.commande_id
FROM personnes
RIGHT JOIN commandes ON personnes.id = commandes.utilisateur_id;
```

- **FULL JOIN (ou FULL OUTER JOIN)**: Sélectionne tous les enregistrements lorsqu'il y a une correspondance dans l'une des tables.

```sql
SELECT personnes.nom, commandes.commande_id
FROM personnes
FULL OUTER JOIN commandes ON personnes.id = commandes.utilisateur_id;
```

- **CROSS JOIN**: Produit le produit cartésien de deux tables, c'est-à-dire qu'il combine chaque ligne de la première table avec chaque ligne de la seconde table.

```sql
SELECT personnes.nom, commandes.commande_id
FROM personnes
CROSS JOIN commandes;
```

Chaque type de jointure  sert à récupérer des informations de manière spécifique selon la relation que j'ai établie entre mes tables. Je dois donc choisir le type de jointure adapté à la situation pour obtenir les résultats souhaités.


## Démonstration - Affichage de la liste des comptes utilisateurs de GLPI ayant ouvert un ticket d'intervention

```sql
SELECT u.name, t.title
FROM glpi_users AS u
JOIN glpi_tickets AS t ON u.id = t.user_id
WHERE t.type='intervention'; -- Je liste tous les utilisateurs qui ont ouvert un ticket d'intervention.
```

## Démonstration - Sauvegarde (dump) de la base de données de GLPI

```bash
mysqldump -u mon_utilisateur -p glpi > sauvegarde_glpi.sql -- Je crée une sauvegarde de la base de données GLPI.
```

Chaque commande est un exemple que je peux utiliser pour gérer ma base de données MySQL ou MariaDB. Je dois veiller à remplacer `mon_utilisateur`, `ma_table`, `ma_base_de_donnees`, `utilisateur`, `motdepasse`, et `nouveaumotdepasse` par mes propres valeurs
