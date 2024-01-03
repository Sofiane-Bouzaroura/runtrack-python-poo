# class Operation:
#     def __init__(self, nombre1, nombre2):
#         print("le nombre1 est:", nombre1)
#         print("le nombre2 est:", nombre2)

# Operation(12,3)




class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation(12, 3)

print("Le nombre1 est:", operation_instance.nombre1)
print("Le nombre2 est:", operation_instance.nombre2)
