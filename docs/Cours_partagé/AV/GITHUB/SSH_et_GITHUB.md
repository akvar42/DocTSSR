# Créer une clé SSH et la lier à GitHub et au dépôt local

## Création de la clé SSH

1. **Générez une nouvelle clé SSH**:
   ```
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   Remplacez "your_email@example.com" par votre adresse e-mail. Suivez les étapes, et appuyez sur Entrée pour accepter les valeurs par défaut.

2. **Assurez-vous que le ssh-agent est en cours d'exécution**:
   ```
   eval "$(ssh-agent -s)"
   ```

3. **Ajoutez votre clé SSH au ssh-agent**:
   ```
   ssh-add ~/.ssh/id_rsa
   ```

## Lier la clé SSH à GitHub

1. **Installez xclip** (pour copier la clé publique dans le presse-papiers) :
   ```
   sudo apt-get install xclip
   ```
   Si vous n'utilisez pas une distribution basée sur Debian, adaptez la commande à votre gestionnaire de paquets.

2. **Copiez la clé publique dans votre presse-papiers**:
   ```
   xclip -sel clip < ~/.ssh/id_rsa.pub
   ```

3. **Connectez-vous à votre compte GitHub** et allez dans `Settings`.

4. Dans le menu de gauche, cliquez sur **SSH and GPG keys**.

5. Cliquez sur **New SSH key**, donnez-lui un titre descriptif (par exemple, "Mon PC personnel") et collez votre clé dans le champ "Key".

6. Cliquez sur **Add SSH key**.

## Lier la clé SSH au dépôt local

1. Si vous avez déjà un dépôt local associé à GitHub via HTTPS, vous devrez changer l'URL du dépôt pour utiliser SSH. Voici comment faire :

   ```
   git remote set-url origin git@github.com:USERNAME/REPO.git
   ```
   Remplacez `USERNAME` par votre nom d'utilisateur GitHub et `REPO` par le nom de votre dépôt.

2. Maintenant, vous pouvez **push**, **pull** et **clone** en utilisant SSH sans avoir à saisir votre nom d'utilisateur et votre mot de passe à chaque fois !


