from Animales import Animales

#Clase hija 5
class Pato(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    def moverse(self):
        print(f"{self.nombre} camina, nada y vuela")
    def reproducirse(self):
        print("La madre pone huevos, los incuba para darles calor y nacen los hijos")
    def interaccion_social(self):
        print("Son bastante sociables con los de su especie")