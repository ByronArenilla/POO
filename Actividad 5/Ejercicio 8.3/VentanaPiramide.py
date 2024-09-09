import tkinter as tk
from tkinter import messagebox
from Piramide import Piramide
import tkinter as tk

class VentanaPiramide(tk.Tk):
    """
    Ventana para ingresar los datos de una pirámide y calcular su volumen y superficie.
    """
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("300x250")
        self.configurar_componentes()

    def configurar_componentes(self):
        # Etiquetas y campos de entrada
        tk.Label(self, text="Base (cm):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20)

        tk.Label(self, text="Altura (cm):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50)

        tk.Label(self, text="Apotema (cm):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80)

        # Botón para calcular
        calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        calcular_btn.place(x=120, y=110)

        # Etiquetas para mostrar resultados
        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=140)

        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)

            self.volumen_lbl.config(text=f"Volumen (cm³): {piramide.calcular_volumen():.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {piramide.calcular_superficie():.2f}")

        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

