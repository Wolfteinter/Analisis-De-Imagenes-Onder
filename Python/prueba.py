from imageManager import ImageManager
img = ImageManager()

imagen = img.openImage()
print(img.getDim(imagen))
img.showImagen(imagen)
img.saveImage(imagen)
