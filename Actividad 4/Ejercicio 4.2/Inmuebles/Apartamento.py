from Inmuebles import InmuebleVivienda
class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
    
    #Método que muestra en pantalla los datos de un apartamento 
    def imprimir(self):
        super().imprimir()