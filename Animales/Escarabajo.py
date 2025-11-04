from Animales import Animales

#Clase hija 4
class Escarabajo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    
    def moverse(self):
        print(f"{self.nombre} camina o vuela cortas distancias")
    
    def reproducirse(self): 
        print("Pone muchos huevos pequeños que, al eclosionar, pasan por varias etapas de crecimiento hasta morir")
    
    def interaccion_social(self):
        print("Son solitarios aunque se pueden encontrar algunas veces en grupos pequeños")