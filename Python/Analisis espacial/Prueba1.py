from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
#hist = ImageHistogram(tools.greyScale(imagen1))
#hist.histogramaRGB()
#Pruebas
#num1 = 5
imagenR = tools.convol(imagen1,[[0,1,0],[1,-4,1],[0,1,0]],1)
#imagenR = tools.applyConvolution([[0,1,0],[1,-4,1],[0,1,0]],1,imagen1)
#imagenR = tools.applyMasks(imagen1,"laplace",1)
#imagenR = tools.applyKirsch(imagen1,1)
img.showImagen(imagenR)
#tools.histogramRGB(imagenR)
