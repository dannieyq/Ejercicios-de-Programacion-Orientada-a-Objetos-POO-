from class_carros import Carros

#Clase Hija 2
class Van(Carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.climatizacion="ventilador manual"
    
    def _climatizacion_(self):
        print(f"El {self.modelo} cuenta con {self.climatizacion}")
    
    def seguridad(self):
        print("Este vehículo cuenta con frenos ABS y cinturones")
    
    def sistema_ventanas(self):
        print("El sistema de ventanas es eléctrico con botones")