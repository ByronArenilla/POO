from Inmuebles import Local
class Oficina(Local):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal,esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self._esGobierno = esGobierno
        self._valorArea = 3500000

    #Método que muestra en pantalla los datos de una oficina
    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental =  {self._esGobierno}")