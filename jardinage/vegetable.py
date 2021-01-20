from abc import abstractmethod, ABC


class Vegetable(ABC):

    def __init__(self, vegetable_number=0):
        self.vegetable_number = vegetable_number
    
    @abstractmethod
    def add_vegetable(self, vegetable_number):
        pass