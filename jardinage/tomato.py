from vegetable import Vegetable


class Tomato(Vegetable):

    def add_vegetable(self, tomato_number):
        self.vegetable_number += tomato_number
        print(f"You have added {tomato_number} tomato(es) seed(s) to a tomato bag of seeds")