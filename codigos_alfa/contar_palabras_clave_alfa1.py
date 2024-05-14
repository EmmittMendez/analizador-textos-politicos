import fitz
import pandas as pd
from collections import Counter

def contar_palabras_clave(pdf_paths, palabras_clave):
    contador_total = Counter()  # Inicializa un contador para contar las palabras clave en todos los PDFs

    for pdf_path in pdf_paths:
        contador = Counter()  # Inicializa un contador para contar las palabras clave en el PDF actual

        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()  # Obtén el texto de la página
            for palabra_clave in palabras_clave:
                contador[palabra_clave] += text.lower().count(palabra_clave.lower())  # Contabiliza las ocurrencias de la palabra clave en la página

        doc.close()

        # Actualiza el contador total con las ocurrencias del PDF actual
        contador_total.update(contador)

    return contador_total

def exportar_a_csv(contador, nombre_archivo):
    # Ordenar el contador por número de repeticiones en orden descendente
    df = pd.DataFrame.from_dict(contador, orient='index', columns=['Conteo']).reset_index()
    df.columns = ['Palabra clave', 'Conteo']
    df.to_csv(nombre_archivo)
    
    palabras_clave_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Guardar palabras clave ordenadas en un archivo CSV
    with open(nombre_archivo, 'w') as file:
        file.write('Palabra clave,Conteo\n')
        for palabra_clave, contador in palabras_clave_ordenadas:
            file.write(f'{palabra_clave},{contador}\n')

# Lista de rutas de archivos PDF
pdf_paths = ['Informes presidenciales\_1_Carlos_Salinas\_1er_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_2do_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_3er_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_4to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_5to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_6to_informe_CS.pdf']

# Lista de palabras clave a buscar
palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                  'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                  'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']  

resultado = contar_palabras_clave(pdf_paths, palabras_clave)
print("Conteo de palabras clave encontradas:")
for palabra_clave, contador in resultado.items():
    print(f"{palabra_clave}: {contador}")

# Ruta de guardado del archivo CSV
exportar_a_csv(resultado, 'Tablas_conteo\conteo_palabras_clave.csv')