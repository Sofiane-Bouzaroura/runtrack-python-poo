class Operation:
    def __init__(self, nombre1 , nombre2):
        self.nombre1 = nombre1 
        self.nombre2 = nombre2
        print("le nombre1 est:", nombre1)
        print("le nombre2 est:", nombre2)

    def addition(self):
        self.resultat = self.nombre1 + self.nombre2
        print("Resultat des deux ", self.resultat)

operation_instance = Operation(12, 3)
operation_instance.addition()



    