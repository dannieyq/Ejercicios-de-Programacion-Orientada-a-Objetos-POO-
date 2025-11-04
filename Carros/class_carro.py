from class_carros import Carros

class carro(Carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.climatizacion="aire acondicionado automático"
    
    def _climatizacion_(self):
        print(f"El {self.modelo} tiene {self.climatizacion}")
    
    def seguridad(self):
        print("Este vehículo contiene airbags, frenos ABS y cámara de reversa")
    
    def sistema_ventanas(self):
        print("El sistema de ventanas es automático con un solo toque")