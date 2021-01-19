from vegetable import Vegetable
from tomato import Tomato
from onion import Onion
from carrot import Carrot
from gardener import Gardener

class GardenerFactory():

    def plant_seed(self, name, number):

        if name == 'Tomato':
            self.number = number

            return Tomato()

        if name == 'Onion':
            self.number = number
            return Onion()

        if name == 'Carrot':
            return Carrot()








class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))