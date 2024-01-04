class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        decouvert = True

    def afficher(self):
        print("Information du compte:")
        print("Numéro de compte:", self.__numero_compte)
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Solde:", self.__solde, "€")
        print("Decouvert autorisé:", "Oui" if  self.__decouvert else "Non")

    def afficherSolde(self):
        print("Le solde du compte est de:", self.__solde )

    def versement(self, montant):
        self.__solde += montant
        print("Versement de:", montant, "effectué. Nouveau solde:", self.__solde)

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print("Retrait de", montant, "effectué. Nouveau solde:", self.__solde)
        else:
            print("Insuffisant. Opération annulée.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print("Agios appliqués. Nouveau solde:", self.__solde)

    def virement(self, compte, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte.versement(montant)
            print("Virement de", montant, "effectuer vers le compte", compte.__numero_compte)
        else:
            print("Insuffisant. Opération de virement annulée.") 


compte1 = CompteBancaire("123456", "Doe", "John", 1000, True)
compte2 = CompteBancaire("553265", "Dayzi", "Jeanne", -500, False)

compte1.afficher()
compte2.afficher()

compte1.virement(compte2, 300)

compte1.afficher()
compte2.afficher()
