from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import ttk
class AnalisisImagenesGUI(object):
    def __init__(self):
        self.root = Tk()
        self.imagen = None

        self.root.title("Analisis de imagenes")
        self.root.config(width=1000, height=600)
        self.buttonElegir = ttk.Button(self.root, text="Recuperar imagen",
            command=lambda: self.elegirImagen())
        self.buttonElegir.place(x=0, y=0)

        self.buttonMostar = ttk.Button(self.root, text="Abrir imagen",
            command=lambda: self.abrirImagen())
        self.buttonMostar.place(x=120, y=0)

        self.root.mainloop()
    def elegirImagen(self):
        self.root.filename =  filedialog.askopenfilename(initialdir = "/home/wolfteinter/Escritorio",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        #Se retorna la imagen ya lista para ser modificada
        self.imagen = Image.open(str(self.root.filename))
        self.imagen.convert('RGB')
        self.imagen.show()

    def abrirImagen(self):

        self.imagen.show()
analisi=AnalisisImagenesGUI()
