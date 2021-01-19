from vegetable import Vegetable


class Onion(Vegetable):

    def plant(self, seed_number=0):
        self.seed = seed_number
        print(f"You have planted {seed_number} onion(s) seed(s).")