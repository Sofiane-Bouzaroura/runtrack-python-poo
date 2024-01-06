class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print("Marque =", self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, nombre_portes=4):
        super().__init__(marque, modele, annee, prix)
        self.nombre_portes = nombre_portes

    def informationVehicule(self):
        super().informationVehicule()
        print("Nombre de portes =", self.nombre_portes)

    def demarrer(self):
        print("Vrom Vroum! La voiture démarre.")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, nombre_de_roues=2):
        super().__init__(marque, modele, annee, prix)
        self.nombre_de_roues = nombre_de_roues

    def informationVehicule(self):
        super().informationVehicule()
        print("Nombre de roues =", self.nombre_de_roues)

    def demarrer(self):
        print("Vroum Vroum! La moto démarre.")

La_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
La_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

La_voiture.demarrer()
La_moto.demarrer()
