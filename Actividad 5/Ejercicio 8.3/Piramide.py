from math import pow
from FiguraGeometrica import FiguraGeometrica

class Piramide(FiguraGeometrica):

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base  # Atributo que identifica la base de la pirámide
        self.altura = altura  # Atributo que identifica la altura de la pirámide
        self.apotema = apotema  # Atributo que identifica el apotema de la pirámide
        self.set_volumen(self.calcular_volumen())  # Calcula y establece el volumen
        self.set_superficie(self.calcular_superficie())  # Calcula y establece la superficie

    def calcular_volumen(self):

        return (pow(self.base, 2) * self.altura) / 3

    def calcular_superficie(self):

        area_base = pow(self.base, 2)
        area_lado = 2 * self.base * self.apotema
        return area_base + area_lado
