from imageManager import ImageManager
class ToolsImage(object):
    #En las partes que image1 tiene el efecto chroma key es sustituido por image2
    def chromaKey(self,image1,image2,precision):
        img = ImageManager()
        width, height = image1.size
        pixels1 = image1.load()
        pixels2 = image2.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                if(self.compareInterval(r,0,precision) and self.compareInterval(g,255,precision) and self.compareInterval(b,0,precision)):
                    pixels1[x,y]=pixels2[x,y]
        return imagen1
    def simpleUmbralizacion(self,image,umbral):
        width, height = image.size
        pixels1 = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                averange = self.averangeColor(r,g,b)[0]
                if(averange < umbral):
                    pixels1[x,y]=(0,0,0)
                else:
                    pixels1[x,y]=(255,255,255)
        return image
    def greyScale(self,image):
        width, height = image.size
        pixels1 = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                pixels1[x,y] = self.averangeColor(r,g,b)
        return image
    def averangeColor(self,r,g,b):
        averange = int((r+g+b)/3)
        color = (averange,averange,averange)
        return color

    #Evalua si un color esta dentro de un rango de colores
    def compareInterval(self,color1,color2,intervalo):
        return not(abs(color1-color2)>=intervalo)
    #Devuelve el entero que representa al color RGB
    def calculateInteger(self,r,g,b):
        return (r<<16) + (g<<8) + b
    def calculateInteger(self,color):
        return (color[2]<<16) + (color[1]<<8) + color[0]
