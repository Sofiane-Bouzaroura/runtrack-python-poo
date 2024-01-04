class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.tache = []

    def ajouterTache(self, tache):
        self.tache.append(tache)

    def suprimerTache(self, titre):
        for tache in self.tache:
            if tache.titre == titre:
                self.tache.nouveau(tache)
                print("Tache", titre, "supprimée.")
                return
        print("Tache", titre, "non trouvée.")
    
    def marquerCommeFinie(self, titre):
        for tache in self.tache:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print("Tache", titre, "marquée comme terminée.")
                return
        print("Tache", titre, "non trouvée.")
    
    def afficherListe(self):
        print("Liste des taches:")
        for tache in self.tache:
            print("Titre:", tache.titre, "Description", tache.description, "Statut", tache.statut)

    def filterListe(self, statut):           
        filtered_taches = [tache for tache in self.tache if tache.statut == statut]
        print("Taches avec le statut:", statut)
        for tache in filtered_taches:
            print("Titre:", tache.titre, "Description:", tache.description, "Statut:", tache.statut)

# Example usage:
tache1 = Tache("Faire les devoirs", "Révision sur les maths", "En cours")
tache2 = Tache("Faire du sport", "Courir 30 minutes", "À faire")


liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)

liste_taches.afficherListe()

liste_taches.marquerCommeFinie("Faire les devoirs")

liste_taches.filterListe("En cours")

