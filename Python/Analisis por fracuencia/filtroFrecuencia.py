import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class FiltroFreacuencia(object):
    def __init__(self,ancho,alto):
        self.matriz = np.ones((ancho,alto))
    def generar(self):
        pass
    def toImage(self):
        imagen = Image.fromarray(self.matriz.astype(np.uint8))
        imagen.show()
f = FiltroFreacuencia(256,256)
f.toImage()
