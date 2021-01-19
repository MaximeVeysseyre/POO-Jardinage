from invocateur import Invocateur

class Donjon():

    def __init__(self, nombre_monstre_donjon=0):
        self.nombre_monstre_donjon = nombre_monstre_donjon
        self.liste_monstre = []
 
    def ajouter_groupe_monstre(self, groupe_monstre):
        self.liste_monstre.append(groupe_monstre)
        self.nombre_monstre_donjon += groupe_monstre.nombre_monstre
        print(f"Vous avez ajouté un groupe de {groupe_monstre.nombre_monstre} {groupe_monstre} au donjon !")

    def afficher_nombre_monstre(self):
        print(f"Il y a {str(self.nombre_monstre_donjon)} monstres dans le donjon !")

    def creation_invocateur(self):
        self.nouvel_invocateur = Invocateur()
        print("Le donjon a créé un invocateur !")
    
    def invocateur_ajoute_monstre(self, categorie_monstre, nombre_monstre):
        if self.nombre_monstre_donjon > 30 or nombre_monstre > 30:
            print("Le donjon ne peut pas contenir plus de 30 monstres !")
        else:
            self.nouvel_invocateur.creation_monstre(categorie_monstre)
            self.nombre_monstre_donjon += nombre_monstre
            print(f"L'invocateur a ajouté {nombre_monstre} {categorie_monstre}(s) au donjon !")

