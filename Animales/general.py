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

#Clase hija 1
class Caballo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    
    def sueño(self):
        print("Usualmente duerme entre 2 a 3 horas intermitentes durante el día")
    
    def moverse(self):
        print(f"{self.nombre} galopa por el campo")
    def reproducirse(self):
        print("Las crías crecen dentro de la madre y la gestación dura casi un año")
    
    def interaccion_social(self):
        print("Vive en manadas y tienen lazos sociales fuertes entre ellos")

#Clase hija 2 
class Cocodrilo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    def moverse(self):
        print(f"{self.nombre} se desliza por el agua o camina lentamente en tierra")
    
    def reproducirse(self):
        print("La madre pone huevos con cáscara en la tierra y luego estos eclosionan")
    
    def interaccion_social(self):
        print("Normalmente los cocodrilos andan solos")

#Clase hija 3
class Pez(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
    
    def moverse(self):
        print(f"{self.nombre} nada con sus aletas")
    
    def reproducirse(self):
        print("La hembra libera los huevos en el agua y el macho los fertiliza afuera")
    
    def interaccion_social(self):
        print("Usualmente se encuentra con otros peces de la misma especie")

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

#Código Principal
Obj_caballo= Caballo("Sara", 5, "Pradera", "Hierba", "Grande", "Marrón")
Obj_cocodrilo = Cocodrilo("Yuleysi", 12, "Río", "pseces y pequeños animales", "Grande", "Verde")
Obj_pez = Pez("Nemo", 1, "Océano", "algas y pequeños crustáceos", "Pequeño", "Naranja")
Obj_escarabajo = Escarabajo("Camilo", 0.2, "Bosque", "Hoja y restos orgánicos", "Pequeño", "Marrón")
Obj_pato = Pato("Miguel", 3, "Lago", "granos y insectos", "Mediano", "Blanco y naranja")

print("\n--- Caballo - Sara ---")
Obj_caballo.alimentarse()
Obj_caballo.adaptacion()
Obj_caballo.instinto()  
Obj_caballo.descanso()
Obj_caballo.comunicacion()
Obj_caballo.sueño()
Obj_caballo.moverse()
Obj_caballo.reproducirse()
Obj_caballo.interaccion_social()

print("\n--- Cocodrilo - Yuleysi ---")
Obj_cocodrilo.alimentarse()
Obj_cocodrilo.adaptacion()
Obj_cocodrilo.instinto()
Obj_cocodrilo.descanso()
Obj_cocodrilo.comunicacion()
Obj_cocodrilo.sueño()
Obj_cocodrilo.moverse()
Obj_cocodrilo.reproducirse()
Obj_cocodrilo.interaccion_social()

print("\n--- Pez - Nemo ---")
Obj_pez.alimentarse()
Obj_pez.adaptacion()
Obj_pez.instinto()
Obj_pez.descanso()
Obj_pez.comunicacion()
Obj_pez.sueño()
Obj_pez.moverse()
Obj_pez.reproducirse()
Obj_pez.interaccion_social()


print("\n--- Escarabajo - Camilo ---")
Obj_escarabajo.alimentarse()
Obj_escarabajo.adaptacion()
Obj_escarabajo.instinto()
Obj_escarabajo.descanso()
Obj_escarabajo.comunicacion()
Obj_escarabajo.sueño()
Obj_escarabajo.moverse()
Obj_escarabajo.reproducirse()
Obj_escarabajo.interaccion_social()

print("\n--- Pato - Miguel ---")
Obj_pato.alimentarse()
Obj_pato.adaptacion()
Obj_pato.instinto()
Obj_pato.descanso()
Obj_pato.comunicacion()
Obj_pato.sueño()
Obj_pato.moverse()
Obj_pato.reproducirse()
Obj_pato.interaccion_social()