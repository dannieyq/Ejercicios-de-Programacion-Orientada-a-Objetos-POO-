#Clase Madre
class Animales:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.dieta=dieta
        self.tamaño=tamaño
        self.color=color
    
    def alimentarse(self):
        print(f"{self.nombre} se alimenta de {self.dieta}.")
    
    def adaptacion(self):
        print(f"{self.nombre} se adapta a su entorno para sobrevivir")

    def instinto(self):
        print(f"{self.nombre} actúa según sus instintos naturales.")
    
    def descanso(self):
        print(f"{self.nombre} descansa para recuperar energía.")
    
    def comunicacion(self):
        print("Se comunica a través de sonidos, gestos corporales, colores, etc")
    
    def sueño(self):
        print("Usualmente duermen entre 6-10 horas pero depende del ambiente y especie")