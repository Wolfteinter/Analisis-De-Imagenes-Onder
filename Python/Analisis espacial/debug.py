from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
imagenR = tools.debug2(imagen1)
