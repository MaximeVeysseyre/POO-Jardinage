from tomato import Tomato
from onion import Onion
from carrot import Carrot
from garden import Garden
from gardener import Gardener


garden = Garden()
garden.add_vegetable_bag(Tomato()) 
onion = Onion() 
onion.add_vegetable(8) 
garden.add_vegetable_bag(onion) 
garden.display_vegetable_number()


gardener = Gardener()
gardener.create_vegetable('Tomato')


garden.create_gardener()
garden.gardener_add_vegetable('Tomato',15)
garden.gardener_add_vegetable('Onion',12)
garden.gardener_add_vegetable('Squelette',1)


garden.display_type_counter()