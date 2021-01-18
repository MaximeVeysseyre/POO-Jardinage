from vegetable import Vegetable


class Tomato(Vegetable):

    # def __init__ (self, tomato_variety, seed_number=0):
    #     self.variety = tomato_variety
    #     self.seed = seed_number
    #     print(f"Creating a(n) {tomato_variety} tomato...")

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} tomato(es) seed(s).")