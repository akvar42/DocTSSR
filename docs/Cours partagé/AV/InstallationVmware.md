# Guide d'utilisation de VMware Workstation pour un technicien

## 1. Introduction

VMware Workstation est une plateforme de virtualisation de type **Type 2** qui permet de créer et gérer des machines virtuelles (VM) sur un système d'exploitation hôte. Il est idéal pour la simulation, le développement, le test et le dépannage de systèmes.

## 2. Prérequis

- Système d'exploitation compatible (Windows ou Linux).
- Configuration matérielle : CPU avec la virtualisation activée, RAM adéquate, espace disque.
- Téléchargement depuis le site officiel de VMware.

## 3. Installation

1. Exécutez l'installateur.
2. Suivez les instructions.
3. Redémarrez l'ordinateur si nécessaire.

## 4. Création d'une nouvelle machine virtuelle

1. Lancez VMware Workstation.
2. Cliquez sur `File > New Virtual Machine`.
3. Choisissez entre `Typical` ou `Custom`.
4. Suivez l'assistant, sélectionnez le fichier ISO ou DVD, et configurez le matériel virtuel.

## 5. Configuration de la machine virtuelle

### a. Configuration générale

- **CPU & Mémoire** : Attribuez des cœurs de processeur et de la RAM.
- **Disque dur** : Ajustez la taille, ajoutez des disques.
- **Périphériques** : Gérez les périphériques tels que CD/DVD, cartes USB.

### b. Configuration réseau avec Virtual Network Editor

VMware Workstation propose un outil, le "Virtual Network Editor", pour gérer et configurer vos réseaux virtuels :
C'est là où il faut aller lorsqu'on a des probleme de conection + activer/desactiver la carte reseau host.

1. Ouvrez le `Virtual Network Editor`.
2. Vous verrez une liste de VMnets (réseaux virtuels).
3. Pour chaque VMnet :
    - **Type** : Définissez-le comme `NAT`, `Bridged` ou `Host-Only`.
    - **Subnet Address** : Configurez l'adresse du sous-réseau.
    - **NAT Settings** : Configurez la translation d'adresse si vous utilisez NAT.
    - **DHCP Settings** : Activez/Désactivez et configurez le DHCP pour le réseau virtuel.

Avec le "Virtual Network Editor", vous pouvez créer des réseaux isolés, des réseaux avec accès Internet, ou des réseaux bridgés directement avec votre réseau physique.

## 6. Utilisation de la machine virtuelle

1. Sélectionnez la VM.
2. Cliquez sur `Start` ou `Play`.

## 7. Snapshots

1. Sélectionnez la VM.
2. Cliquez sur `VM > Snapshot > Take Snapshot`.
3. Pour restaurer : Sélectionnez le snapshot et `Revert to Snapshot`.

## 8. Clonage de VMs

1. Sélectionnez la VM.
2. Cliquez sur `VM > Manage > Clone`.

## 9. Importation/Exportation des VMs

- Pour exporter : `File > Export to OVF`.
- Pour importer : `File > Open`, puis le fichier OVF ou OVA.

## 10. Conseils pour les techniciens

- Activez l'accélération 3D pour les applications graphiques.
- Utilisez le mode `Bridged` pour que la VM soit sur le même réseau que l'hôte.
- Mettez à jour vos VMs avec les outils VMware.
- Isolations pour des tests sensibles.

## Conclusion

Maîtrisez VMware Workstation pour maximiser vos capacités de virtualisation. Bonne virtualisation!

