class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print("Nom du produit:", self.nom)
        print("Prix HT:", self.prixHT, "€")
        print("TVA:", self.TVA, "%")
        print("Prix TTC:", self.CalculerPrixTTC(), "€")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Console", 400, 20)
produit2 = Produit("Smartphone", 500, 15)

print("Produit 1:")
produit1.afficher()
print()

print("Produit 2:")
produit2.afficher()
print()


produit1.modifierNom("Playstation 5")
produit1.modifierPrixHT(500)

print("Produit 1 après modification:")
produit1.afficher()
print()

print("Informations sur le Produit 2:")
print("Nom:", produit2.obtenirNom())
print("Prix HT:", produit2.obtenirPrixHT(), "€")
print("TVA:", produit2.obtenirTVA(), "%")
print("Prix TTC:", produit2.CalculerPrixTTC(), "€")
