import fitz
from collections import Counter

def contar_palabras_clave(pdf_path, palabras_clave):
    contador = Counter()  # Inicializa un contador para contar las palabras clave

    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text()  # Obtén el texto de la página
        for palabra_clave in palabras_clave:
            contador[palabra_clave] += text.lower().count(palabra_clave.lower())  # Contabiliza las ocurrencias de la palabra clave

    doc.close()

    return contador

# Ejemplo de uso
pdf_path = 'documentos\prueba.pdf'
palabras_clave = ['nave', 'pygame', 'funcion', 'objeto']  # Lista de palabras clave a buscar y contar

resultado = contar_palabras_clave(pdf_path, palabras_clave)
print("Conteo de palabras clave encontradas:")
for palabra_clave, contador in resultado.items():
    print(f"{palabra_clave}: {contador}")
