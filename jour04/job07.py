class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        self.melanger_paquet()

    def melanger_paquet(self):
        n = len(self.paquet)
        for i in range(n - 1, 0, -1):
            j = i if i == 0 else i % (i + 1)
            self.paquet[i], self.paquet[j] = self.paquet[j], self.paquet[i]

    def calculer_points(self, main):
        total_points = 0
        nombre_as = 0

        for carte in main:
            if carte.valeur.isdigit():
                total_points += int(carte.valeur)
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                total_points += 10
            elif carte.valeur == 'As':
                nombre_as += 1

        for _ in range(nombre_as):
            if total_points + 11 <= 21:
                total_points += 11
            else:
                total_points += 1

        return total_points

    def jouer_partie(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]
        main_croupier = [self.paquet.pop(), self.paquet.pop()]

        while True:
            print(f"Main du joueur: {', '.join([carte.valeur for carte in main_joueur])}")
            choix = input("Voulez-vous prendre une carte de plus ? (oui/non): ")

            if choix.lower() == 'oui':
                main_joueur.append(self.paquet.pop())
                points_joueur = self.calculer_points(main_joueur)

                if points_joueur > 21:
                    print("Vous avez dépassé 21 points. Vous avez perdu.")
                    return
            else:
                break

        while self.calculer_points(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        points_joueur = self.calculer_points(main_joueur)
        points_croupier = self.calculer_points(main_croupier)

        print(f"\nMain du joueur: {', '.join([carte.valeur for carte in main_joueur])} - Total points: {points_joueur}")
        print(f"Main du croupier: {', '.join([carte.valeur for carte in main_croupier])} - Total points: {points_croupier}")

        if points_joueur > 21:
            print("Vous avez dépassé 21 points. Vous avez perdu.")
        elif points_croupier > 21 or points_joueur > points_croupier:
            print("Félicitations ! Vous avez gagné.")
        elif points_joueur < points_croupier:
            print("Désolé, vous avez perdu. Le croupier gagne.")
        else:
            print("Égalité !")

jeu = Jeu()
jeu.jouer_partie()




