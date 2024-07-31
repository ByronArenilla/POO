from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasaAnual: float):
        super().__init__(saldo, tasaAnual)
        self.sobregiro = 0

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad

        if resultado < 0:
            self.sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)  # Si no hay sobregiro se realiza el retiro normal

    def consignar(self, cantidad: float):
        residuo = self.sobregiro - cantidad

        if self.sobregiro > 0:
            if residuo <= 0:
                self.sobregiro = 0
                self._saldo = -residuo
            else:
                self.sobregiro = residuo
        else:
            super().consignar(cantidad)  # Si no hay sobregiro, se realiza una consignación normal

    def extractoMensual(self):
        super().extractoMensual()

    def __repr__(self) -> str:
        return f'''Saldo = $ {self._saldo} \n
Comisión mensual = $ {self._comisionMensual} \n
Número de transacciones = {self._numeroConsignaciones + self._numeroRetiros} \n
Valor de sobregiro = $ {self.sobregiro}'''
