from Animales import Canido
class Perro(Canido):
    def __init__(self):
        super().__init__()

    def getSonido(self):
        return "Ladrido"
    
    def getAlimentos(self):
        return "Carnivoro"
    
    def getHabitad(self):
        return "Domestico"
    
    def getNombreCientifico(self):
        return "Canis lupus familiaris"
    
