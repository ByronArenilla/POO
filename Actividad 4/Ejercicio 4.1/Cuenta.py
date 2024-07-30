class Cuenta():
    def __init__(self,saldo,tasaAnual):
        self.__saldo = saldo
        self.__tasaAnual = tasaAnual
        self.__numeroConsignaciones = 0
        self.__numeroRetiros = 0
        self.__comisionMensual = 0

    ##Método que recibe una cantidad de dinero a consignar y actualiza el saldo de la cuenta

    def consignar(self, cantidad):
        self.__saldo += cantidad
        #Se actualiza el número de consignaciones realizadas en la cuenta
        self.__numeroConsignaciones += 1

    ##Método que recibe una cantidad de dinero a retirar y actualiza el saldo de la cuenta

    def retirar(self, cantidad):
        nuevoSaldo = self.__saldo - cantidad
        #Si la cantidad a retirar no supera el saldo, el retiro no se puede realizar
        if nuevoSaldo >= 0:
            self.__saldo -= cantidad
            self.__numeroRetiros += 1
        else:
            print ("La cantidad a retirar excede el saldo actual")

    


        
