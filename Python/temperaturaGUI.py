from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import ttk
from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage
from PIL import ImageTk

imagenAnchuraMaxima=500
imagenAlturaMaxima=500

root = Tk()
root.title("Analisis de imagenes")
root.config(width=1001, height=600)
img = ImageManager()
tools = ToolsImage()
imagen1 = img.openImage()
#Se modifica la imagen para hacerla de maximo de ancho 500 y maximo de alto de 500
imagen1.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
#Covertir A imagen mostrable
imagenL = ImageTk.PhotoImage(imagen1)
#Primera imagen
viewImagen1 = Label(root,image=imagenL).place(x=0,y=0)
#Segunda imagen
imagenL2 = ImageTk.PhotoImage(tools.displaceTemperature(imagen1,0))
viewImagen2 = Label(root,image=imagenL2)
viewImagen2.place(x=501,y=0)
#Actualizar la imagen del label
def show(val):
    imagenL3 = ImageTk.PhotoImage(tools.displaceTemperature(imagen1,int(val)))
    viewImagen2.configure(image=imagenL3)
    viewImagen2['image']=imagenL3
    viewImagen2.image=imagenL3
#Deslizador
w = Scale(root,from_= -255,to_= 255,orient=HORIZONTAL,length=1000,tickinterval=10,command=show)
w.place(x=0,y=525)
#Guardar la imagen
def guardar():
        imagenL3 = tools.displaceTemperature(imagen1,w.get())
        img.saveImage(imagenL3)
#Boton para guardar
B = Button(root, text ="Guardar Imagen", command = guardar).place(x=450,y=510)
root.mainloop()
