import fitz
import nltk
import string
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.draw.dispersion import dispersion_plot

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

pdf_paths = ['Informes presidenciales\_1_Carlos_Salinas\_1er_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_2do_informe_CS.pdf', 
             'Informes presidenciales\_1_Carlos_Salinas\_3er_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_4to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_5to_informe_CS.pdf',
             'Informes presidenciales\_1_Carlos_Salinas\_6to_informe_CS.pdf']

# Función para extraer texto de un PDF y tokenizarlo
def tokenizar_texto_pdf(pdf_path):
    texto = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            texto += page.get_text()
    tokens = nltk.word_tokenize(texto)
    tokens = [token for token in tokens if token not in string.punctuation]
    return tokens

def graficar(tokens_combinados, palabras_clave):
    dispersion_plot(tokens_combinados, palabras_clave, ignore_case=True, title='Gráfica de Dispersión Léxica')
    plt.gcf().set_size_inches(11, 5)  # Establecer tamaño de la figura
    #plt.tight_layout()  # Ajustar diseño de la figura
    plt.xlabel("Desplazamiento de palabra")
    plt.ylabel("Palabras clave")
    plt.grid(True)

palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                  'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                  'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']

tokens_combinados = []
for pdf_path in pdf_paths:
    tokens_pdf = tokenizar_texto_pdf(pdf_path)
    tokens_combinados.extend(tokens_pdf)
    
#tokens_combinados = list(set(tokens_combinados)) # Eliminar tokens duplicados (representación de tokens unicos)

graficar(tokens_combinados, palabras_clave)
plt.show()