# Désactiver les Mises à Jour sur Windows 10

## **Avertissement**: 
La désactivation des mises à jour peut exposer votre système à des vulnérabilités. Assurez-vous de comprendre les conséquences avant de procéder.

### 1. Via le Service de Windows Update (le plus rapide)

1. Appuyez sur `Win + R`, tapez `services.msc` et appuyez sur Entrée.
2. Dans la liste, recherchez `Windows Update` et double-cliquez dessus.
3. Dans le menu déroulant du type de démarrage, choisissez `Désactivé`.
4. Cliquez sur `Stop` pour arrêter le service.
5. Cliquez sur `OK`.

### 2. Via les Paramètres de Stratégie de Groupe Local

*Note*: Cette méthode n'est pas disponible pour Windows 10 Home.

1. Appuyez sur `Win + R`, tapez `gpedit.msc` et appuyez sur Entrée.
2. Naviguez vers `Configuration ordinateur` > `Modèles d'administration` > `Composants Windows` > `Windows Update`.
3. Double-cliquez sur `Configurer les mises à jour automatiques`.
4. Sélectionnez `Désactivé` puis cliquez sur `OK`.

### 3. Via le Registre Windows

**Avertissement** : Modifier le registre peut avoir des conséquences indésirables si mal fait. Procédez avec prudence.

1. Appuyez sur `Win + R`, tapez `regedit` et appuyez sur Entrée.
2. Naviguez vers `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows`.
3. Clic droit sur `Windows` > `Nouveau` > `Clé`. Nommez cette clé `WindowsUpdate` (si elle n'existe pas déjà).
4. Clic droit sur `WindowsUpdate` > `Nouveau` > `Clé`. Nommez cette clé `AU`.
5. Dans la clé `AU`, clic droit dans le volet de droite > `Nouveau` > `Valeur DWORD (32 bits)`. Nommez cette valeur `NoAutoUpdate`.
6. Double-cliquez sur `NoAutoUpdate` et définissez la valeur à `1`.
7. Fermez l'éditeur de registre.

