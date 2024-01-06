import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2 
        # return 3.14159 * self.rayon ** 2   

rectangle = Rectangle(3, 5)
cercle = Cercle(4)

aire_rectangle = rectangle.aire()
aire_cercle = cercle.aire()

print("Aire du rectangle:", aire_rectangle)
print("Aire du cercle:", aire_cercle)