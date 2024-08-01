from Inmuebles import Inmueble
from enum import Enum #Esto para poder hacer la enumeración correctamente
class TipoLocal(Enum):
    INTERNO = 1
    CALLE = 2

class Local(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion,tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self._tipoLocal = tipoLocal
    
    #Método que muestra en pantalla los datos de un local
    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {TipoLocal.name}")