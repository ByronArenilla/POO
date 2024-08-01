from Inmuebles import Casa
class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
    

    ##Método que muestra en pantalla los datos de una casa urbana 
    def imprimir(self):
        super().imprimir()