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
4. **Explication**

 ssh-keygen: C'est la commande principale pour la génération de clés SSH.

-t rsa: Cet argument spécifie le type de clé à créer. Dans ce cas, vous avez choisi RSA (Rivest-Shamir-Adleman), qui est un algorithme de chiffrement asymétrique largement utilisé.

-b 4096: Cet argument définit la taille de la clé en bits. Ici, la taille de la clé est de 4096 bits, ce qui est considéré comme étant très sécurisé. Par défaut, si vous n'indiquez pas la taille de la clé avec -b, la taille sera de 3072 bits pour RSA (dans les versions plus récentes de SSH), mais cela peut varier selon la version et la configuration.

-C: Cet argument permet de fournir un commentaire qui est attaché à la clé. Habituellement, le commentaire est utilisé pour identifier la clé, par exemple avec une adresse e-mail ou le nom de l'utilisateur. Après -C, vous devriez normalement fournir une valeur pour le commentaire, par exemple : ssh-keygen -t rsa -b 4096 -C "votre.email@example.com".

En utilisant cette commande, vous générerez une paire de clés : une clé privée (normalement appelée id_rsa par défaut) et une clé publique (normalement appelée id_rsa.pub par défaut). La clé privée doit être gardée secrète et protégée, tandis que la clé publique peut être partagée ou ajoutée à des serveurs pour permettre une authentification sans mot de passe. 

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


