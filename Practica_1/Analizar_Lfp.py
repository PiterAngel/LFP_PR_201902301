from instrucciones import instrucciones


class Analizar_Lfp:
    def __init__(self, contenido):
        self.contenido = contenido
        self.instruccion = None

    def Analisis_Lfp(self):
        variablexdd = self.contenido.split("<Â¿")
        # print(variablexdd)
        conte = variablexdd[1].split("\n")
        # print(contenido)
        for i in range(1, len(conte)-1):
            instruccion = []
            Nombre = ""
            Grafica = ""
            Titulo = ""
            Titulox = ""
            Tituloy = ""

            if i == 1:
                instruccion.append(conte[i])
                # #print(instruccion)
                nombres = instruccion[0].split(":")
                # #print(nombres)
                if nombres[0] == "NOMBRE":
                    nombre = nombres[1]
                    Nombre = nombre.split('"')[1]
                    # print(Nombre)
                elif nombres[0] == "GRAFICA":
                    nombre = nombres[1]
                    Grafica = nombre.split('"')[1]
                    # print(Grafica)
                elif nombres[0] == "TITULO":
                    nombre = nombres[1]
                    Titulo = nombre.split('"')[1]
                    # print(Titulo)
                elif nombres[0] == "TITULOX":
                    nombre = nombres[1]
                    Titulox = nombre.split('"')[1]
                    # print(Titulox)
                elif nombres[0] == "TITULOY":
                    nombre = nombres[1]
                    Tituloy = nombre.split('"')[1]
                    # print(Tituloy)

            elif i == 2:
                instruccion.append(conte[i])
                # #print(instruccion)
                nombres = instruccion[0].split(":")
                # #print(nombres)
                if nombres[0] == "NOMBRE":
                    nombre = nombres[1]
                    Nombre = nombre.split('"')[1]
                    # print(Nombre)
                elif nombres[0] == "GRAFICA":
                    nombre = nombres[1]
                    Grafica = nombre.split('"')[1]
                    # print(Grafica)
                elif nombres[0] == "TITULO":
                    nombre = nombres[1]
                    Titulo = nombre.split('"')[1]
                    # print(Titulo)
                elif nombres[0] == "TITULOX":
                    nombre = nombres[1]
                    Titulox = nombre.split('"')[1]
                    # print(Titulox)
                elif nombres[0] == "TITULOY":
                    nombre = nombres[1]
                    Tituloy = nombre.split('"')[1]
                    # print(Tituloy)

            elif i == 3:
                instruccion.append(conte[i])
                # #print(instruccion)
                nombres = instruccion[0].split(":")
                # #print(nombres)
                if nombres[0] == "NOMBRE":
                    nombre = nombres[1]
                    Nombre = nombre.split('"')[1]
                    # print(Nombre)
                elif nombres[0] == "GRAFICA":
                    nombre = nombres[1]
                    Grafica = nombre.split('"')[1]
                    # print(Grafica)
                elif nombres[0] == "TITULO":
                    nombre = nombres[1]
                    Titulo = nombre.split('"')[1]
                    # print(Titulo)
                elif nombres[0] == "TITULOX":
                    nombre = nombres[1]
                    Titulox = nombre.split('"')[1]
                    # print(Titulox)
                elif nombres[0] == "TITULOY":
                    nombre = nombres[1]
                    Tituloy = nombre.split('"')[1]
                    # print(Tituloy)

            elif i == 4:
                instruccion.append(conte[i])
                # #print(instruccion)
                nombres = instruccion[0].split(":")
                # #print(nombres)
                if nombres[0] == "NOMBRE":
                    nombre = nombres[1]
                    Nombre = nombre.split('"')[1]
                    # print(Nombre)
                elif nombres[0] == "GRAFICA":
                    nombre = nombres[1]
                    Grafica = nombre.split('"')[1]
                    # print(Grafica)
                elif nombres[0] == "TITULO":
                    nombre = nombres[1]
                    Titulo = nombre.split('"')[1]
                    # print(Titulo)
                elif nombres[0] == "TITULOX":
                    nombre = nombres[1]
                    Titulox = nombre.split('"')[1]
                    # print(Titulox)
                elif nombres[0] == "TITULOY":
                    nombre = nombres[1]
                    Tituloy = nombre.split('"')[1]
                    # print(Tituloy)
            elif i == 5:
                instruccion.append(conte[i])
                # #print(instruccion)
                nombres = instruccion[0].split(":")
                # #print(nombres)
                if nombres[0] == "NOMBRE":
                    nombre = nombres[1]
                    Nombre = nombre.split('"')[1]
                    # print(Nombre)
                elif nombres[0] == "GRAFICA":
                    nombre = nombres[1]
                    Grafica = nombre.split('"')[1]
                    # print(Grafica)
                elif nombres[0] == "TITULO":
                    nombre = nombres[1]
                    Titulo = nombre.split('"')[1]
                    # print(Titulo)
                elif nombres[0] == "TITULOX":
                    nombre = nombres[1]
                    Titulox = nombre.split('"')[1]
                    # print(Titulox)
                elif nombres[0] == "TITULOY":
                    nombre = nombres[1]
                    Tituloy = nombre.split('"')[1]
                    # print(Tituloy)

            instruccion = instrucciones(
                Nombre, Grafica, Titulo, Titulox, Tituloy)
        print("El archivo .lfp ah sido analizado con éxito :0")
