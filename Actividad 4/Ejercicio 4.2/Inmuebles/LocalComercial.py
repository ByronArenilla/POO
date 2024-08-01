from Inmuebles import Local
class LocalComercial(Local):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal,centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self._centroComercial = centroComercial
        self._valorArea = 3000000

    ##Método que muestra en pantalla los datos de un local comercial
    def imprimir(self):
        super().imprimir()
        print (f"Centro comercial = {self._centroComercial}")

    