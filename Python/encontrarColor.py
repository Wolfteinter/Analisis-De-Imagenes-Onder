from imageManager import ImageManager
def compararColores(color1,color2,intervalo):
    return not(abs(color1-color2)>=intervalo)
def calcularEntero(r,g,b):
    return (r<<16) + (g<<8) + b
def cambiarPixeles(imagen,color,inter):
    width, height = imagen.size
    pixels = imagen.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            if(compararColores(r,color[0],inter) and compararColores(g,color[1],inter) and compararColores(b,color[2],inter)):
                pixels[x,y]=(255,255,0)
    img.saveImage(imagen)
def cambiarPixeles2(imagen,color,inter):
    width, height = imagen.size
    pixels = imagen.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            if(compararColores(calcularEntero(r,g,b),calcularEntero(color[0],color[1],color[2]),inter)):
                pixels[x,y]=(255,255,0)
    img.saveImage(imagen)

img = ImageManager()
imagen = img.openImage()
cambiarPixeles2(imagen,(63,11,1),100)
print(img.getDim(imagen))
img.showImagen(imagen)
