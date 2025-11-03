
from Clase_vidrio import botella_Vidrio
from Clase_plastico import botella_Plastico


#CÓDIGO PRINCIPAL
print("\n--------- VIDRIO VS PLÁSTICO ---------")
print("Vamos a hacer una comparación entre las botellas de vidrio y las de plástico\n")
obj_Botella_Vidrio=botella_Vidrio("Vidrio", "1.5L", "Cilíndrico con cuello estrecho", "Elegante y transparente", "Corcho", "Superficie lisa sin grabados")
obj_Botella_Plastico=botella_Plastico("Plástico", "600ml", "Cilíndro", "Colorido", "Rosca", "Etiqueta impresa")

print("BOTELLA VIDRIO\n")
print("Similitudes:")
obj_Botella_Vidrio.contener_liq()
obj_Botella_Vidrio.facilitar_vertido()
obj_Botella_Vidrio.cierre_hermetico()
obj_Botella_Vidrio.transporte()
obj_Botella_Vidrio.transparenciaa()
print("Diferencias:")
obj_Botella_Vidrio.manejar()
obj_Botella_Vidrio.compatibilidad_bebidas()
obj_Botella_Vidrio.mostrar_reutilizacion()

print("\n BOTELLA PLÁSTICO\n")
print("Similitudes:")
obj_Botella_Plastico.contener_liq()
obj_Botella_Plastico.facilitar_vertido()
obj_Botella_Plastico.cierre_hermetico()
obj_Botella_Plastico.transporte()
obj_Botella_Plastico.transparenciaa()
print("Diferencias:")
obj_Botella_Plastico.manejar()
obj_Botella_Plastico.compatibilidad_bebidas()
obj_Botella_Plastico.mostrar_reciclaje()