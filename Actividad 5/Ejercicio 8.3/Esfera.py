from math import pi, pow
from FiguraGeometrica import FiguraGeometrica

class Esfera(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio  # Atributo que identifica el radio de la esfera
        self.set_volumen(self.calcular_volumen())  # Calcula y establece el volumen
        self.set_superficie(self.calcular_superficie())  # Calcula y establece la superficie

    def calcular_volumen(self):

        return 4/3 * pi * pow(self.radio, 3)

    def calcular_superficie(self):

        return 4 * pi * pow(self.radio, 2)
