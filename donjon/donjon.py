from invocateur import Invocateur

class Donjon():

    compteur_zombie = 0
    compteur_squelette = 0
    compteur_vampire = 0
    compteur_type_monstre_different = 0

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
            self.compter_type_monstre(categorie_monstre, nombre_monstre)
        
    def compter_type_monstre(self, categorie_monstre, nombre_monstre):
        if categorie_monstre in ['Zombie', 'zombie']:
            Donjon.compteur_zombie += nombre_monstre
            Donjon.compteur_type_monstre_different += 1

        if categorie_monstre in ['Squelette', 'squelette']:
            Donjon.compteur_squelette += nombre_monstre
            Donjon.compteur_type_monstre_different += 1
        
        if categorie_monstre in ['Vampire', 'vampire']:
            Donjon.compteur_vampire += nombre_monstre
            Donjon.compteur_type_monstre_different += 1
    
    def afficher_compteur_par_type(self):
        print(f"Il y a actuellement {Donjon.compteur_zombie} zombie(s) dans le donjon !")
        print(f"Il y a actuellement {Donjon.compteur_squelette} squelette(s) dans le donjon !")
        print(f"Il y a actuellement {Donjon.compteur_vampire} vampire(s) dans le donjon !")
        print(f"Il y a actuellement {Donjon.compteur_type_monstre_different} types de monstres différents dans le donjon !")

