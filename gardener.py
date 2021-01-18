from vegetable import Vegetable
from tomato import Tomato
from onion import Onion
from carrot import Carrot


class Gardener():

    def __init__(self, seed_number=0):
        self.seed = seed_number
    
    def _choisir(self, cls):
        return cls

    def add(self, cls):
        self._choisir(cls)
        self.seed =+ cls.seed