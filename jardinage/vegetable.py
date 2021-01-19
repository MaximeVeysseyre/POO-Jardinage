from abc import abstractmethod, ABC

class Vegetable(ABC):

    def __init__(self, seed_number=0):
        self.seed = seed_number

    @abstractmethod
    def plant(self, seed_number):
        pass