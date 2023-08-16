### Installation et partage de l'imprimante HP LaserJet M9050 MFP

1. **Démarrage du gestionnaire d'ajout d'imprimante** :
   - On se rend dans `Panneau de configuration` > `Matériel et audio` > `Périphériques et imprimantes`.
   - On clique sur `Ajouter une imprimante`.

2. **Choix du type d'imprimante** :
   - Lorsqu'on est interrogé sur la manière d'installer l'imprimante, on choisit `Ajouter une imprimante en utilisant une adresse IP ou un nom d'hôte`.
   - On clique sur `Suivant`.

3. **Renseignement de l'adresse IP** :
   - Dans le champ `Nom d'hôte ou adresse IP`, on inscrit `172.16.63.251`.
   - On s'assure que l'option `Interroger l'imprimante et sélectionner automatiquement le pilote à utiliser` est activée.
   - On clique sur `Suivant`.

4. **Sélection du pilote** :
   - Si Windows reconnaît l'imprimante, il peut proposer un pilote par défaut. Sinon, on sélectionne `HP` comme fabricant et trouve `LaserJet M9050 MFP` dans la liste des pilotes.
   - Si le pilote n'est pas listé, il faudra peut-être le télécharger depuis le site officiel de HP et l'installer manuellement.
   - On clique sur `Suivant`.

5. **Nom de l'imprimante** :
   - On donne un nom à l'imprimante, par exemple : "HP LaserJet M9050 MFP".
   - On clique sur `Suivant`.

6. **Options de partage** :
   - Quand l'option de partage est présentée, on coche `Partager cette imprimante`.
   - Dans le champ `Nom de partage`, on indique un nom qui sera utilisé sur le réseau pour accéder à cette imprimante. Par exemple, "HPM9050_Shared".
   - On clique sur `Suivant`.

7. **Finalisation** :
   - Une page récapitulative est présentée. On vérifie toutes les informations.
   - On clique sur `Terminer`.

8. **Test** :
   - Pour confirmer que tout est bien configuré, on imprime une page test.

9. **Accès depuis un autre poste** :
   - Depuis un autre ordinateur du réseau, on va dans `Périphériques et imprimantes`, puis on ajoute une imprimante.
   - On recherche l'imprimante partagée par nom et l'ajoute à la liste des imprimantes de l'ordinateur.
