from Cuenta import Cuenta
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente


print ("Cuenta de ahorros: ")
saldoInicialAhorros = float(input("Ingrese el saldo inicial: "))
tasaAhorros = float(input("Ingrese la tasa de interés: "))
cuenta1 = CuentaAhorros(saldoInicialAhorros,tasaAhorros)
canitdadDepositar= float(input(("Ingrese la cantidad a consignar: ")))
cuenta1.consignar(canitdadDepositar)
cantidadRetirar = float(input("Ingrese la cantidad a retirar: "))
cuenta1.retirar(cantidadRetirar)
cuenta1.extractoMensual()
print(cuenta1.__repr__())

