from VentanaCilindro import VentanaCilindro
from VentanaEsfera import VentanaEsfera
from VentanaPiramide import VentanaPiramide
import tkinter as tk
class VentanaPrincipal(tk.Tk):
    """
    Clase principal que ofrece la interfaz inicial para elegir entre diferentes figuras geométricas.
    """
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x150")
        self.configurar_componentes()

    def configurar_componentes(self):
        # Botón para abrir la ventana del Cilindro
        cilindro_btn = tk.Button(self, text="Cilindro", command=self.abrir_ventana_cilindro)
        cilindro_btn.place(x=100, y=20)

        # Botón para abrir la ventana de la Esfera
        esfera_btn = tk.Button(self, text="Esfera", command=self.abrir_ventana_esfera)
        esfera_btn.place(x=100, y=60)

        # Botón para abrir la ventana de la Pirámide
        piramide_btn = tk.Button(self, text="Pirámide", command=self.abrir_ventana_piramide)
        piramide_btn.place(x=100, y=100)

    def abrir_ventana_cilindro(self):
        """
        Abre la ventana para calcular el volumen y la superficie de un cilindro.
        """
        self.withdraw()  # Oculta la ventana principal
        ventana_cilindro = VentanaCilindro()
        ventana_cilindro.protocol("WM_DELETE_WINDOW", self.mostrar_ventana_principal)

    def abrir_ventana_esfera(self):
        """
        Abre la ventana para calcular el volumen y la superficie de una esfera.
        """
        self.withdraw()  # Oculta la ventana principal
        ventana_esfera = VentanaEsfera()
        ventana_esfera.protocol("WM_DELETE_WINDOW", self.mostrar_ventana_principal)

    def abrir_ventana_piramide(self):
        """
        Abre la ventana para calcular el volumen y la superficie de una pirámide.
        """
        self.withdraw()  # Oculta la ventana principal
        ventana_piramide = VentanaPiramide()
        ventana_piramide.protocol("WM_DELETE_WINDOW", self.mostrar_ventana_principal)

    def mostrar_ventana_principal(self):
        """
        Muestra la ventana principal nuevamente cuando se cierra una ventana de figura.
        """
        self.deiconify()

