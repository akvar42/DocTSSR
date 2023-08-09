import PyPDF2
from pdf2image import convert_from_path
import glob
import os
import shutil

#Lire Readme !!!!!!!!!!!!!
#Avincent 05082023

def extract_pdfs(source_folder, target_folder):
    # Trouver tous les fichiers PDF dans le dossier source et les sous-dossiers
    pdf_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    # Copier les fichiers PDF trouvés dans le dossier cible
    for pdf_file in pdf_files:
        shutil.copy(pdf_file, target_folder)
        print(f"Copié: {pdf_file} -> {target_folder}")

def extract_text_and_images(pdf_path, output_folder):
    images = []
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        # Extraire le texte de la page
        page_text = page.extract_text()
        text += page_text + "\n"
        # Convertir la page PDF en image
        image = convert_from_path(pdf_path, first_page=page_num, last_page=page_num + 1)[0]
        # Sauvegarder l'image dans le dossier de sortie
        image_path = os.path.join(output_folder, f"image{page_num}.png")
        image.save(image_path)
        images.append(image_path)
    return text, images

def main():
    source_folder = input("Veuillez entrer le chemin du dossier contenant les PDF: ")
    target_folder = "target_pdfs"
    os.makedirs(target_folder, exist_ok=True)
    # Extraire les PDF du dossier source vers le dossier cible
    extract_pdfs(source_folder, target_folder)

    pdf_paths = glob.glob(os.path.join(target_folder, '*.pdf'))
    for pdf_path in pdf_paths:
        # Créer un dossier avec le nom du PDF
        output_folder = os.path.basename(pdf_path).replace('.pdf', '')
        os.makedirs(output_folder, exist_ok=True)

        # Extraire le texte et les images du PDF
        text, images = extract_text_and_images(pdf_path, output_folder)
        markdown_content = text

        # Ajouter les images au contenu Markdown en utilisant un chemin relatif
        for page_num, image in enumerate(images):
            relative_image_path = f"image{page_num}.png" # Chemin relatif à l'emplacement du fichier Markdown
            markdown_content += f"![Image]({relative_image_path})\n"

        # Sauvegarder le contenu Markdown dans un fichier
        output_file_name = os.path.join(output_folder, os.path.basename(pdf_path).replace('.pdf', '.md'))
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        print(f"Fichier Markdown {output_file_name} généré avec succès.")

if __name__ == "__main__":
    main()
