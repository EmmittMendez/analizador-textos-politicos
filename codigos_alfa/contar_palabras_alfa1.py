import fitz
import nltk
from collections import Counter

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def contar_palabras(pdf_paths):
    contador = Counter()                 # Inicializa un contador para contar las palabras
    
    for pdf_path in pdf_paths:
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()           # Obtén el texto de la página

            # Tokenizar el texto y filtrar los signos de puntuación
            tokens = nltk.word_tokenize(text)
            palabras = [token.lower() for token in tokens if token.isalnum()]  # Se mantienen solo las palabras alfanuméricas
            contador.update(palabras)        # Actualiza el contador con las palabras
        doc.close()

    return contador

def obtener_total_palabras(contador):
    total_palabras = sum(contador.values())
    total_palabras_diferentes = len(contador)
    return total_palabras, total_palabras_diferentes

def exportar_a_csv(contador, nombre_archivo):
    # Ordenar el contador por número de repeticiones en orden descendente
    palabras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Guardar palabras ordenadas en un archivo CSV
    with open(nombre_archivo, 'w') as file:
        file.write('Palabra,Conteo\n')
        for palabra, contador in palabras_ordenadas:
            file.write(f'{palabra},{contador}\n')

# Lista de rutas de archivos PDF
pdf_paths = ['Informes presidenciales\_1_Carlos_Salinas\_1er_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_2do_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_3er_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_4to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_5to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_6to_informe_CS.pdf']

resultado = contar_palabras(pdf_paths)
print("Conteo de palabras encontradas:")
for palabra, contador in resultado.items():
    print(f"{palabra}: {contador}")

total_palabras, total_palabras_diferentes = obtener_total_palabras(resultado)
print(f"Total de palabras: {total_palabras}")
print(f"Total de palabras diferentes: {total_palabras_diferentes}")

# Ruta de guardado del archivo CSV
exportar_a_csv(resultado, 'Tablas_conteo\palabras_ordenadas1.csv')
