import os

from PyPDF2 import PdfWriter, PdfReader
from pdfminer.high_level import extract_text
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def reduce_pdf_size(input_pdf_path, output_pdf_path, quality=75):
    # Extraire le texte du fichier PDF d'entrée
    text = extract_text(input_pdf_path)

    # Créer un fichier PDF temporaire
    temp_pdf_path = 'temp.pdf'
    c = canvas.Canvas(temp_pdf_path, pagesize=letter)

    # Ajouter le texte extrait au PDF temporaire
    c.drawString(100, 750, text)
    c.save()

    # Lire le fichier PDF temporaire et écrire dans le fichier de sortie
    output_pdf = PdfWriter()
    temp_pdf = PdfReader(open(temp_pdf_path, 'rb'))

    for i in range(len(temp_pdf.pages)):
        output_pdf.add_page(temp_pdf.pages[i])

    with open(output_pdf_path, 'wb') as f:
        output_pdf.write(f)

    # Supprimer le fichier PDF temporaire
    os.remove(temp_pdf_path)

# Exemple d'utilisation
input_pdf_path = 'inputes/contrat_oro24_v1.pdf'
output_pdf_path = 'output/document_compressed.pdf'
reduce_pdf_size(input_pdf_path, output_pdf_path)