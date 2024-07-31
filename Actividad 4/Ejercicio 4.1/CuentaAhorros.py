# from Cuenta import Cuenta
# ##Creo una clase CuentaAhorros que hereda de Cuenta
# class CuentaAhorros(Cuenta): #-> Esta clase también hereda todos los métodos
#     def __init__(self, saldo, tasaAnual):
#         super().__init__(saldo, tasaAnual) #Esto es lo que yo quiero que herede}
#         self._activa = False
#         if saldo > 10000:
#             self._Activa = True
    
#     ##Método que recibe una cantidad de dinero a retirar y actualiza el saldo de la cuenta
#     def retirar(self,cantidad):
#         if self._activa:
#             super().retirar(cantidad)

#     ##Método que recibe una cantidad de dinero a consignar y actualiza el saldo de la cuenta
#     def consignar(self, cantidad):
#         if self._Activa:
#             super().consignar(cantidad)
    
#     ##Método que genera el extracto mensual dwe una cuenta de ahorros
#     def extractoMensual(self):
#         #Si la cantidad de retiros es superior a cuatr, se genera una comisión mensual
#         if (self.__numeroRetiros > 4):
#             self.__comisionMensual += (self.__numeroRetiros - 4) * 1000
        
#         super().extractoMensual()
    
#     ##Método que muestra en pantala los datos de una cuenta de ahorros
#     def __repr__(self) -> str:
#         return super().__repr__()

from Cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasaAnual: float):
        super().__init__(saldo, tasaAnual)
        self._activa = saldo > 10000

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)

    def extractoMensual(self):
        # Usa el método accesor para obtener el número de retiros
        if self.get_numeroRetiros() > 4:
            self.set_comisionMensual(self.get_comisionMensual() + (self.get_numeroRetiros() - 4) * 1000)
        super().extractoMensual()

    def __repr__(self) -> str:
        return super().__repr__()  

    


