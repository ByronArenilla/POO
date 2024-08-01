from Inmuebles import Apartamento
class ApartamentoFamiliar(Apartamento):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños,valorAdministracion):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
        self._valorAdministracion = valorAdministracion
        self._valorArea = 2000000

    #Método que muestra en pantalla los datos de un apartamento Familiar
    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self._valorAdministracion}")
