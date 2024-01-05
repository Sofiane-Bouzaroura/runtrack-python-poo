class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombre_de_buts = 0
        self.nombre_de_passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.nombre_de_buts += 1

    def effectuerUnePasseDecisive(self):
        self.nombre_de_passes += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom}:")
        print(f"Nombre de buts: {self.nombre_de_buts}")
        print(f"Nombre de passes décisives: {self.nombre_de_passes}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de tous les joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, nouvelle_statistique):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                nouvelle_statistique(joueur)
                return
        print(f"Joueur {nom_joueur} non trouvé dans l'équipe {self.nom}.")

joueur1 = Joueur("Ronaldo", 10, "Attaquant")
joueur2 = Joueur("Mbappé", 11, "Attaquant")
joueur3 = Joueur("Kane", 7, "Attaquant")

equipe1 = Equipe("Équipe A")
equipe2 = Equipe("Équipe B")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)

joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

def nouvelleStatistiqueExemple(joueur):
    joueur.nombre_de_buts += 1

equipe1.mettreAJourStatistiquesJoueur("Ronaldo", nouvelleStatistiqueExemple)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
