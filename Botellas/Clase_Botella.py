#CLASE BOTELLA
class Botella():
    def __init__(self, material, capacidad, forma, diseño, tapa, transparencia):
        self.material=material
        self.capacidad=capacidad
        self.forma=forma
        self.diseño=diseño
        self.tapa=tapa
        self.transparencia=transparencia

    #METODOS
    def contener_liq(self):
        print("1. En estás botellas se guardan liquidos como: agua, gaseosas, jugos, etc")
    
    def facilitar_vertido(self):
        print("2. La forma de la botella facilita el vertido del contenido, aunque no haya agarre")
    
    def cierre_hermetico(self):
        print(f"3. La tapa {self.tapa} permite un cierre hermético para evitar derrames y conservar el contenido")
    
    def transporte(self):
        print("4. Las botellas son fáciles de transportar en las canastas de los camiones facilitando su distribución a las tiendas")
    
    def transparenciaa(self):
        print(f"5. Gracias al material de {self.material} permite ver el contenido interno de la botella")