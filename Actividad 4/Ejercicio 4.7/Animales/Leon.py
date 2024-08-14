from Animales import Felino
class Leon(Felino):
    def __init__(self):
        super().__init__()

    def getSonido(self):
        return "Rugido"
    
    def getAlimentos(self):
        return "Carnivoro"
    
    def getHabitad(self):
        return "Praderas"
    
    def getNombreCientifico(self):
        return "Panthera leo"