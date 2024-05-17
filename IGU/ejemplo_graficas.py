import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def plot_grafica():
    # Crear datos para graficar
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear la figura y el gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Gráfica de ejemplo')

    # Agregar la figura al canvas de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Gráfica")

# Botón para mostrar la gráfica
boton_grafica = tk.Button(ventana, text="Mostrar Gráfica", command=plot_grafica)
boton_grafica.pack(pady=10)

# Ejecutar el bucle principal de la ventana principal
ventana.mainloop()
