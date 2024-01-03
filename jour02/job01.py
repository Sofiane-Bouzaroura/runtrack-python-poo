# class Rectangle:
#     def __init__(self):
#         self.longueur = 10
#         self.largeur = 5

#     def changer_valeur(self):



class Rectangle:
    def __init__(self):
        self.longueur = 10
        self.largeur = 5

    def changer_valeur(self, nouvelle_longueur, nouvelle_largeur):
        self.longueur = nouvelle_longueur
        self.largeur = nouvelle_largeur

# Example usage:
rectangle_instance = Rectangle()
print("Valeur du rectangle:")
print("Longueur:", rectangle_instance.longueur)
print("Largeur:", rectangle_instance.largeur)

rectangle_instance.changer_valeur(12, 6)

print("\nAprés la valeur changer:")
print("Nouvelle longueur:", rectangle_instance.longueur)
print("Nouvelle largeur:", rectangle_instance.largeur)
