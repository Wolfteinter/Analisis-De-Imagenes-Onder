from imageManager import ImageManager
from imageHistogram import ImageHistogram
img = ImageManager()
imagen = img.openImage()
ih = ImageHistogram(imagen)
img.showImagen(imagen)
ih.histogramaRGB()
ih.histogramaR()
ih.histogramaG()
ih.histogramaB()
#img.saveImage(imagen)
