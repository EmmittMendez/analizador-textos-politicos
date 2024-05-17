import tkinter as tk
from tkinter import ttk

from Window1 import Window1
from Window2 import Window2
from Window3 import Window3

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ventana Principal')

        # Centrar la ventana
        window_width = 500
        window_height = 500

        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición de la ventana
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Posicionar la ventana
        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.resizable(False, False)

        self.button1 = ttk.Button(self, text="Abrir ventana 1", command=self.open_window1)
        self.button1.pack(pady=20)

        self.button2 = ttk.Button(self, text="Abrir ventana 2", command=self.open_window2)
        self.button2.pack(pady=20)

        self.button3 = ttk.Button(self, text="Abrir ventana 3", command=self.open_window3)
        self.button3.pack(pady=20)

        self.quit_button = ttk.Button(self, text="Salir", command=self.quit)
        self.quit_button.pack(pady=20)
    def open_window1(self):
        self.new_window = Window1(self)

    def open_window2(self):
        self.new_window = Window2(self)

    def open_window3(self):
        self.new_window = Window3(self)

#class Window1(tk.Toplevel):
#    def __init__(self):
#        super().__init__()
#        self.title('Ventana 1')

#class Window2(tk.Toplevel):
#    def __init__(self):
#        super().__init__()
#        self.title('Ventana 2')

#class Window3(tk.Toplevel):
#    def __init__(self):
#        super().__init__()
#        self.title('Ventana 3')

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()