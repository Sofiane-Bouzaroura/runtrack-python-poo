class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print("Coordonnées du point", self.x, self.y)

    def afficherXendY(self):
        print("La coordonnée x est", self.x)
        print("La coordonnée y est", self.y)

    def changerXendY(self, nouvelle_valeur_x, nouvelle_valeur_y):
        self.x = nouvelle_valeur_x
        self.y = nouvelle_valeur_y

point1 = Point(1, 7)

point1.afficherLesPoints()

point1.changerXendY(8, 10)

point1.afficherLesPoints()
point1.afficherXendY()




