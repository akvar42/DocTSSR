import os
import fitz

# Chemin du répertoire contenant les fichiers PDF
pdf_directory = "C:\\Users\\Guillaume\\OneDrive\\Documents\\ENI TSSR\\Notes\\PDF_TO_MD\\PDF_INPUT"

# Chemin du répertoire de sortie pour les fichiers Markdown
md_output_directory = "C:\\Users\\Guillaume\\OneDrive\\Documents\\ENI TSSR\\Notes\\PDF_TO_MD\\PDF_OUTPUT"

# Parcourir les fichiers PDF dans le répertoire
for pdf_file in os.listdir(pdf_directory):
    if pdf_file.lower().endswith(".pdf"):
        pdf_input_path = os.path.join(pdf_directory, pdf_file)
        md_output_path = os.path.join(md_output_directory, os.path.splitext(pdf_file)[0] + ".md")
        
        doc = fitz.open(pdf_input_path)
        md_content = ""
        is_list = False
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            blocks = page.get_text("blocks")
            
            for b in blocks:
                text = b[4]
                font_size = b[1]
                font_flags = b[5]
                
                # Ignorer les blocs qui semblent être des images
                if "image:" in text.lower():
                    continue
                
                # Détecter les niveaux de titres en fonction de la taille de la police et du style
                if font_size >= 12 and font_flags == 1:  # Vérifier si le texte est en gras
                    md_content += "# " + text.strip() + "\n\n"
                elif font_size >= 10 and font_flags == 1:
                    md_content += "## " + text.strip() + "\n\n"
                elif font_size >= 8 and font_flags == 1:
                    md_content += "### " + text.strip() + "\n\n"
                else:
                    if is_list and text.strip().startswith("-"):
                        md_content += "- " + text.strip()[1:].strip() + "\n"
                    elif is_list:
                        md_content += "  " + text.strip() + "\n"
                    else:
                        md_content += text.strip() + "\n\n"
                
                # Détecter si la ligne est une liste
                if text.strip().startswith("-"):
                    is_list = True
                else:
                    is_list = False
        
        doc.close()
        
        with open(md_output_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)
        
        print("Conversion terminée :", pdf_input_path, "->", md_output_path)


