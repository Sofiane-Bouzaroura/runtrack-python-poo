class Personne:
    def __init__(self, nom, prenon):
        self.nom = nom
        self.prenom = prenon
        
    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)  

personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

personne1.SePresenter()
personne2.SePresenter()