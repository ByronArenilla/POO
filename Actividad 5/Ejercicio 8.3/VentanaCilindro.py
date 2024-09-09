import tkinter as tk
from tkinter import messagebox
from Cilindro import Cilindro

class VentanaCilindro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("300x200")
        self.configurar_componentes()

    def configurar_componentes(self):
        # Etiquetas y campos de entrada
        tk.Label(self, text="Radio (cm):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=20)

        tk.Label(self, text="Altura (cm):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50)

        # Botón para calcular
        calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        calcular_btn.place(x=120, y=80)

        # Etiquetas para mostrar resultados
        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=110)

        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=140)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)

            self.volumen_lbl.config(text=f"Volumen (cm³): {cilindro.calcular_volumen():.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {cilindro.calcular_superficie():.2f}")

        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

