from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
img.saveImage(tools.simpleUmbralizacion(tools.greyScale(imagen1),200))
