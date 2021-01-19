from squelette import Squelette
from vampire import Vampire
from zombie import Zombie
from donjon import Donjon
from invocateur import Invocateur


donjon = Donjon()
donjon.ajouter_groupe_monstre(Vampire()) 
zombie = Zombie() 
zombie.ajouter_monstre(8) 
donjon.ajouter_groupe_monstre(zombie) 
donjon.afficher_nombre_monstre()


invocateur = Invocateur()
invocateur.creation_monstre('Zombie')


donjon.creation_invocateur()
donjon.invocateur_ajoute_monstre('Zombie',15)
donjon.invocateur_ajoute_monstre('Zombie',15)
donjon.invocateur_ajoute_monstre('Squelette',1)
