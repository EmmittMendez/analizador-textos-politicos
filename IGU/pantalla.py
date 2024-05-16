# pantalla_base.py
import tkinter as tk

class PantallaBase(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.salir)

    def salir(self):
        self.destroy()