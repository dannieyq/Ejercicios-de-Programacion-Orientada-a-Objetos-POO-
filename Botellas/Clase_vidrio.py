from Clase_Botella import Botella

#Clase Botella Vidrio(Hija 1)
class botella_Vidrio(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.reutilizacion=80
    
    def manejar(self):
        print(f"1. Al tener forma de {self.forma} es fácil de guardar sin embargo al ser una botella de vidrio el manejo de esta requiere mucho más cuidado")
    
    def compatibilidad_bebidas(self):
        print("2. Depende mucho del material del vidrio sin embargo si es capaz de soportar el calor más que una botella de plástico")
    
    def mostrar_reutilizacion(self):
        print(f"3. Esta botella de vidrio puede reutilizarse aproximadamente {self.reutilizacion} veces sin perder calidad")
