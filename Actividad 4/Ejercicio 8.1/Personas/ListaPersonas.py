
class ListaPersonas:
    def __init__(self):
        # Atributo que identifica una lista de personas
        self.lista_personas = []

    # Método que permite agregar una persona a la lista de personas
    def añadir_persona(self, persona):
        # Añade una persona a la lista
        self.lista_personas.append(persona)

    # Método que permite eliminar una persona de la lista de personas
    # @param i Parámetro que define la posición a eliminar en la lista de personas
    def eliminar_persona(self, i):
        # Verifica que la posición sea válida antes de eliminar
        if 0 <= i < len(self.lista_personas):
            # Elimina la persona en la posición dada
            del self.lista_personas[i]

    # Método que permite eliminar todos los elementos de la lista de personas
    def borrar_lista(self):
        # Limpia la lista eliminando todas las personas
        self.lista_personas.clear()