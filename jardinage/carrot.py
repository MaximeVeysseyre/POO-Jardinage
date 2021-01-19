from vegetable import Vegetable


class Carrot(Vegetable):

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} carrot(s) seed(s).")