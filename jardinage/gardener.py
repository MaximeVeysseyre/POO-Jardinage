from vegetable import Vegetable
from tomato import Tomato
from onion import Onion
from carrot import Carrot


class Gardener():

    def __init__(self, seed_number=0):
        self.seed = seed_number
    
    def _choose(self, class):
        return class

    def add(self, class):
        self._choose(class)
        self.seed =+ class.seed

