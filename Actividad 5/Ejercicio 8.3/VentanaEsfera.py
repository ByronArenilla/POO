import tkinter as tk
from tkinter import messagebox
from Esfera import Esfera

class VentanaEsfera(tk.Tk):
    """
    Ventana para ingresar los datos de una esfera y calcular su volumen y superficie.
    """
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("300x200")
        self.configurar_componentes()

    def configurar_componentes(self):
        # Etiquetas y campos de entrada
        tk.Label(self, text="Radio (cm):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=20)

        # Botón para calcular
        calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        calcular_btn.place(x=120, y=50)

        # Etiquetas para mostrar resultados
        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=80)

        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=110)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)

            self.volumen_lbl.config(text=f"Volumen (cm³): {esfera.calcular_volumen():.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {esfera.calcular_superficie():.2f}")

        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


