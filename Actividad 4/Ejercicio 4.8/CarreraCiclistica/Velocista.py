from CarreraCiclistica import Ciclista
class Velocista(Ciclista):
        def __init__(self,identificador,nombre,potenciaPromedio,velocidadPromedio):
            super().__init__(identificador,nombre)
            self.__potenciaPromedio = potenciaPromedio
            self.__velocidadPromedio = velocidadPromedio

        def _getPotenciaPromedio(self):
              return self.__potenciaPromedio
        
        def _SetPotenciaPromedio(self,potenciaPromedio):
              self.__potenciaPromedio = potenciaPromedio
            
        def _getVelocidadPromedio(self):
              return self.__velocidadPromedio
        
        def _setVelocidadPromedio(self,velocidadPromedio):
              self.__velocidadPromedio = velocidadPromedio
        
        #Método que muestra en pantalla los datos de un velocista
        def _imprimir(self):
                super()._imprimir()
                print(f"Potencia promedio: {self._getPotenciaPromedio()}")
                print(f"Velocidad promedio: {self._getVelocidadPromedio()}")

        def _imprimirTipo(self):
              return "Es un velocista"
