import matplotlib.pyplot as plt
from imageManager import ImageManager
from random import randint
import numpy as np
from numpy import log,e
import numpy as np
from math import sqrt,pi
#import psycho
#psycho.full()
#CURP = CXGO980405HZSMRN03   002930903891040693
#6349GZ
def createGenerator(n):
    for i in range(0, n):
        yield i
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
    def debug(self,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        #for x in range(3):
            #for y in range(3):
                #print(pixels[x,y],"  ",end="")
            #print("\n")
    def debug2(self,image):
        imagenAux2=image.copy()
        consulta = imagenAux2.load()
        generateSample=self.generateSample
        sample = generateSample(1,1,3,consulta)
        print(self.convolution([[0,1,0],[1,-4,1],[0,1,0]],sample,1))
        #print(sample)
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
        # j es [0,1] 0 es hacia arriba y 1 hacia abajo
    def onderExpand(self,j,i,image):
        imagenAux=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x,y]
                #x*log(pow(x,2))
                #log(255/x)
                #(255-1/(j*sqrt(2*pi))*pow(e,)1*r/20))    Parecida a la gaussiana
                newR = int(self.evaluateValue((pow(-1,j) * (1/(sqrt(2*pi)))*pow(e,1*r/i)) + 255*j ))
                newG = int(self.evaluateValue((pow(-1,j) * (1/(sqrt(2*pi)))*pow(e,1*g/i)) + 255*j ))
                newB = int(self.evaluateValue((pow(-1,j) * (1/(sqrt(2*pi)))*pow(e,1*b/i)) + 255*j ))
                pixels[x,y]=(newR,newG,newB)
        return imagenAux
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
    def convol(self,image, kernel, bias):
        image2=image.copy()
        kernel = np.array(kernel)
        m, n = kernel.shape
        if (m == n):
            y, x = image.size
            pixels = image.load()
            consulta = image2.load()
            y = y - m + 1
            x = x - m + 1
            consulta = np.array(consulta)
            print(consulta)
            for i in range(y):
                for j in range(x):
                    pixels[i,j] = np.sum(consulta[i:i+m][j:j+m]*kernel) + bias

        return image
    #Convolution method
    def simpleConvolution(self,kernel,df,image):
        imagenAux=image.copy()
        imagenAux2=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        consulta = imagenAux2.load()
        tam = len(kernel[0])
        for x in createGenerator(width):
            for y in createGenerator(height):
                initX = x-int(tam/2)
                initY = y-int(tam/2)
                posX=0
                posY=0
                accruedR=0
                accruedG=0
                accruedB=0
                excepts = 0
                for i in createGenerator(pow(tam,2)):
                    try:
                        r,g,b=consulta[initX+posX%tam,initY+posY]
                    except:
                        excepts+=1
                    else:
                        accruedR += r*kernel[posX%tam][posY]/df
                        accruedG += g*kernel[posX%tam][posY]/df
                        accruedB += b*kernel[posX%tam][posY]/df
                        posX+=1
                        if(i%tam==tam-1):
                            posY+=1
                #already i have the kernel
                pixels[x,y]=(int(accruedR),int(accruedG),int(accruedB))
        return imagenAux
    def generateSample(self,x,y,tam,consulta):
        #consulta tiene errores
        '''for i in range(3):
            for j in range(3):
                print(j,i,consulta[j,i])
        print("\n")'''
        #Generate a samble of consulta
        sample = [[None]*tam]*tam
        initX = x-int(tam/2)
        initY = y-int(tam/2)
        posX=0
        posY=0
        for i in createGenerator(pow(tam,2)):
            try:
                color = consulta[(initX+posX%tam),(initY+posY)]
                #print((initX+posX%tam),(initY+posY),color)
            except:
                return None
            else:
                sample[posX%tam][posY] = color
                posX+=1
                if(i%tam==tam-1):
                    posY+=1
        return sample
    def convolution(self,kernel,sample,divisor):
        #the sample an operate with the kernel and apply the divisor
        accruedR=0
        accruedG=0
        accruedB=0
        for i in createGenerator(len(kernel)):
            for j in createGenerator(len(kernel)):
                r,g,b = sample[i][j]
                multipler = kernel[i][j]
                accruedR += r*multipler/divisor
                accruedG += g*multipler/divisor
                accruedB += b*multipler/divisor
        return (int(accruedR),int(accruedG),int(accruedB))

    def applyConvolution(self,kernel,df,image):
        imagenAux=image.copy()
        imagenAux2=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        consulta = imagenAux2.load()
        tam = len(kernel)
        convolution=self.convolution
        generateSample=self.generateSample
        for y in createGenerator(height):
            for x in createGenerator(width):
                #aqui esta el error
                sample = generateSample(x,y,tam,consulta)
                if(sample != None):
                    pixels[x,y]=convolution(kernel,sample,df)
                else:
                    pixels[x,y]=(0,0,0)
        return imagenAux

    def applyKirsch(self,image,divisor):
        imagenAux=image.copy()
        imagenAux2=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        consulta = imagenAux2.load()
        convolution=self.convolution
        generateSample=self.generateSample
        convolutionKirsch=self.convolutionKirsch
        for x in createGenerator(width):
            for y in createGenerator(height):
                sample=generateSample(x,y,3,consulta)
                if(sample!=None):
                    pixels[x,y]=convolutionKirsch(sample,divisor)
                else:
                    pixels[x,y]=(255,255,255)
        return imagenAux

    def convolutionKirsch(self,sample,divisor):
        arregloMascaras = self.getKernel("Kirsch")
        mayorR = -1
        mayorG = -1
        mayorB = -1
        convolution=self.convolution
        for i in createGenerator(8):
            r,g,b = convolution(arregloMascaras[i],sample,divisor)
            if(r > mayorR):
                mayorR = r
            if(g > mayorG):
                mayorG = g
            if(b > mayorB):
                mayorB = b
        return (r,g,b)
    def applyMasks(self,image,name,df):
        imagenAux=image.copy()
        imagenAux2=image.copy()
        width, height = imagenAux.size
        pixels = imagenAux.load()
        consulta = imagenAux2.load()
        arregloMascaras = self.getKernel(name)
        tam = len(arregloMascaras[0])
        for x in range(width):
            for y in range(height):
                mayorR = -1
                mayorG = -1
                mayorB = -1
                for z in range(len(arregloMascaras)):
                    #Convolutionnp.range
                    initX = x-int(tam/2)
                    initY = y-int(tam/2)
                    posX=0
                    posY=0
                    accruedR=0
                    accruedG=0
                    accruedB=0
                    excepts = 0
                    for i in range(pow(tam,2)):
                        try:
                            r,g,b=consulta[initX+posX%tam,initY+posY]
                        except:
                            excepts+=1
                        else:
                            accruedR += r*arregloMascaras[z][posX%tam][posY]/df
                            accruedG += g*arregloMascaras[z][posX%tam][posY]/df
                            accruedB += b*arregloMascaras[z][posX%tam][posY]/df
                            posX+=1
                            if(i%tam==tam-1):
                                posY+=1
                    if(accruedR > mayorR):
                        mayorR = accruedR
                    if(accruedG > mayorG):
                        mayorG = accruedG
                    if(accruedB > mayorB):
                        mayorB = accruedB
                pixels[x,y] = (int(mayorR),int(mayorG),int(mayorB))
        return imagenAux
    def getKernel(self,name):
        if(name=="Kirsch"):
            kirsch1 = [[-3, -3, 5],[-3, 0, 5],[-3, -3, 5]]
            kirsch2 = [[-3, 5, 5],[-3, 0, 5],[-3, -3, -3]]
            kirsch3 = [[5, 5, 5],[-3, 0, -3],[-3, -3, -3]]
            kirsch4 = [[5, 5, -3],[5, 0, -3],[-3, -3, -3]]
            kirsch5 = [[5, -3, -3],[5, 0, -3],[5, -3, -3]]
            kirsch6 = [[-3, -3, -3],[5, 0, -3],[5, 5, -3]]
            kirsch7 = [[-3, -3, -3],[-3, 0, -3],[5, 5, 5]]
            kirsch8 = [[-3, -3, -3],[-3, 0, 5],[-3, 5, 5]]
            arregloMascaras = [kirsch1,kirsch2,kirsch3,kirsch4,kirsch5,kirsch6,kirsch7,kirsch8]
            return arregloMascaras
        if(name=="pixelDiference"):
            pixelDiferenceGx = [[0,0,0],[0,1,-1],[0, 0, 0]]
            pixelDiferenceGy = [[0, -1, 0],[0, 1, 0],[0, 0, 0]]
            arregloMascaras = [pixelDiferenceGx,pixelDiferenceGy]
            return arregloMascaras
        if(name=="pixelSepareteDiference"):
            pixelSepareteDiferenceGx = [[0,0,0],[1, 0,-1],[0, 0, 0]]
            pixelSepareteDiferenceGy = [[0, -1, 0],[0,0,0],[0,1,0]]
            arregloMascaras = [pixelSepareteDiferenceGx,pixelSepareteDiferenceGy]
            return arregloMascaras
        if(name=="prewitt"):
            prewittGx = [[1,0,-1],[1,0,-1],[1,0,-1]]
            prewittGy = [[-1,-1,-1],[0,0,0],[1, 1, 1]]
            arregloMascaras = [prewittGx,prewittGy]
            return arregloMascaras
        if(name=="sobel"):
            sobelGx = [[1,0,-1],[2,0,-2],[1,0,-1]]
            sobelGy = [[-1,-2,-1],[0,0,0],[1,2,1]]
            arregloMascaras = [sobelGx,sobelGy]
            return arregloMascaras
        if(name=="roberts"):
            robertsGx = [[0,0,-1],[0,1,0],[0,0,0]]
            robertsGy = [[-1,0,0],[0,1,0],[0,0,0]]
            arregloMascaras = [robertsGx,robertsGy]
            return arregloMascaras
        if(name=="laplace"):
            return [[0,1,0],[1,-4,1],[0,1,0]]


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
        for i in range(1,256):
            wB = wB + values[i]
            wF = total - wB;
            if (wB > 0 and wF > 0):
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
        #plt.grid('true')
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
