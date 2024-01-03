class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.__disponible = True  

    def afficher_informations(self):
        print("Titre:", self.titre)
        print("Auteur:", self.auteur)
        print("Nombre de pages:", self.pages)
        print("Disponible:", "Oui" if self.__disponible else "Non")

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            print("Le livre a été emprunté.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.__disponible:
            print("Le livre a été rendu.")
            self.__disponible = True
        else:
            print("Le livre était déjà disponible. Impossible de le rendre à nouveau.")

livre_instance = Livre("Hamlet", "William Shakespeare", 127)

livre_instance.afficher_informations()

if livre_instance.vérification():
    livre_instance.emprunter()

livre_instance.rendre()

livre_instance.afficher_informations()

