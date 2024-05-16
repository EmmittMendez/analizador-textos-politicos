# pantalla_principal.py
import tkinter as tk
from pantalla import PantallaBase

class PantallaPrincipal(PantallaBase):
    def __init__(self):
        super().__init__()
        self.titulo = tk.Label(self, text="Pantalla Principal")
        self.boton1 = tk.Button(self, text="Boton 1")
        # Configura los demás widgets aquí

    def mostrar(self):
        self.titulo.pack(pady=15)
        self.boton1.pack(pady=15)
        # Empaqueta los demás widgets aquí