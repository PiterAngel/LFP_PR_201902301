import re
from tkinter import filedialog, Tk


def abrir():  # FUNCION ABRIR

    Tk().withdraw()  # SELECCIONARLO XD
    archivo = filedialog.askopenfile(  # VARIABLE PARA ABRIR ARCHIVO
        title="Seleccionar un archivo",
        initialdir="./",  # la ./ seleccionar donde esta el archivo
        filetypes=(
            ("archivos Data", "*.txt"),
            ("TODOS LOS ARCHIVOS", "*.*")  # *.* para cualquier cosa
            # data.txt
            # Holaclase.claselfp
        )
    )

    if archivo is None:  # Si es nulo
        print("No se SELECCIONO UN ARCHIVO")
        return None
    else:
        texto = archivo.read()  # PARA LEER EL ARCHIVO
        archivo.close()
        return texto  # abrir e imprimir el texto dentro de ese archivo


if __name__ == "__main__":
    print("========================HOLA-BIENVENIDO================================================")
while True:
    print("De las siguientes opciones porfavor eliga una")
    print("Opcion 1. Cargar Data")
    print("Opcion 2. Cargar Instrucciones")
    print("Opcion 3. Analizar")
    print("Opcion 4. Reportes")
    print("Opcion 5. Salir")
    opcion = float(input("Porfavor ingrese su opción: "))

    if opcion == 1:

        print("cargar DATA")
        abrir()

    elif opcion == 2:
        print("cargar instrucciones")

    elif opcion == 3:
        print("Analizar")

    elif opcion == 4:
        print("Reportes")

    elif opcion == 5:
        print("Que tenga un bonito día C:")
        print("=======================================================================================")
        break
    else:
        print("Error, porfavor ingrese solo una de las opciones")

    print("=======================================================================================")
    continue
