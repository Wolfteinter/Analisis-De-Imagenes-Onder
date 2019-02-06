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
def intercambiarPixeles(imagen1,imagen2):
    #Imagen1 tiene el croma
    inter = 80
    width, height = imagen1.size
    pixels1 = imagen1.load()
    pixels2 = imagen2.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels1[x,y]
            if(compararColores(r,70,inter) and compararColores(g,255,inter) and compararColores(b,10,inter)):
                pixels1[x,y]=pixels2[x,y]
    img.saveImage(imagen)

img = ImageManager()
imagen = img.openImage()
imagen2 = img.openImage()
intercambiarPixeles(imagen,imagen2)
