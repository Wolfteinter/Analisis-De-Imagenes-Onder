from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
img.showImagen(tools.displaceTemperature(imagen1,150))
#tools.histogramRGB(imagen1)
#tools.histogramRGB(tools.displace(imagen1,150))
