import pandas as pd
from matplotlib import pyplot as plt

df_clave = pd.read_csv("Tablas_conteo\conteo_palabras_clave.csv", encoding='latin1')
#print(df_clave.head()) # Imprime las primeras 5 filas del DataFrame para verificar que se haya cargado correctamente

plt.figure(figsize=(11,5))
plt.bar(df_clave['Palabra clave'], df_clave['Conteo'])
plt.xlabel('Palabra clave')
plt.ylabel('Conteo')
plt.title('Conteo de palabras clave en informes presidenciales')
plt.grid(True)

plt.show()
