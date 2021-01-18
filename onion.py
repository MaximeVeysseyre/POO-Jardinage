from vegetable import Vegetable


class Onion(Vegetable):

    # def __init__ (self, onion_variety, seed_number=0):
    #     self.variety = onion_variety
    #     self.seed= seed_number
    #     print(f"Creating a(n) {onion_variety} onion...")

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} onion(s) seed(s).")