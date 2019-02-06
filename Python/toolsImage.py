from imageManager import ImageManager
class ToolsImage(object):
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
        img.saveImage(image1)
    def compareInterval(self,color1,color2,intervalo):
        return not(abs(color1-color2)>=intervalo)
    def calculateInteger(self,r,g,b):
        return (r<<16) + (g<<8) + b
    def calculateInteger(self,color):
        return (color[2]<<16) + (color[1]<<8) + color[0]
