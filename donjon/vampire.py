from monstre import Monstre

class Vampire(Monstre):

    def ajouter_monstre(self, nombre_vampire):
        self.nombre_monstre += nombre_vampire
        print(f"Vous avez ajouté {nombre_vampire} vampire(s) à un groupe de vampires !")