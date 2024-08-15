from CarreraCiclistica import Ciclista
class ContraRelojista(Ciclista):
    def __init__(self,identificador,nombre,velocidadMaxima):
        super().__init__(identificador,nombre)
        self.__velocidadMaxima = velocidadMaxima

    def _getVelocidadMaxima(self):
            return self.__velocidadMaxima
    
    def _setVelocidadMaxima(self,velocidadMaxima):
         self.__velocidadMaxima = velocidadMaxima

    def _imprimir(self):
        super()._imprimir()
        print(f"Aceleracion promedio: {self._getVelocidadMaxima()}")

    def _imprimirTipo(self):
         return "Es un contrarrelojista"

