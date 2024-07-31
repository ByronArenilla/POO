# from Cuenta import Cuenta
# class CuentaCorriente(Cuenta):
#     def __init__(self, saldo, tasaAnual):
#         super().__init__(saldo, tasaAnual)
#         self.sobregiro = 0

#     #Métoodo que recibe una cantidad de dinero a retirar y actualiza el saldo de la cuenta
#     def retirar(self,cantidad):
#         resultado = self.__saldo - cantidad

#         if resultado < 0:
#             self.sobregiro -= resultado
#             self.__saldo = 0
#         else:
#             super().retirar(cantidad) #Si no hay sobre giro se realiza el retiro normal

#     #Método que recibe una cantidad de dinero a consignar y actualiza el saldo de la cuenta
#     def consignar(self, cantidad):
#         residuo = self.sobregiro - cantidad

#         #Si existe sobre giro la cantidad consignada se resta al sobregiro
#         if self.sobregiro > 0:
#             if residuo > 0:
#                 self.sobregiro = 0
#                 self.__saldo = residuo

#             else:
#                 self.sobregiro = -residuo
#                 self.__saldo =0
#         else:
#             super().consignar(cantidad) #si no hay sobregiro, se realiza una consignación normal 
                
#     #Método que genera el extracto mensual de la cuenta
#     def extractoMensual(self):
#         return super().extractoMensual()
    
#     def __repr__(self):
#         return f'''Saldo = $ {self.__saldo} \n
# Comision mensual = $ {self.__comisionMensual} \n
# Número de transacciones = {self.__numeroConsignaciones + self.__numeroRetiros} \n
# Valor de sobregiro = {self.__numeroConsignaciones + self.__numeroRetiros }   '''

from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasaAnual: float):
        super().__init__(saldo, tasaAnual)
        self.sobregiro = 0

    def retirar(self, cantidad: float):
        resultado = self.get_saldo() - cantidad

        if resultado < 0:
            self.sobregiro -= resultado
            self.set_saldo(0)
        else:
            super().retirar(cantidad)  # Si no hay sobregiro se realiza el retiro normal

    def consignar(self, cantidad: float):
        residuo = self.sobregiro - cantidad

        if self.sobregiro > 0:
            if residuo <= 0:
                self.sobregiro = 0
                self.set_saldo(-residuo)
            else:
                self.sobregiro = residuo
        else:
            super().consignar(cantidad)  # Si no hay sobregiro, se realiza una consignación normal

    def extractoMensual(self):
        super().extractoMensual()

    def __repr__(self) -> str:
        return f'''Saldo = $ {self.get_saldo()} \n
Comisión mensual = $ {self.get_comisionMensual()} \n
Número de transacciones = {self.get_numeroConsignaciones() + self.get_numeroRetiros()} \n
Valor de sobregiro = $ {self.sobregiro}'''

    # Métodos accesores adicionales
    def get_saldo(self) -> float:
        return self._Cuenta__saldo

    def set_saldo(self, saldo: float):
        self._Cuenta__saldo = saldo

    def get_numeroConsignaciones(self) -> int:
        return self._Cuenta__numeroConsignaciones

    def get_numeroRetiros(self) -> int:
        return self._Cuenta__numeroRetiros