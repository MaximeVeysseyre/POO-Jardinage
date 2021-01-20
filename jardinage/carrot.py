from vegetable import Vegetable


class Carrot(Vegetable):

    def add_vegetable(self, carrot_number):
        self.vegetable_number += carrot_number
        print(f"You have added {carrot_number} carrot(s) seed(s) to a carrot bag of seeds")