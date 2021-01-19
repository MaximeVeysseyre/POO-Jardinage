from vegetable import Vegetable


class Tomato(Vegetable):

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} tomato(es) seed(s).")