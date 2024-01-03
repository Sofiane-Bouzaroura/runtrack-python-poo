class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiant = numero_etudiant
        self.credits = 0  

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.credits += nombre_credits
            print("crédits ajoutés. Total de crédits maintenant :", nombre_credits, self.credits)
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

john_doe = Student("Doe", "John", 145)

john_doe.add_credits(10)
john_doe.add_credits(5)
john_doe.add_credits(15) 

print("Le nombre de crédits de est de points.",john_doe.prenom, john_doe.nom, john_doe.credits )

