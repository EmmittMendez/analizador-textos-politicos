import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.messagebox as messagebox
import PyPDF2

class Window1(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('Ventana 1')
        self.parent = parent
        self.parent.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

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

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Crear un botón para seleccionar un archivo PDF
        self.select_file_button = ttk.Button(self, text="Seleccionar archivo PDF", command=self.select_file)
        self.select_file_button.pack(pady=20)

        # Crear una etiqueta y un campo de texto para el presidente
        self.president_label = ttk.Label(self, text="Presidente:")
        self.president_label.pack(pady=10)
        self.president_entry = ttk.Entry(self)
        self.president_entry.pack(pady=10)

        # Crear una etiqueta y un campo de texto para el año de sexenio
        self.year_label = ttk.Label(self, text="Año de sexenio:")
        self.year_label.pack(pady=10)
        self.year_entry = ttk.Entry(self)
        self.year_entry.pack(pady=10)

    def select_file(self):
        # Abrir el explorador de archivos y seleccionar un archivo PDF
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            # Mostrar un cuadro de mensaje
            messagebox.showinfo("Archivo seleccionado", "El archivo se ha subido correctamente.")
            

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_file = file_path
            self.read_pdf_file()

    def read_pdf_file(self):
        with open(self.pdf_file, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            self.pdf_data = {}
            self.pdf_data['presidente'] = reader.getDocumentInfo().title
            self.pdf_data['año_de_sexenio'] = reader.getDocumentInfo().subject

    def on_close(self):
        self.destroy()
        self.parent.deiconify()