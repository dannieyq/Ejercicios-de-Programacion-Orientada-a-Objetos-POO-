class Carros:
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        self.modelo=modelo
        self.color=color
        self.motor=motor
        self.n_puertas=puertas
        self.n_pasajeros=pasajeros
        self.combustible=combustible
    
    def arranque(self):
        print(f"El vehículo {self.modelo} enciende su motor y está listo para usarse")

    def apagado(self):
        print(f"El vehículo {self.modelo} apaga el motor y detiene sus sistemas")

    def aceleracion_frenado(self):
        print(f"El vehículo {self.modelo} acelera o frena de manera rápida")

    def sistema_direccion(self):
        print(f"El sistema de dirección de {self.modelo} funciona correctamente")

    def luces(self):
        print(f"Las luces de {self.modelo} están encendidas.")

    def sistema_espejo(self):
        print(f"El sistema de espejos de {self.modelo} está ajustado.")