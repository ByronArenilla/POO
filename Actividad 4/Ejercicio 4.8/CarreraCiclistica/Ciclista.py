from abc import ABC, abstractmethod
class Ciclista():
        @classmethod
        @abstractmethod
        def __init__(self,identificador,nombre) :
            self.__identificador = identificador
            self.__nombre = nombre
            self.__tiempoAcumulado = 0

        #Método abstracto que muestra en pantalla el tipo específico de un ciclista
        @abstractmethod
        def imprimirTipo(self):
              pass
        
        #Método que devuelve el identificador de un ciclista
        def _getIdentificador(self):
              return self.__identificador

        #Método que establece el identificador de un ciclista
        def  __setIdentificador(self, identificador):
              self.__identificador = identificador 

        def _getNombre(self):
              return  self.__nombre
        
        def _setNombre(self, nombre):
              self.__nombre = nombre

        
        def _getPosicionGeneral(self, posicionGeneral):
              return posicionGeneral
        
        def _setPosicionGeneral(self, posicionGeneral):
              posicionGeneral = posicionGeneral
        
        def _getTiempoAcumulado(self):
              return self.__tiempoAcumulado
        
        def _setTiempoAcumulado(self, tiempoAcumulado):
              self.__tiempoAcumulado = tiempoAcumulado

        #Método que muestra en pantalla los datos de un ciclista
        def _imprimir(self):
              print(f"Identificador : {self._getIdentificador()}")
              print(f"Nombre: {self._getNombre()}")
              print(f"Tiempo acumulado: {self._getTiempoAcumulado()}")
              


        