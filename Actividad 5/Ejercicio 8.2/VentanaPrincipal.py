import tkinter as tk
from tkinter import messagebox
from Notas import Notas
# Clase para la interfaz gráfica
class VentanaPrincipal:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Notas")
        self.root.geometry("280x380")
        self.root.resizable(False, False)
        
        # Crear los elementos de la interfaz
        self.crear_componentes()

    def crear_componentes(self):
        # Etiquetas y campos para las 5 notas
        self.labels = []
        self.campos = []
        for i in range(5):
            label = tk.Label(self.root, text=f"Nota {i + 1}:")
            label.place(x=20, y=20 + i * 30)
            self.labels.append(label)

            campo = tk.Entry(self.root)
            campo.place(x=105, y=20 + i * 30)
            self.campos.append(campo)

        # Botón para calcular
        self.calcular_btn = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=20, y=170)

        # Botón para limpiar
        self.limpiar_btn = tk.Button(self.root, text="Limpiar", command=self.limpiar)
        self.limpiar_btn.place(x=125, y=170)

        # Etiquetas para mostrar los resultados
        self.promedio_label = tk.Label(self.root, text="Promedio = ")
        self.promedio_label.place(x=20, y=210)

        self.desviacion_label = tk.Label(self.root, text="Desviación = ")
        self.desviacion_label.place(x=20, y=240)

        self.mayor_label = tk.Label(self.root, text="Nota mayor = ")
        self.mayor_label.place(x=20, y=270)

        self.menor_label = tk.Label(self.root, text="Nota menor = ")
        self.menor_label.place(x=20, y=300)

    def calcular(self):
        try:
            # Crear el objeto Notas y asignar valores de las entradas
            notas = Notas()
            for i in range(5):
                notas.listaNotas[i] = float(self.campos[i].get())

            # Calcular y mostrar los resultados
            promedio = notas.calcular_promedio()
            desviacion = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()

            self.promedio_label.config(text=f"Promedio = {promedio:.2f}")
            self.desviacion_label.config(text=f"Desviación = {desviacion:.2f}")
            self.mayor_label.config(text=f"Nota mayor = {mayor}")
            self.menor_label.config(text=f"Nota menor = {menor}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def limpiar(self):
        # Limpiar los campos de texto
        for campo in self.campos:
            campo.delete(0, tk.END)

        # Limpiar los resultados mostrados
        self.promedio_label.config(text="Promedio = ")
        self.desviacion_label.config(text="Desviación = ")
        self.mayor_label.config(text="Nota mayor = ")
        self.menor_label.config(text="Nota menor = ")
