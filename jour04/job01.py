class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self):
        print("Âge :", self.age)

    def bonjour(self):
        print("Hello")

    def modifier_age(self, nouvel_age):
        if nouvel_age >= 0:
            self.age = nouvel_age
            print("L'âge a été modifié.")
        else:
            print("Veuillez fournir un âge valide.")

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def afficher_age(self):
        print(f"J'ai {self.age} ans.")
    
class Professeur(Personne):
    def __init__(self, age, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee
        self.age = age

    def enseigner(self):
        print("Le cours va commencer.")

max = Personne()
eleve = Eleve()

eleve.afficher_age()







