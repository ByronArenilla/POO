from math import pi, pow
from FiguraGeometrica import FiguraGeometrica

class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio  # Atributo que identifica el radio del cilindro
        self.altura = altura  # Atributo que identifica la altura del cilindro
        self.set_volumen(self.calcular_volumen())  # Calcula y establece el volumen
        self.set_superficie(self.calcular_superficie())  # Calcula y establece la superficie

    def calcular_volumen(self):

        return pi * self.altura * pow(self.radio, 2)

    def calcular_superficie(self):

        area_lado = 2 * pi * self.radio * self.altura
        area_base = 2 * pi * pow(self.radio, 2)
        return area_lado + area_base
