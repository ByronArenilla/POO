class Cuenta:
    def __init__(self, saldo: float, tasaAnual: float):
        self._saldo = saldo
        self._tasaAnual = tasaAnual
        self._numeroConsignaciones = 0
        self._numeroRetiros = 0
        self._comisionMensual = 0

    def consignar(self, cantidad: float):
        self._saldo += cantidad
        self._numeroConsignaciones += 1

    def retirar(self, cantidad: float):
        if self._saldo >= cantidad:
            self._saldo -= cantidad
            self._numeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual")

    def calcularInteres(self):
        tasaMensual = self._tasaAnual / 12
        interesMensual = self._saldo * tasaMensual
        self._saldo += interesMensual

    def extractoMensual(self):
        self._saldo -= self._comisionMensual
        self.calcularInteres()

    def __repr__(self) -> str:
        return f"Saldo = $ {self._saldo} \nComision mensual = $ {self._comisionMensual} \nNúmero de transacciones = {self._numeroConsignaciones + self._numeroRetiros}"