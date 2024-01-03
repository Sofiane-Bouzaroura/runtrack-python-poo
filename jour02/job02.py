class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def afficher_informations(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Nombre de pages: {self.pages}")

    def ajouter_pages(self, nombre_pages):
        self.pages += nombre_pages
        print(f"Nombre de pages après ajout: {self.pages}")

livre_instance = Livre("Hamlet", "William Shakespeare", 127)

livre_instance.afficher_informations()

livre_instance.ajouter_pages(20)

livre_instance.afficher_informations()
