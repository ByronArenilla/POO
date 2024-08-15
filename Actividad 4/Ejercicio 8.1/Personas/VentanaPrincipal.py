import tkinter as tk
from .ListaPersonas import ListaPersonas
from Personas import Persona

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        # Llama al constructor de la clase padre (tk.Tk)
        super().__init__()

        # Crea una instancia de ListaPersonas
        self.lista = ListaPersonas()
        
        # Configuración básica de la ventana principal
        self.title("Personas")  # Establece el título de la ventana
        self.geometry("270x350")  # Establece el tamaño de la ventana
        self.resizable(False, False)  # No permite cambiar el tamaño de la ventana

        # Definición y ubicación de los elementos gráficos en la ventana
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.place(x=20, y=20)  # Coloca la etiqueta de nombre
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=105, y=20)  # Coloca el campo de entrada para el nombre

        self.label_apellidos = tk.Label(self, text="Apellidos:")
        self.label_apellidos.place(x=20, y=50)  # Coloca la etiqueta de apellidos
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=105, y=50)  # Coloca el campo de entrada para los apellidos

        self.label_telefono = tk.Label(self, text="Teléfono:")
        self.label_telefono.place(x=20, y=80)  # Coloca la etiqueta de teléfono
        self.campo_telefono = tk.Entry(self)
        self.campo_telefono.place(x=105, y=80)  # Coloca el campo de entrada para el teléfono

        self.label_direccion = tk.Label(self, text="Dirección:")
        self.label_direccion.place(x=20, y=110)  # Coloca la etiqueta de dirección
        self.campo_direccion = tk.Entry(self)
        self.campo_direccion.place(x=105, y=110)  # Coloca el campo de entrada para la dirección

        self.boton_añadir = tk.Button(self, text="Añadir", command=self.añadir_persona)
        self.boton_añadir.place(x=105, y=150)  # Coloca el botón para añadir personas

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_persona)
        self.boton_eliminar.place(x=20, y=280)  # Coloca el botón para eliminar personas

        self.boton_borrar_lista = tk.Button(self, text="Borrar Lista", command=self.borrar_lista)
        self.boton_borrar_lista.place(x=120, y=280)  # Coloca el botón para borrar la lista completa

        self.lista_nombres = tk.Listbox(self)
        self.lista_nombres.place(x=20, y=190, width=220, height=80)  # Coloca la lista gráfica de personas

    # Método que añade una persona a la lista y a la interfaz gráfica
    def añadir_persona(self):
        # Crea una nueva persona con los datos de los campos de texto
        persona = Persona(self.campo_nombre.get(), self.campo_apellidos.get(), self.campo_telefono.get(), self.campo_direccion.get())
        # Añade la persona a la lista de personas
        self.lista.añadir_persona(persona)
        # Añade la persona a la lista gráfica
        self.lista_nombres.insert(tk.END, f"{persona.nombre} - {persona.apellidos} - {persona.telefono} - {persona.direccion}")
        # Limpia los campos de entrada
        self.limpiar_campos()

    # Método que elimina la persona seleccionada en la lista gráfica y de la lista de personas
    def eliminar_persona(self):
        seleccion = self.lista_nombres.curselection()  # Obtiene la selección actual en la lista gráfica
        if seleccion:
            self.lista.eliminar_persona(seleccion[0])  # Elimina la persona en la posición seleccionada
            self.lista_nombres.delete(seleccion[0])  # Elimina la persona de la lista gráfica

    # Método que borra todas las personas de la lista y de la interfaz gráfica
    def borrar_lista(self):
        self.lista.borrar_lista()  # Borra todas las personas de la lista
        self.lista_nombres.delete(0, tk.END)  # Borra todos los elementos de la lista gráfica

    # Método que limpia los campos de entrada de la ventana
    def limpiar_campos(self):
        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_telefono.delete(0, tk.END)
        self.campo_direccion.delete(0, tk.END)