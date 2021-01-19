from monstre import Monstre

class Squelette(Monstre):

    def ajouter_monstre(self, nombre_squelette):
        self.nombre_monstre += nombre_squelette
        print(f"Vous avez ajouté {nombre_squelette} squelette(s) à un groupe de squelettes")