from tkinter import Frame, Tk, Button, Toplevel
from crear_informe import CargarInforme  # Importar la nueva clase

class PantallaPrincipal(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Crear los cuatro botones principales
        self.boton1 = Button(self, text="Cargar informes", command=self.cargar_informes, padx=60, pady=15)
        self.boton1.pack()
        self.boton2 = Button(self, text="Mostrar estadísticas generales", command=lambda: print("Botón 2 presionado"), padx=60, pady=20)
        self.boton2.pack()
        self.boton3 = Button(self, text="Mostrar/Comparar gráficas", command=lambda: print("Botón 3 presionado"), padx=60, pady=20)
        self.boton3.pack()
        self.boton4 = Button(self, text="Salir del programa", command=self.salir, padx=60, pady=20)
        self.boton4.pack()

    def cargar_informes(self):
        # Ocultar la ventana principal
        self.master.withdraw()
        # Crear una nueva ventana
        self.new_window = Toplevel(self.master)
        CargarInforme(self.new_window)

    def salir(self):
        self.master.destroy()


root = Tk()
root.geometry('500x500')
root.wm_title("Analizador de informes políticos")
app = PantallaPrincipal(root)
app.mainloop()