import re
from tkinter import filedialog, Tk

lista = []
[[104, "h"], [97, "o"], [], []]


def abrir():  # FUNCION ABRIR

    Tk().withdraw()  # SELECCIONARLO XD
    archivo = filedialog.askopenfile(  # VARIABLE PARA ABRIR ARCHIVO
        title="Seleccionar un archivo",
        initialdir="./",  # la ./ seleccionar donde esta el archivo
        filetypes=(
            ("archivos LFP", "*.txt"),
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


if __name__ == '__main__':
    lista = []
    txt = abrir()
    Contador_Digitos = 0
    Contador_Caracteres = 0
    Contador_Symbolos = 0

    if txt is not None:
        # print(txt)
        if(len(txt) > 0):
            for C in txt:
                # print(C, end="\n")
                if ord(C) == '\n':  # IF ORD(C) == 72: PARA SABER O IGNORAR EL NUMERO DE LA TABLA ASSCI
                    pass
                elif C == '':
                    pass
                else:
                    listaAux = [ord(C), C]  # LISTA CON ESOS DATOS
                    lista.append(listaAux)

            # para imrpimir el salto de línea al final
            # ORD PARA DEVOLVER EL NÚMERO DE LA TABLA ASSCI DE CADA DIGITO
            # C es un caracter y no se puede mezclar con un string
            # PARA SABER EL VALOR DE CADA LETRA
            # print(C + " - " + str(ord(C))) #PARA ANTERIOR

            for e in lista:
                if e[0] >= 48 and e[0] <= 57:
                    Contador_Digitos += 1
                elif e[0] >= 65 and e[0] <= 90 or e[0] >= 97 and e[0] <= 122:
                    Contador_Caracteres += 1
                elif e[0] >= 33 and e[0] <= 47 or e[0] >= 58 and e[0] <= 64:
                    Contador_Symbolos += 1
                print("Assciii: " + str(e[0]) + " - Caracter: " + e[1])
                #print("Assciii: " + str(e[0]) + " - Caracter: " + e[1])
                #print("HAYYYYYYY: " + contador3)
                # 0 GUARDA LOS CARACTERES DEL ASSCI
                # PARA MOSTRAR EL NUMERO ASSCI Y SU CARACTER OSEA QUE ES XD
                # Assciii: 71 - Caracter: Gs
                #

                # if ord(txt) >= "12" and ord(txt) <= "20":
                #   contador = txt+1

                # print(contador)

        else:

            print("No hay texto :,v F")
    else:
        print("No se puede procesar ")
print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
print("Hay un total de: " + str(Contador_Digitos) + " Digitos")
print("Hay un total de: " + str(Contador_Caracteres) + " Carácteres")
print("Hay un total de: " + str(Contador_Symbolos) + " Symbolos :0")
print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")

# LOS COMENTARIOS NO EJECUTAN NADA PORQUE NO TIENE NINGUNA FUNCION
# caracteres = 0
# for linea in txt:
#    caracteres += len(linea)
# if linea == '\n':
#       caracteres += 1
#       espacios = ''.join(re.findall("\s+", txt))
#   print(caracteres)
# if(len(txt) > 0):
# contador = ord(C)
# for letra in txt:
#    if letra.lower() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#        contador += 1
#    # return contador
#    print("hay" + str(contador))
#contador1 = ord(C)
#            contador2 = ord(C)
#            for letra in txt:
#                if (ord(C) >= 48 and ord(C) <= 57):
#                    contador1 += 1
#                elif (ord(C) >= "65" and ord(C) <= "97"):
#                    contador2 += 1
#                else:
#                    pass
#                    print("HAY1: " + str(contador1) +
#                          " HAY2: " + str(contador2))
