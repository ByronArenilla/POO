from Inmuebles import Apartamento
class Apartaestudio(Apartamento):
    def __init__(self, identificadorInmobiliario, area, direccion, ):
        super().__init__(identificadorInmobiliario, area, direccion, 1, 1)
        self._valorArea = 1500000

    def imprimir(self):
        super().imprimir()