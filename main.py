from vegetable import Vegetable
from tomato import Tomato
from onion import Onion
from carrot import Carrot
from gardener import Gardener


gardener = Gardener() 
gardener.add(Tomato()) 
onion = Onion() 
onion.plant(8) 
gardener.add(onion) 
print(gardener.seed)  