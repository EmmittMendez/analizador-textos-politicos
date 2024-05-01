import fitz

def resaltar_palabras_clave(pdf_path, palabras_clave, resaltador_color=(1, 1, 0)):  # Amarillo por defecto
    doc = fitz.open(pdf_path)
    for page in doc:
        for palabra_clave in palabras_clave:
            ocurrencias = page.search_for(palabra_clave)
            for bbox in ocurrencias:
                highlight = page.add_highlight_annot(bbox)
                highlight.set_colors(stroke=resaltador_color)

    doc.save(pdf_path + "_resaltado.pdf")
    doc.close()

# Ejemplo de uso
pdf_path = 'documentos\prueba.pdf'
palabras_clave = ['nave', 'objeto', 'laseres', 'clase', 'funcion']  # Lista de palabras clave a resaltar
resaltar_palabras_clave(pdf_path, palabras_clave)
