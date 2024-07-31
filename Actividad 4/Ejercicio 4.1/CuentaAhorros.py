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
        if self._numeroRetiros > 4:
            self._comisionMensual += (self._numeroRetiros - 4) * 1000
        super().extractoMensual()

    def __repr__(self) -> str:
        return super().__repr__()
