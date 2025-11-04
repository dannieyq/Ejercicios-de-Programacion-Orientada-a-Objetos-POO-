from class_carro import carro
from class_camion import Camion
from class_van import Van

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