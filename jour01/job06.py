class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        
    def afficherAge(self):
        print("l'age de l'animal est de:", self.age, "an")

    def vieillir(self):
        self.age += 1
        print("l'age de l'animal après vieillissement:", self.age, "an")
    
    def surnommer(self, nom):
        self.prenom = nom
        print("l'animal s'apelle:", self.prenom)
 
animal01 = Animal()

animal01.afficherAge()

animal01.vieillir()

animal01.afficherAge()

animal01.surnommer("Daizy")