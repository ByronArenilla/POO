from CarreraCiclistica import Ciclista
class Escalador(Ciclista):
    def __init__(self,identificador,nombre,aceleracionPromedio,gradoRampa):
        super().__init__(identificador,nombre)
        self.__aceleracionPromedio = aceleracionPromedio
        self.__gradoRampa = gradoRampa

    def _getAceleracionPromedio(self):
        return self.__aceleracionPromedio
    
    def _setAceleracionPromedio(self,aceleracionPromedio):
        self.__aceleracionPromedio = aceleracionPromedio

    def _getGradoRampa(self):
        return self.__gradoRampa
    
    def _setGradoRampa(self,gradoRampa):
        self.__gradoRampa =gradoRampa

    def _imprimir(self):
        super()._imprimir
        print(f"Aceleración promedio: {self._getAceleracionPromedio}")
        print(f"Grado de rampa: {self._getGradoRampa()}")

    def _imprimirTipo(self):
        return "Es un escalador"
    

            