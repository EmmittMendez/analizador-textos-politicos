from tkinter import Toplevel, Label

class CargarInforme():
        
        def __init__(self, master=None):
            self.master = master
            self.new_window = Toplevel(self.master)
            self.new_window.geometry('500x500')
            self.new_window.wm_title("Cargar informes")
            self.create_widgets()
        
        def create_widgets(self):
            self.titulo = Label(self.new_window, text='Cargar informes', padx=15, pady=15, font=('Helvetica', 20), fg='Blue')
            self.titulo.pack()
            self.new_window.mainloop()