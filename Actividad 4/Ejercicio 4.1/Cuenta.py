# class Cuenta():
#     def __init__(self,saldo,tasaAnual):
#         self.__saldo = saldo
#         self.__tasaAnual = tasaAnual
#         self.__numeroConsignaciones = 0
#         self.__numeroRetiros = 0
#         self.__comisionMensual = 0

#     ##Método que recibe una cantidad de dinero a consignar y actualiza el saldo de la cuenta

#     def consignar(self, cantidad):
#         self.__saldo += cantidad
#         #Se actualiza el número de consignaciones realizadas en la cuenta
#         self.__numeroConsignaciones += 1

#     ##Método que recibe una cantidad de dinero a retirar y actualiza el saldo de la cuenta

#     def retirar(self, cantidad):
#         nuevoSaldo = self.__saldo - cantidad
#         #Si la cantidad a retirar no supera el saldo, el retiro no se puede realizar
#         if nuevoSaldo >= 0:
#             self.__saldo -= cantidad
#             self.__numeroRetiros += 1
#         else:
#             print ("La cantidad a retirar excede el saldo actual")

#     ##Método que calcula interés mensual de la cuenta a partir de la tasa aplicada
#     def calcularInteres(self):
#         tasaMensual = self.__tasaAnual /12
#         interesMensual = self.__saldo * tasaMensual
#         self.__saldo += interesMensual

#     ##Métdo que genera un extracto aplicando al saldo actual una comisión y calculando intereses

#     def extractoMensual(self):
#         self.__saldo -= self.__comisionMensual
#         self.calcularInteres()
    
#     def __repr__(self):
#         return f'''Saldo = $ {self.__saldo} \n
# Comision mensual = $ {self.__comisionMensual} \n
# Número de transaccionesw = {self.__numeroConsignaciones + self.__numeroRetiros}    '''

class Cuenta:
    def __init__(self, saldo: float, tasaAnual: float):
        self.__saldo = saldo
        self.__tasaAnual = tasaAnual
        self.__numeroConsignaciones = 0
        self.__numeroRetiros = 0
        self.__comisionMensual = 0

    def consignar(self, cantidad: float):
        self.__saldo += cantidad
        self.__numeroConsignaciones += 1

    def retirar(self, cantidad: float):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            self.__numeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual")

    def calcularInteres(self):
        tasaMensual = self.__tasaAnual / 12
        interesMensual = self.__saldo * tasaMensual
        self.__saldo += interesMensual

    def extractoMensual(self):
        self.__saldo -= self.__comisionMensual
        self.calcularInteres()

    # Métodos accesores
    def get_numeroRetiros(self) -> int:
        return self.__numeroRetiros

    def get_comisionMensual(self) -> float:
        return self.__comisionMensual

    def set_comisionMensual(self, comision: float):
        self.__comisionMensual = comision

    def __repr__(self) -> str:
        return f"Saldo = $ {self.__saldo} \nComision mensual = $ {self.__comisionMensual} \nNúmero de transacciones = {self.__numeroConsignaciones + self.__numeroRetiros}"
