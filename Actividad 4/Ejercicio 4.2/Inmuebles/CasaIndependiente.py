from Inmuebles import CasaUrbana
class CasaIndependiente(CasaUrbana):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self._valorArea = 3000000

    #Método que muestra en pantalla los datos de una casa independiente
    def imprimir(self):
        super().imprimir()