from Animales import Felino
class Gato(Felino):
    def __init__(self):
        super().__init__()
    def getSonido(self):
        return "Maullido"
    
    def getAlimentos(self):
        return "Ratones"
    
    def getHabitad(self):
        return "Doméstico"
    
    def getNombreCientifico(self):
        return "Felis silvestris catus"