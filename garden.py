from gardener import Gardener

class Garden():

    tomato_counter = 0
    onion_counter = 0
    carrot_counter = 0
    different_vegetable_type_counter = 0

    def __init__(self, number_vegetable_garden=0):
        self.number_vegetable_garden = number_vegetable_garden
        self.vegetable_list = []
 
    def add_vegetable_bag(self, vegetable_bag):
        self.vegetable_list.append(vegetable_bag)
        self.number_vegetable_garden += vegetable_bag.vegetable_number
        print (f"You added a bag of {vegetable_bag.vegetable_number} {vegetable_bag} to the garden!")

    def display_vegetable_number(self):
        print (f"There are {str (self.number_vegetable_garden)} vegetables in the garden!")

    def create_gardener(self):
        self.new_gardener = Gardener()
        print("The garden created a gardener !")
    
    def gardener_add_vegetable(self, vegetable_category, vegetable_number):
        if self.number_vegetable_garden > 30 or vegetable_number > 30:
            print("The garden cannot contain more than 30 vegetables !")
        else:
            self.new_gardener.create_vegetable(vegetable_category)
            self.number_vegetable_garden += vegetable_number
            print(f"Gardener added {vegetable_number} {vegetable_category}(s) to the garden !")
            self.count_vegetable_type(vegetable_category, vegetable_number)
        
    def count_vegetable_type(self, vegetable_category, vegetable_number):
        if vegetable_category in ['Tomato', 'tomato']:
            Garden.tomato_counter += vegetable_number
            Garden.different_vegetable_type_counter += 1

        if vegetable_category in ['Onion', 'onion']:
            Garden.onion_counter += vegetable_number
            Garden.different_vegetable_type_counter += 1
        
        if vegetable_category in ['Carrot', 'carrot']:
            Garden.carrot_counter += vegetable_number
            Garden.different_vegetable_type_counter += 1
    
    def display_type_counter(self):
        print(f"There are currently {Garden.tomato_counter} tomato(es) in the garden !")
        print(f"There are currently {Garden.onion_counter} onion(s) in the garden !")
        print(f"There are currently {Garden.carrot_counter} carrot(s) in the garden !")
        print(f"There are currently {Garden.different_vegetable_type_counter} vegetables types differents in the garden !")