from monstre import Monstre

class Zombie(Monstre):

    def ajouter_monstre(self, nombre_zombie):
        self.nombre_monstre += nombre_zombie
        print(f"Vous avez ajouté {nombre_zombie} zombie(s) à un groupe de zombies !")