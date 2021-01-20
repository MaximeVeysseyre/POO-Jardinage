from abc import abstractmethod, ABC


class Monstre(ABC):

    def __init__(self, nombre_monstre=0):
        self.nombre_monstre = nombre_monstre
    
    @abstractmethod
    def ajouter_monstre(self, nombre_monstre):
        pass