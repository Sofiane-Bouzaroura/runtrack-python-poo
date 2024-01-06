# class Rectangle:
#     def __init__(self, longueur, largeur):
#         self.__longueur = longueur
#         self.__largeur = largeur

#     def perimetre(self):
#         return (self.__longueur + self.__largeur) * 2

#     def surface(self):
#         return self.__longueur * self.__largeur

#     def get_longueur(self):
#         return self.__longueur

#     def set_longueur(self, longueur):
#         self.__longueur = longueur

#     def get_largeur(self):
#         return self.__largeur
    
#     def set_largeur(self, largeur):
#         self.__largeur = largeur

# class Parallelepipede(Rectangle):
#     def __init__(self, hauteur, longueur, largeur):
#         Rectangle.__init__(self, longueur, largeur)
#         self.__hauteur = hauteur

#     def volume(self):
#         return self.__longueur * self.__largeur * self.__hauteur

#     def get_hauteur(self):
#         return self.__hauteur

#     def set_hauteur(self, hauteur):
#         self.__hauteur = hauteur

# rectangle = Rectangle(10, 7)
# valeur_perimetre = rectangle.perimetre()
# valeur_surface = rectangle.surface()

# print("Rectangle - Périmètre:", valeur_perimetre)
# print("Rectangle - Surface:", valeur_surface)


# parallelepiped = Parallelepipede(10, 7, 2)
# print("Parallélépipède - Périmètre:", parallelepiped.perimetre())
# print("Parallélépipède - Surface:", parallelepiped.surface())
# print("Parallélépipède - Volume:", parallelepiped.volume())


class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs et mutateurs pour la longueur
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Assesseurs et mutateurs pour la largeur
    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Assesseur et mutateur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume du parallélépipède
    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur


# Instanciation de la classe Rectangle
mon_rectangle = Rectangle(5, 8)

# Utilisation des méthodes de la classe Rectangle
print("Périmètre du rectangle :", mon_rectangle.perimetre())
print("Surface du rectangle :", mon_rectangle.surface())

# Instanciation de la classe Parallelepipede
mon_parallelepipede = Parallelepipede(3, 4, 6)

# Utilisation des méthodes de la classe Rectangle (héritées) et de la classe Parallelepipede
print("Périmètre du parallélépipède :", mon_parallelepipede.perimetre())
print("Surface du parallélépipède :", mon_parallelepipede.surface())
print("Volume du parallélépipède :", mon_parallelepipede.volume())
