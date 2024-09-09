from Notas import Notas
from VentanaPrincipal import VentanaPrincipal
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = VentanaPrincipal(root)  # Instancia la clase VentanaPrincipal
    root.mainloop()  # Ejecuta la aplicación