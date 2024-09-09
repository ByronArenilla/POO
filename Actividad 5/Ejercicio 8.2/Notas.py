import math

# Clase Notas para almacenar y calcular operaciones con las notas
class Notas:
    def __init__(self):
        # Instancia un array con 5 notas
        self.listaNotas = [0.0] * 5

    def calcular_promedio(self):
        # Calcula el promedio de las notas
        suma = sum(self.listaNotas)
        return suma / len(self.listaNotas)

    def calcular_desviacion(self):
        # Calcula la desviación estándar de las notas
        prom = self.calcular_promedio()
        suma = sum((nota - prom) ** 2 for nota in self.listaNotas)
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        # Calcula el valor menor del array de notas
        return min(self.listaNotas)

    def calcular_mayor(self):
        # Calcula el valor mayor del array de notas
        return max(self.listaNotas)