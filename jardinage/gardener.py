from tomato import Tomato
from onion import Onion
from carrot import Carrot


class Gardener():

    def __init__(self):
        self.list_vegetable_created = []

    def create_vegetable(self, category_choice):

        if category_choice in ['Tomato', 'tomato']:
            self.list_vegetable_created.append(Tomato())

        if category_choice in ['Onion', 'onion']:
            self.list_vegetable_created.append(Onion())

        if category_choice in ['Carrot', 'carrot']:
            self.list_vegetable_created.append(Carrot())