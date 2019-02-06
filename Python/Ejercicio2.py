from imageManager import ImageManager
from toolsImage import ToolsImage

img = ImageManager()
tools = ToolsImage()

imagen1 = img.openImage()
imagen2 = img.openImage()
tools.chromaKey(imagen1,imagen2,90)
