```
# Définir le chemin du dossier source et du dossier de destination
$sourceDir = "C:\chemin\vers\le\dossier\source"
$destDir = "C:\chemin\vers\le\dossier\destination"

# Rechercher tous les fichiers .pdf, à l'exclusion des .zip, et les copier vers le dossier de destination
Get-ChildItem -Path $sourceDir -Recurse -File -Filter "*.pdf" | Where-Object { $_.Extension -ne ".zip" } | ForEach-Object {
    $dest = $destDir + $_.FullName.Substring($sourceDir.Length)
    $destFolder = Split-Path -Path $dest -Parent
    if (-not (Test-Path $destFolder)) {
        New-Item -Path $destFolder -ItemType Directory
    }
    Copy-Item -Path $_.FullName -Destination $dest
}

Write-Output "Copie terminée."
```
