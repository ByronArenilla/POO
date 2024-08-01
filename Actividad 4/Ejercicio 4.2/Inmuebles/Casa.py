from Inmuebles import InmuebleVivienda
class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños,numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
        self._numeroPisos = numeroPisos

    #Método que muestra en panatalla los datos de una casa
    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numeroPisos}")
        
    