class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom
    
    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_personne(self):
         self.__nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_population(self):
        self.__ville.ajouter_personne()

Paris = Ville("Paris", 1000000)   
Marseille = Ville("Marseille", 861635)

print("Population de la ville de Paris:", Paris.get_nombre_habitants())       
print("Population de la ville de Mareille:", Marseille.get_nombre_habitants())

John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Cloé = Personne("Cloé", 18, Marseille)

John.ajouter_population()
Myrtille.ajouter_population()
Cloé.ajouter_population()

print("Mise a jour de la population de la ville de Paris:", Paris.get_nombre_habitants())
print("Mise a jour de la population de la ville de Marseille:", Marseille.get_nombre_habitants())