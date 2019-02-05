from imageManager import ImageManager
import matplotlib.pyplot as plt

img = ImageManager()
xr=[0]*256
xg=[0]*256
xb=[0]*256
imagen = img.openImage()
width, height = imagen.size
pixels = imagen.load()
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x,y]
        xr[r] += 1
        xg[g] += 1
        xb[b] += 1
plt.hist(pixels)
plt.show()
