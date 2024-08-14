from abc import ABC, abstractmethod
class Animal(ABC):
    @classmethod
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def getNombreCientifico(self):
        pass
    
    @abstractmethod
    def getSonido(self):
        pass

    @abstractmethod
    def getAlimentos(self):
        pass

    @abstractmethod
    def getHabitad(self):
        pass
    