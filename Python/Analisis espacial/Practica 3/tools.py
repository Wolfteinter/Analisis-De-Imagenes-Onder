import cv2
import numpy as np
import cv2 as cv
class Tools(object):
    def umbralizacion(self,image,umbral):
        image2 = image.copy()
        width, height = image2.shape[:2]
        for x in range(width):
            for y in range(height):
                r, g, b = image2[x,y]
                avr = np.mean([r,g,b])
                if(avr < int(umbral)):
                    image2[x,y]=(0,0,0)
                else:
                    image2[x,y]=(255,255,255)
        meanX = 1;
        meanY = 1;
        pixelsC = 0;
        for x in range(width):
            for y in range(height):
                r, g, b = image2[x,y]
                if(r == 0 and g == 0 and b==0):
                    meanX += x;
                    meanY += y;
                    pixelsC += 1
        meanX = int(meanX/pixelsC)
        meanY = int(meanY/pixelsC)
        '''
        for x in range(meanX-30,meanX+30):
            for y in range(meanY-30,meanY+30):
                image2[meanX,meanY] = (0,255,0)'''
        cv2.rectangle(image2, (meanX-5, meanY-5), (meanX+5, meanY+5),(0,255,0), 2)


        return image2
