from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import ttk
from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage
from PIL import ImageTk

root = Tk()
root.title("Analisis de imagenes")
root.config(width=1000, height=600)
img = ImageManager()
tools = ToolsImage()
imagen1 = img.openImage()
viewImagen1 = Label(root,image=ImageTk.PhotoImage(tools.simpleUmbralizacion(imagen1,200))).pack()
w = Scale(root,from_= 0,to_= 255,orient=HORIZONTAL,length=1000,tickinterval=10)
w.pack()
root.mainloop()
