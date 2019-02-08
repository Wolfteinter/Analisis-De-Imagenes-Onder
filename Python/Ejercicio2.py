from imageManager import ImageManager
from toolsImage import ToolsImage
#Se instancia los objetos
img = ImageManager()
tools = ToolsImage()
#Se abre imagen1
imagen1 = img.openImage()
#Se abre imagen2
imagen2 = img.openImage()
#Se aplica el efecto chroma key
tools.chromaKey(imagen1,imagen2,90)
