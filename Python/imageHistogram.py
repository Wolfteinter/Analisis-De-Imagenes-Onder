import matplotlib.pyplot as plt
class ImageHistogram(object):
    def __init__(self,imagen):
        self.imagen = imagen
        self.xr=[0]*256
        self.xg=[0]*256
        self.xb=[0]*256
        width, height = self.imagen.size
        pixels = self.imagen.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                self.xr[r] += 1
                self.xg[g] += 1
                self.xb[b] += 1
    def histogramaRGB(self):
        plt.title("RGB")
        plt.xlabel("Valor 0-255")
        plt.ylabel("Frecuencia")
        plt.grid('true')
        plt.bar(range(256),self.xr,color="red")
        plt.bar(range(256),self.xg,color="green")
        plt.bar(range(256),self.xb,color="blue")
        plt.show()
    def histogramaR(self):
        plt.title("Rojos")
        plt.xlabel("Valor 0-255")
        plt.ylabel("Frecuencia")
        plt.grid('true')
        plt.bar(range(256),self.xr,color="red")
        plt.show()
    def histogramaG(self):
        plt.title("Verdes")
        plt.xlabel("Valor 0-255")
        plt.ylabel("Frecuencia")
        plt.grid('true')
        plt.bar(range(256),self.xg,color="green")
        plt.show()
    def histogramaB(self):
        plt.title("Azules")
        plt.xlabel("Valor 0-255")
        plt.ylabel("Frecuencia")
        plt.grid('true')
        plt.bar(range(256),self.xb,color="blue")
        plt.show()
