from Animales import Canido
class Lobo(Canido):
    def __init__(self):
        super().__init__()

    def getSonido(self):
        return "Aullido"
    
    def getAlimentos(self):
        return "Carnivoro"
    
    def getHabitad(self):
        return "Bosque"
    
    def getNombreCientifico(self):
        return "Cani lupus"