from vegetable import Vegetable


class Onion(Vegetable):

    def add_vegetable(self, onion_number):
        self.vegetable_number += onion_number
        print(f"You have added {onion_number} onion(s) seed(s) to an onion bag of seeds")