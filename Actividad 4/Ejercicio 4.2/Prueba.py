from Inmuebles import *
aptoFamiliar = ApartamentoFamiliar(103067,120,"Avenida Santander 45-45",3,2,200000)
print ("Datos apartamento")
aptoFamiliar.calcularPrecioVenta(aptoFamiliar._valorArea)
aptoFamiliar.imprimir()

aparaestudio = Apartaestudio(12354,50,"Avenida Caracas 30-15")
print("\nDatos apartamento")
aparaestudio.calcularPrecioVenta(aparaestudio._valorArea)
aparaestudio.imprimir()