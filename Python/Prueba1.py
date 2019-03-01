from imageManager import ImageManager
from imageHistogram import ImageHistogram
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
#hist = ImageHistogram(tools.greyScale(imagen1))
#hist.histogramaRGB()
img.showImagen(tools.tangencialExpand(imagen1))
