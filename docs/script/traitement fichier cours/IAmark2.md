```
import openai
import os

openai.api_key = 'entrer votre clef API'

def traiter_texte_par_morceaux(texte, taille_max=2000):
    morceaux = [texte[i:i+taille_max] for i in range(0, len(texte), taille_max)]
    texte_traité = ""
    
    for morceau in morceaux:
        reponse = openai.Completion.create(engine="davinci", prompt=morceau, max_tokens=100)
        texte_traité += reponse.choices[0].text.strip()
    
    return texte_traité

def traiter_fichiers(dossier_source, dossier_destination):
    for racine, dossiers, fichiers in os.walk(dossier_source):
        for fichier in fichiers:
            if fichier.endswith(".md"):
                chemin_complet = os.path.join(racine, fichier)
                with open(chemin_complet, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                    contenu_traité = traiter_texte_par_morceaux(contenu)
                
                chemin_destination = os.path.join(dossier_destination, fichier)
                with open(chemin_destination, 'w', encoding='utf-8') as f:
                    f.write(contenu_traité)

if __name__ == "__main__":
    dossier_source = input("Entrez le chemin du dossier source contenant les fichiers .md :")
    dossier_destination = input("Entrez le chemin du dossier de destination pour les fichiers traités :")
    traiter_fichiers(dossier_source, dossier_destination)
```
