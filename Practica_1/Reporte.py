import os
contenido_report = ""


def encabezado():
    global contenido_report
    contenido_report += """ <!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />

    <title>REPORTE DE PRODUCTOS </title>
    
  </head>
  <body>
  
  <style type="text/css">
  body {
    background-image: url('https://www.xtrafondos.com/descargar.php?id=7943&resolucion=1280x720');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
  color: #FFFFFF; }
  </style>

    <h1 ><center> Piter Angel Esaú Valiente De León, 201902301 </center> </h1>
    
    
    """


def tablas(lp, lp2):

    global contenido_report
    contenido_report += """<table class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Nombre</th>
          <th scope="col">Precio</th>
          <th scope="col">Cantidad Vendida</th>
          <th scope="col">Total</th>

        </tr>
      </thead>
      <tbody>"""
    contador = 1
    for p in lp2:
        contenido_report += """
        <tr>
          <th scope="row">""" + str(contador)+"""</th>
          <td>""" + str(p.nombre)+"""</td>
          <td>""" + str(p.precio)+"""</td>
          <td>""" + str(p.cantidad)+"""</td>
          <td>""" + str(p.total)+"""</td>
        </tr>"""
        contador += 1

    contenido_report += """ </tbody>
    </table>
    <p> <center>EL PRODUCTO MAS VENDIDO ES: """ + lp[0].nombre + """ </center></p>
    <p> <center>EL PRODUCTOS MENOS VENDIDO ES: """ + lp[len(lp)-1].nombre + """</center></p>
    <p> <center>=========================================================================================================================</center></p>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
  </body>
</html>
"""


def ordenamiento(lista):
    try:
        for i in range(1, len(lista)):
            aux = lista[i]
            j = i-1
            while (j >= 0 and int(lista[j].cantidad) < int(aux.cantidad)):
                lista[j+1] = lista[j]
                j = j-1
            lista[j+1] = aux
        return (lista)

    except:
        print("")


def ordenamiento2(lista):
    try:
        for i in range(1, len(lista)):
            aux = lista[i]
            j = i-1
            while (j >= 0 and float(lista[j].total) < float(aux.total)):
                lista[j+1] = lista[j]
                j = j-1
            lista[j+1] = aux
        return (lista)

    except:
        print("")


def crear_reporte():
    global contenido_report

    reporte = open("Reporte.html", "w", encoding="utf8")
    reporte.write(contenido_report)
    reporte.close()
    os.startfile("Reporte.html")


def generar(listap):
    # for i in range(len(listap)):
    #   print(ordenamiento(listap)[i].cantidad)

    # print(listap)
    encabezado()
    tablas(ordenamiento(listap), ordenamiento2(listap))
    crear_reporte()
    print("Se generó el archivo correctamente C;")
