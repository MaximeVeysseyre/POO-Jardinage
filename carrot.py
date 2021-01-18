from vegetable import Vegetable


class Carrot(Vegetable):

    # def __init__ (self, carrot_variety, seed_number=0):
    #     self.variety = carrot_variety
    #     self.seed = seed_number
    #     print(f"Creating a(n) {carrot_variety} carrot...")

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} carrot(s) seed(s).")