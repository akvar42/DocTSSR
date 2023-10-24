# Guide PowerShell

PowerShell est un environnement de scripting avancé basé sur .NET, permettant l'automatisation des tâches administratives et la gestion des configurations.

## PowerShell est Orienté Objet
En PowerShell, tout est un objet. Cela signifie que chaque sortie d'une commande peut avoir des propriétés et des méthodes auxquelles on peut accéder.

## Les Cmdlets
Les commandes dans PowerShell sont appelées "cmdlets" (prononcées "command-lets"). Elles suivent généralement la syntaxe Verbe-Nom, par exemple Get-Process.

## Les Principales Commandes (Cmdlets)
- `Get-Command`: Liste toutes les cmdlets disponibles
  ```powershell
  Get-Command
  ```
- `Get-Help`: Obtient de l'aide pour une cmdlet spécifique
  ```powershell
  Get-Help Get-Process
  ```
- `Get-Process`: Liste tous les processus en cours
  ```powershell
  Get-Process
  ```
- `Set-ExecutionPolicy`: Change la politique d'exécution des scripts
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```
- `Import-Module`: Importe un module PowerShell
  ```powershell
  Import-Module ActiveDirectory
  ```
- `Get-Member`: Obtient les propriétés et les méthodes d'un objet
  ```powershell
  $process = Get-Process -Name "chrome"
  $process | Get-Member
  ```

## d'autres Cmdlets Couramment Utilisés

### Where-Object

`Where-Object` filtre les objets en fonction de leurs propriétés. 

```powershell
Get-Process | Where-Object {$_.CPU -gt 100}
```
Ceci retourne tous les processus dont l'utilisation CPU est supérieure à 100.

### Select-Object

`Select-Object` permet de sélectionner des propriétés spécifiques d'un objet.

```powershell
Get-Process | Select-Object Name, CPU, ID
```
Ceci retourne le nom, l'utilisation CPU et l'ID de tous les processus.

### Sort-Object

`Sort-Object` trie les objets en fonction de leurs propriétés.

```powershell
Get-Process | Sort-Object CPU -Descending
```
Ceci trie les processus en fonction de leur utilisation CPU, du plus élevé au plus bas.

###  Measure-Object

`Measure-Object` calcule des propriétés telles que le compte, la somme ou la moyenne d'objets.

```powershell
Get-Content C:fichier.txt | Measure-Object -Line
```
Ceci compte le nombre de lignes dans un fichier.

###  Out-File

`Out-File` dirige la sortie vers un fichier.

```powershell
Get-Process | Out-File C:processus.txt
```
Ceci sauvegarde la liste des processus dans un fichier nommé "processus.txt".

###  Test-Connection

`Test-Connection` envoie des paquets ICMP (ping) à une adresse.

```powershell
Test-Connection google.com
```
Ceci vérifie si google.com est accessible via ping.




## Les Opérateurs
- -eq: Égal à
- -ne: Non égal à
- -gt: Plus grand que
- -lt: Moins que
- -ge: Plus grand ou égal à
- -le: Moins ou égal à

## Les Variables
- `$NomVariable = "Valeur"` : Définit une variable
  ```powershell
  $monNom = "Alice"
  ```
- `$env:NomVariable` : Accède à une variable d'environnement
  ```powershell
  $env:USERNAME
  ```

## Les Fonctions
```powershell
function Saluer {
    param(
        [string]$nom = "Monde"
    )
    Write-Host "Bonjour, $nom!"
}

# Appeler la fonction
Saluer -nom "Alice"
```

## Les Boucles et Conditions
```powershell
# If
if ($monNom -eq "Alice") {
    Write-Host "Bonjour Alice!"
}

# ForEach
$processus = Get-Process
foreach ($process in $processus) {
    Write-Host $process.Name
}

# While
$i = 0
while ($i -lt 10) {
    Write-Host $i
    $i++
}
```

## Les Structures de Contrôle

### Switch

Le `switch` est une structure de contrôle qui permet de tester la valeur d'une variable ou d'une expression et d'exécuter un bloc de code en fonction de cette valeur.

```powershell
switch ($variable) {
    'valeur1' {
        # code à exécuter si $variable égale 'valeur1'
    }
    'valeur2' {
        # code à exécuter si $variable égale 'valeur2'
    }
    default {
        # code à exécuter si aucune correspondance n'est trouvée
    }
}
```

### Do-While

Le `do-while` est une boucle qui exécute un bloc de code au moins une fois avant de vérifier la condition.

```powershell
do {
    # code à exécuter
    $i++
} while ($i -lt 10)
```

### Try-Catch-Finally

La structure `try-catch-finally` est utilisée pour capturer et gérer les erreurs.

```powershell
try {
    # code qui peut générer une erreur
    Get-Item 'C:nonexistentfile.txt'
} catch {
    # code à exécuter en cas d'erreur
    Write-Host "Une erreur s'est produite : $_"
} finally {
    # code à exécuter quel que soit le résultat (erreur ou non)
    Write-Host "Opération terminée."
}
```


## Les Pipelines
```powershell
Get-Process | Where-Object {$_.CPU -gt 100}
```

## Les Objets et Propriétés
Supposons que l'on exécute Get-Process pour obtenir des informations sur les processus en cours. Chaque processus est un objet avec des propriétés comme CPU, Id, etc. On peut accéder à ces propriétés en utilisant la notation pointée.

```powershell
$process = Get-Process -Name "chrome"
$process.Id  # Accède à la propriété "Id"
```

## sauvegarde Scripts
Pour enregistrer un ensemble de commandes dans un fichier script, utilisez l'extension .ps1.

```powershell
# MonScript.ps1
param(
    [string]$nom = "Monde"
)
Write-Host "Bonjour, $nom!"

# Pour exécuter en personalisant la variable $nom au lancement du script :
.MonScript.ps1 -nom "Alice"
```
