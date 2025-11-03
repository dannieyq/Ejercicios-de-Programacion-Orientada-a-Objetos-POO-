from Clase_Botella import Botella

#Clase Botella Plástico(Hija 2)
class botella_Plastico(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)
        self.reciclable="reciclable"
    
    def manejar(self):
        print(f"1. Su forma y material permiten un manejo cómodo y seguro")
    
    def compatibilidad_bebidas(self):
        print("2. La botella de plástico es más adecuada para bebidas frías ya que se puede derretir")
    
    def mostrar_reciclaje(self):
        print(f"3. Las botellas plásticas son {self.reciclable}")
