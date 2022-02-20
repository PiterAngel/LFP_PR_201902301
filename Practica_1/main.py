from abrir2 import abrir2
from abrir3 import abrir3
from Analizar_Data import Analizar_Data
from Analizar_Lfp import Analizar_Lfp
from Reporte import *

a = abrir2()
b = abrir3()


class main2:
    def __init__(self):
        self.app()

    def app(self):
        print("")


while True:
    print("========================HOLA-BIENVENIDO================================================")
    print("De las siguientes opciones porfavor eliga una :D")
    print("Opcion 1. Cargar Data")
    print("Opcion 2. Cargar Instrucciones")
    print("Opcion 3. Analizar")
    print("Opcion 4. Reportes")
    print("Opcion 5. Salir")
    opcion = float(input("Porfavor ingrese su opción: "))

    if opcion == 1:

        a.Leer_Data('.data')
        # print(a.contenido)

    elif opcion == 2:
        b.Leer_Lfp('.lfp')

    elif opcion == 3:
        Analizar_Data(a.contenido).Analisis_Data()
        Analizar_Lfp(b.contenido).Analisis_Lfp()

    elif opcion == 4:
        generar(Analizar_Data(a.contenido).Analisis_Data())

    elif opcion == 5:
        print("Que tenga un bonito día C:")
        print("====================================================================================")
        break
    else:
        print("Error, porfavor ingrese solo una de las opciones")

    print("=======================================================================================")
    continue
