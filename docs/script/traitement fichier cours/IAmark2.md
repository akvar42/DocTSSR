```
import openai
import os

# Configuration de l'API OpenAI
openai.api_key = 'VOTRE_CLÉ_API'

def traiter_texte(texte):
    taille_max = 2000
    morceaux = [texte[i:i+taille_max] for i in range(0, len(texte), taille_max)]
    texte_traité = ""

    for morceau in morceaux:
        # Utiliser l'API OpenAI pour traiter le morceau de texte
        reponse = openai.Completion.create(
            engine="davinci", 
            prompt=f"Extrait les données pertinentes de ce texte :\n\n{morceau}\n\net mets-les en page en Markdown.",
            max_tokens=1000,  # Ajustez cette valeur en fonction de vos besoins
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            language="fr"
        )
        texte_traité += reponse.choices[0].text.strip()
    
    return texte_traité

def traiter_fichiers(dossier_source, dossier_destination):
    for root, dirs, files in os.walk(dossier_source):
        for fichier in files:
            if fichier.endswith('.md'):
                chemin_fichier = os.path.join(root, fichier)
                with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    contenu = f.read()

                    # Traiter le contenu
                    contenu_traité = traiter_texte(contenu)
                    
                    # Chemin relatif pour conserver la structure du sous-dossier
                    chemin_relatif = os.path.relpath(root, dossier_source)
                    dossier_destination_final = os.path.join(dossier_destination, chemin_relatif)
                    
                    # Créer le sous-dossier dans le dossier de destination si nécessaire
                    if not os.path.exists(dossier_destination_final):
                        os.makedirs(dossier_destination_final)

                    # Écrire le contenu traité dans le dossier de destination
                    chemin_fichier_traité = os.path.join(dossier_destination_final, 'traité_' + fichier)
                    with open(chemin_fichier_traité, 'w', encoding='utf-8') as f_out:
                        f_out.write(contenu_traité)

if __name__ == "__main__":
    dossier_source = input("Entrez le chemin du dossier source contenant les fichiers .md : ")
    dossier_destination = input("Entrez le chemin du dossier de destination pour les fichiers traités : ")
    traiter_fichiers(dossier_source, dossier_destination)

```
