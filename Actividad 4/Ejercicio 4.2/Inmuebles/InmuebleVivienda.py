from Inmuebles import Inmueble
class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion,numeroHabitaciones,numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion)
        self._numeroHabitaciones = numeroHabitaciones
        self._numeroBaños = numeroBaños

    ##Método que muestra en pantalla los datos de un inmueble para la vivienda
    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numeroHabitaciones}")
        print(f"Número de baños = {self._numeroBaños}")



