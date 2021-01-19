from zombie import Zombie
from squelette import Squelette
from vampire import Vampire

class Invocateur():

    def __init__(self):
        self.liste_monstre_cree = []

    def creation_monstre(self, choix_categorie):

        if choix_categorie in ['Zombie', 'zombie']:
            self.liste_monstre_cree.append(Zombie())

        if choix_categorie in ['Squelette', 'squelette']:
            self.liste_monstre_cree.append(Squelette())

        if choix_categorie in ['Vampire', 'vampire']:
            self.liste_monstre_cree.append(Vampire())
