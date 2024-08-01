from Inmuebles import Casa
class CasaRural(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos,distanciaCabera, altitud):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self._distanciaCabera = distanciaCabera
        self._altitud = altitud
        self._valorArea = 1500000

    ##Método que muestra en pantalla los datos de una casa rural
    def imprimir(self):
        super().imprimir()
        print(f"Distancia la cabecera municipal = {self._distanciaCabera} km")
        print(f"Altitud sobre el nivel del mar {self._altitud} metros")

