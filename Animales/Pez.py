from Animales import Animales

#Clase hija 3
class Pez(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    
    def moverse(self):
        print(f"{self.nombre} nada con sus aletas")
    
    def reproducirse(self):
        print("La hembra libera los huevos en el agua y el macho los fertiliza afuera")
    
    def interaccion_social(self):
        print("Usualmente se encuentra con otros peces de la misma especie")