from CasaUrbana import CasaUrbana
class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos,valorAdministracion,tienePiscina,tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self._valorArea = 2500000
        self._valorAdministracion = valorAdministracion
        self._tienePiscina = tienePiscina
        self._tieneCamposDeportivos = tieneCamposDeportivos

    #Método que muestra en pantalla los datos de una casa en conjunto cerrado
    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración =  {self._valorAdministracion}")
        print(f"Tiene piscina? = {self._tienePiscina}")
        print (f"Tiene campos deportivos = {self._tieneCamposDeportivos}")
        