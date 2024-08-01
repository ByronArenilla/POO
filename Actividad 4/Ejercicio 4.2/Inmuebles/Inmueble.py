class Inmueble():
    def __init__(self, identificadorInmobiliario, area,direccion):
        self._identificadorInmobiliario = identificadorInmobiliario
        self._area = area
        self._direccion = direccion
        self._precioVenta = None
    
    #Método que a partir del valor del área de un inmueble, calcula su precio de venta
    def calcularPrecioVenta (self,valorArea):
        self._precioVenta = self._area * valorArea
        return self._precioVenta
    
    #Método que muestra en pantalla los datos de un inmueble 
    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificadorInmobiliario}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = {self._precioVenta}")