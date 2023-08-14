# Création d'utilisateurs et de groupes avec PowerShell

## 1. Ouvrir PowerShell en tant qu'administrateur

Assurez-vous d'exécuter PowerShell avec des droits administratifs pour éviter tout problème de permission.

## 2. Création des utilisateurs

### Rosita Espinosa

```powershell
New-ADUser -Name "Rosita Espinosa" -GivenName "Rosita" -Surname "Espinosa" -UserPrincipalName "rosita.espinosa@exemple.com" -SamAccountName "REspinosa" -Description "Membre du groupe Logistique" -PasswordNeverExpires $true -AccountPassword (ConvertTo-SecureString -AsPlainText "MotDePasseTemporaire" -Force)
```

### Morgan Jones

```powershell
New-ADUser -Name "Morgan Jones" -GivenName "Morgan" -Surname "Jones" -UserPrincipalName "morgan.jones@exemple.com" -SamAccountName "MJones" -Description "Membre du groupe Logistique" -PasswordNeverExpires $true -AccountPassword (ConvertTo-SecureString -AsPlainText "MotDePasseTemporaire" -Force)
```

### AV

```powershell
New-ADUser -Name "AV" -GivenName "AV" -Surname "" -UserPrincipalName "av@exemple.com" -SamAccountName "AV" -Description "Membre du groupe Informatique" -PasswordNeverExpires $true -AccountPassword (ConvertTo-SecureString -AsPlainText "MotDePasseTemporaire" -Force)
```

**Note** : Modifiez les champs `-UserPrincipalName` pour les adapter à votre domaine, et changez "MotDePasseTemporaire" par un mot de passe initial pour chaque utilisateur.

## 3. Création des groupes

### Groupe Logistique

```powershell
New-ADGroup -Name "Groupe Logistique" -GroupScope Global -Description "Groupe pour les membres de la logistique" -Path "OU=Groups,DC=exemple,DC=com"
```

### Groupe Informatique

```powershell
New-ADGroup -Name "Groupe Informatique" -GroupScope Global -Description "Groupe pour les membres de l'informatique" -Path "OU=Groups,DC=exemple,DC=com"
```

**Note** : Modifiez `-Path` pour le correspondre à l'emplacement désiré dans votre Active Directory.

## 4. Ajout des utilisateurs aux groupes

### Ajout de Rosita Espinosa et Morgan Jones au groupe Logistique

```powershell
Add-ADGroupMember -Identity "Groupe Logistique" -Members REspinosa, MJones
```

### Ajout de AV au groupe Informatique

```powershell
Add-ADGroupMember -Identity "Groupe Informatique" -Members AV
```

