from producto import producto


class Analizar_Data:
    def __init__(self, contenido):
        self.productos = []
        self.mes = ""
        self.anio = 0
        self.contenido = contenido

    def Analisis_Data(self):
        c = self.contenido
        variablexd = c.split("(")
        # print(variablexd)
        mes = variablexd[0].split(" ")
        self.mes = mes[0]
        # print(self.mes)
        self.anio = int(mes[2])
        # print(self.anio)

        datozzz = variablexd[1].split("\n")
        # print(datozzz)
        # print("**********************")

        datoszz1 = datozzz[1].split("[")
        # print(datoszz1)
        datoszz2 = datoszz1[1].split(",")
        # print(datoszz2)
        producto1 = datoszz2[0].split('"')
        # print(producto1[1])
        # PARA NUMEROS PRECIO Y VENTAS
        # PRECIO
        #preciozzz = datoszz2[1]
        # print(preciozzz)

        print("--------------------------------------------")
        for i in range(1, len(datozzz)-1):
            t1 = datozzz[i].split("[")
            # print(t1)
            t2 = t1[1]
            # print(t2)
            t3 = t2.split(",")
            precio = t3[1]
            # print(precio)
            t5 = t3[2].split("];")
            # print(t5)
            cantidad = t5[0]
            # rint(cantidad)

            # print(t3)
            t4 = t3[0].split('"')
            nombre = t4[1]
            # print(nombre)
            total = float(precio) * int(cantidad)
            nuevo = producto(nombre, precio, cantidad, total)
            self.productos.append(nuevo)

        # for i in range(len(self.productos)):
         #   print("NOMBRE: " + self.productos[i].nombre)
         #   print("PRECIO: " + self.productos[i].precio)
         #   print("CANTIDAD : " + self.productos[i].cantidad)
        print("El archivo .data ah sido analizado con éxito :0")
        return self.productos
