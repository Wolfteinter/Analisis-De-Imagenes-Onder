import matplotlib.pyplot as plt
from imageManager import ImageManager
from random import randint
import numpy as np
from numpy import log
class ToolsImage(object):
    #En las partes que image1 tiene el efecto chroma key es sustituido por image2
    def chromaKey(self,image1,image2,precision):
        imagenAux=image.copy()
        imagenAux2=image.copy()
        width, height = imagenAux.size
        pixels1 = imagenAux.load()
        pixels2 = imagenAux2.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                if(self.compareInterval(r,0,precision) and self.compareInterval(g,255,precision) and self.compareInterval(b,0,precision)):
                    pixels1[x,y]=pixels2[x,y]
        return imagenAux
    def displace(self,image,c):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR = r+c
                newR = newR if(newR>0) else 0
                newR = newR if(newR<255) else 255

                newG = g+c
                newG = newG if(newG>0) else 0
                newG = newG if(newG<255) else 255

                newB = b+c
                newB = newB if(newB>0) else 0
                newB = newB if(newB<255) else 255

                pixels[x,y]=(newR,newG,newB)
        return imagenAux
    def linealExpand(self,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        vMin = min(self.calculateMin(self.getHistogramR(image)),self.calculateMin(self.getHistogramG(image)),self.calculateMin(self.getHistogramB(image)))
        vMax = max(self.calculateMax(self.getHistogramR(image)),self.calculateMax(self.getHistogramG(image)),self.calculateMax(self.getHistogramB(image)))
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR =int(self.evaluateValue((255/(vMax-vMin))*(r-vMin)))
                newG = int(self.evaluateValue((255/(vMax-vMin))*(g-vMin)))
                newB = int(self.evaluateValue((255/(vMax-vMin))*(b-vMin)))
                pixels[x,y]=(newR,newG,newB)
        return imagenAux
    def logaritmicExpand(self,j,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR =int(self.evaluateValue((255*log(j+r))/log(256)))
                newG = int(self.evaluateValue((255*log(j+g))/log(256)))
                newB = int(self.evaluateValue((255*log(j+b))/log(256)))
                pixels[x,y]=(newR,newG,newB)
        return imagenAux
    def exponetialExpand(self,z,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR =int(self.evaluateValue(pow((1+z),r)/z))
                newG = int(self.evaluateValue(pow((1+z),g)/z))
                newB = int(self.evaluateValue(pow((1+z),b)/z))
                pixels[x,y]=(newR,newG,newB)
        return imagenAux
    def tangencialExpand(self,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR =int(self.evaluateValue(np.tan(r)))
                newG = int(self.evaluateValue(np.tan(g)))
                newB = int(self.evaluateValue(np.tan(b)))
                pixels[x,y]=(newR,newG,newB)
        return imagenAux
    '''def linealExpand(self,vMin,vMax,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR = self.evaluateValue((255/(vMax-vMin))*(r-vMin))
                newG = self.evaluateValue((255/(vMax-vMin))*(g-vMin))
                newB = self.evaluateValue((255/(vMax-vMin))*(b-vMin))

                pixels[x,y]=(newR,newG,newB)
        return imagenAux'''
    def calculateMin(self,histogram):
        for i in range(len(histogram)):
            if(histogram[i] != 0):
                return i
    def calculateMax(self,histogram):
        for i in range(len(histogram)):
            if(histogram[len(histogram)-1-i] != 0):
                return len(histogram)-1-i
    def evaluateValue(self,value):
        value = value if(value>0) else 0
        value = value if(value<255) else 255
        return value
    def getTrend(self,histogram):
        value = -1
        xValue = -1
        for x in range(len(histogram)):
            if(histogram[x]>value):
                value = histogram[x]
                xValue = x
        return xValue
    def displaceTemperature(self,image,c):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                newR = r+c
                newR = newR if(newR>0) else 0
                newR = newR if(newR<255) else 255


                newB = b-c
                newB = newB if(newB>0) else 0
                newB = newB if(newB<255) else 255

                pixels[x,y]=(newR,g,newB)
        return imagenAux
    def simpleUmbralizacion(self,image,umbral):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels1 = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                averange = self.averangeColor(r,g,b)[0]
                if(averange < int(umbral)):
                    pixels1[x,y]=(0,0,0)
                else:
                    pixels1[x,y]=(255,255,255)
        return imagenAux
    def automaticUmbralizacion(self,image):
        #get the histogram to the image
        values = self.getHistogramToUmbralizacion(image)
        #Select a umbral random
        u0 = randint(0,255)
        while(True):
            #Calculate the left averange
            u1 = self.calculateArea(values,0,u0)
            #Calculate the rigth averange
            u2 = self.calculateArea(values,u0+1,len(values))
            #Calculate the averange between u1 and u2
            averange = int((u1+u2)/2)
            if(u0 == averange):
                break
            u0 = averange
        print(u0)
        return self.simpleUmbralizacion(image,u0)
    def otsuUmbralizacion(self,image):
        values = self.getHistogramToUmbralizacion(image)
        values= np.array(values)
        total = values.sum()
        sumB=0
        wB = 0;
        maximum = 0
        sum1 = np.dot(range(0,256),values)
        for i in range(256):
            wB = wB + values[i]
            wF = total - wB;
            if (wB == 0 and wF == 0):
                continue
            sumB = sumB +  (i-1) * values[i]
            mF = (sum1 - sumB) / wF
            between = wB * wF * ((sumB / wB) - mF) * ((sumB / wB) - mF)
            if (between >= maximum):
                level = i;
                maximum = between;
        print(level)
        return self.simpleUmbralizacion(image,level)
    def greyScale(self,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels1 = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                pixels1[x,y] = self.averangeColor(r,g,b)
        return imagenAux
    def histogramRGB(self,image):
        xr=[0]*256
        xg=[0]*256
        xb=[0]*256
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                xr[r] += 1
                xg[g] += 1
                xb[b] += 1
        plt.title("RGB")
        plt.xlabel("Valor 0-255")
        plt.ylabel("Frecuencia")
        plt.grid('true')
        plt.bar(range(256),xr,color="red")
        plt.bar(range(256),xg,color="green")
        plt.bar(range(256),xb,color="blue")
        plt.show()
    def getHistogramR(self,image):
        xr=[0]*256
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                xr[r] += 1
        return xr
    def getHistogramG(self,image):
        xg=[0]*256
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                xg[g] += 1
        return xg
    def getHistogramB(self,image):
        xb=[0]*256
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                xb[b] += 1
        return xb
    def getHistogramToUmbralizacion(self,image):
        xb=[0]*256
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                xb[b] += 1
        #plt.bar(range(256),xb,color="blue")
        #plt.show()
        return xb
    def calculateArea(self,values,li,ld):
        values = values[li:ld]
        if(len(values) != 0):
             inter = np.array(values)
             ui = int(((inter*range(li,ld)).sum())/inter.sum())-1
             return ui
        return 0
    def negativeImage(self,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels1 = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels1[x,y]
                pixels1[x,y] = (255-r,255-g,255-b)
        return imagenAux
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
