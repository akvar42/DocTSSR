## Création d'un dossier et d'un fichier pour tous les utilisateurs sur Windows 10

Pour créer un dossier nommé "Procédures" sur le bureau de chaque utilisateur existant et y ajouter un fichier "Règlement intérieur" sur un système Windows 10, suivez les étapes ci-dessous. Vous aurez besoin de privilèges administratifs pour réaliser ces opérations.

### 1. Préparation :
- Ouvrez le Bloc-notes ou tout autre éditeur de texte.
- Créez un fichier appelé "Règlement intérieur" (ajoutez le contenu souhaité si nécessaire).
- Enregistrez ce fichier à un emplacement temporaire, par exemple `C:\temp`.

### 2. Script PowerShell :
- Ouvrez une fenêtre PowerShell en tant qu'administrateur.
- Copiez et collez le script suivant :

```powershell
# Chemin de destination pour le nouveau dossier sur le bureau de chaque utilisateur
$destinationPath = "C:\Users\*\Desktop\Procédures"

# Chemin du fichier "Règlement intérieur" que vous avez préparé
$sourceFile = "C:\temp\Règlement intérieur.txt"

# Création du dossier "Procédures" sur le bureau de chaque utilisateur
Get-ChildItem -Path "C:\Users\*" -Directory | ForEach-Object {
    $folderPath = Join-Path $_.FullName "Desktop\Procédures"
    if (-not (Test-Path $folderPath)) {
        New-Item -Path $folderPath -ItemType Directory
    }
}

# Copie du fichier "Règlement intérieur" dans le dossier "Procédures" de chaque utilisateur
Copy-Item -Path $sourceFile -Destination $destinationPath
```

### 3. Exécution du script :
- Exécutez le script dans la fenêtre PowerShell. Cela créera le dossier "Procédures" sur le bureau de chaque utilisateur et y copiera le fichier "Règlement intérieur".

### 4. Nettoyage (facultatif) :
- Si vous le souhaitez, vous pouvez maintenant supprimer le fichier "Règlement intérieur" de l'emplacement temporaire `C:\temp`.

**Note** : Ce script ne fonctionnera que pour les profils d'utilisateurs existants. Si de nouveaux comptes sont créés après l'exécution du script, vous devrez réexécuter le script ou créer le dossier et le fichier manuellement pour ces nouveaux utilisateurs.
