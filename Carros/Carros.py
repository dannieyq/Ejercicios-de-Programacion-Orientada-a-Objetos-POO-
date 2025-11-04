#Clase Madre
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

#Clase Hija 1
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

#Código Principal

Obj_carro = carro("Toyota", "Rojo", "1.8L", 4, 5, "Gasolina")
Obj_van = Van("Hyundai", "Gris", "2.2L", 5, 8, "Diésel")
Obj_camion = Camion("Chevrolet", "Blanco", "3.0L", 2, 3, "Diésel")

print("CARRO:")
print("---- FUNCIONES COMUNES ----")
Obj_carro.arranque()
Obj_carro.apagado()
Obj_carro.aceleracion_frenado()
Obj_carro.sistema_direccion()
Obj_carro.luces()
Obj_carro.sistema_espejo()
print()

print("---- DIFERENCIAS ENTRE VEHÍCULOS ----")
Obj_carro._climatizacion_()
Obj_carro.seguridad()
Obj_carro.sistema_ventanas()
print()

print("VAN:")
print("---- FUNCIONES COMUNES ----")
Obj_van.arranque()
Obj_van.apagado()
Obj_van.aceleracion_frenado()
Obj_van.sistema_direccion()
Obj_van.luces()
Obj_van.sistema_espejo()
print()
print("---- DIFERENCIAS ENTRE VEHÍCULOS ----\n")
Obj_van._climatizacion_()
Obj_van.seguridad()
Obj_van.sistema_ventanas()
print()

print("CAMIÓN:")
print("---- FUNCIONES COMUNES ----")
Obj_camion.arranque()
Obj_camion.apagado()
Obj_camion.aceleracion_frenado()
Obj_camion.sistema_direccion()
Obj_camion.luces()
Obj_camion.sistema_espejo()
print()
print("---- DIFERENCIAS ENTRE VEHÍCULOS ----\n")
Obj_camion._climatizacion_()
Obj_camion.seguridad()
Obj_camion.sistema_ventanas()
print()

print("----------- FIN DE LA COMPARACIÓN -----------")