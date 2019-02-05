from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import ttk
class ImageManager(object):
    #Selector de archivos para escojer una imagen
    def openImage(self):
        #Variable para usar el Chooser
        root = Tk()
        root.config(width=0, height=0)
        #Se abre el Chooser
        #Se obtiene la ruta del la imagen
        root.filename =  filedialog.askopenfilename(initialdir = "/home/wolfteinter/Escritorio",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        #Se retorna la imagen ya lista para ser modificada
        img = Image.open(str(root.filename))
        #Se combierte a RGB image
        return img.convert('RGB')
    def showImagen(self,image):
        image.show()
    #regresa las dimenciones de la imagen
    def getDim(self,image):
        return image.size
    #Guarda una imagen con un nombre en especifico
    def saveImage(self,image):
        root = Tk()
        root.config(width=300, height=200)
        # Crear caja de texto.
        entry = ttk.Entry(root)
        # Posicionarla en la ventana.
        texto = ttk.Label(root,text="Nombre: ")
        texto.place(x=10, y=50)
        entry.place(x=60, y=50)
        button = ttk.Button(root, text="Generar Imagen",
            command=lambda: image.save(entry.get()+".png"))
        button.place(x=50, y=100)
        root.mainloop()
        ##icono.save(".png")
