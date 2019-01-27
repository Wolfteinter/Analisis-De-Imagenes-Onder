from tkinter import *
from tkinter import filedialog
from PIL import Image
class ImageManager(object):
    def openImage(self):
        #Variable para usar el Chooser
        root = Tk()
        #Se abre el Chooser
        #Se obtiene la ruta del la imagen
        root.filename =  filedialog.askopenfilename(initialdir = "/home/wolfteinter/Escritorio",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
        #Se retorna la imagen ya lista para ser modificada
        img = Image.open(str(root.filename))
        #Se combierte a RGB
        return img.convert('RGB')
    def showImagen(self,imagen):
        imagen.show()
