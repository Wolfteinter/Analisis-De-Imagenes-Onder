import numpy as np
class FiltroFreacuencia(object):
    def __init__(self,ancho,alto):
        self.matriz = np.ones((2, 3))
    def generar(self):
        pass
    def toImage(self):
        imagen = Image.fromarray(self.matriz.astype(np.uint8))
        imagen.show()
f = FiltroFreacuencia(16,16)
f.toImage()
