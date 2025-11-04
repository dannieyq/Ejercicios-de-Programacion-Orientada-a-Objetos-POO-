from Animales import Animales

#Clase hija 2 
class Cocodrilo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    def moverse(self):
        print(f"{self.nombre} se desliza por el agua o camina lentamente en tierra")
    
    def reproducirse(self):
        print("La madre pone huevos con cáscara en la tierra y luego estos eclosionan")
    
    def interaccion_social(self):
        print("Normalmente los cocodrilos andan solos")