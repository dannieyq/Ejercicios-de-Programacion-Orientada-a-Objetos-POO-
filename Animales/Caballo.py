from Animales import Animales

#Clase hija 1
class Caballo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    
    def sueño(self):
        print("Usualmente duerme entre 2 a 3 horas intermitentes durante el día")
    
    def moverse(self):
        print(f"{self.nombre} galopa por el campo.")
    def reproducirse(self):
        print("Las crías crecen dentro de la madre y la gestación dura casi un año")
    
    def interaccion_social(self):
        print("Vive en manadas y tienen lazos sociales fuertes entre ellos")