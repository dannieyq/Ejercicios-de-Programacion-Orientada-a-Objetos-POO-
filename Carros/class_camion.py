from class_carros import Carros

#Clase Hija 3
class Camion(Carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.climatizacion="sin climatización"
    
    def _climatizacion_(self):
        print(f"El {self.modelo} está {self.climatizacion}")
    
    def seguridad(self):
        print("Este vehículo contiene cinturones y cerraduras manuales")
    
    def sistema_ventanas(self):
        print("El sistema de ventanas es manual con manivela")