
from re import X
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from producto import producto


class abrir2():

    def Leer_Data(self, extension):
        self.contenido = ""
        Tk().withdraw()

        filename = askopenfilename(title='Porfavor selecciona un archivo correspondiente', filetypes=[
            ('ARCHIVOS Data', '.*data'), ('TODOS LOS ARCHIVOS', '.*')])

        with open(filename) as infile:
            self.contenido = infile.read().strip()

        self.contenido = self.contenido.upper()  # -> MAYUSCULAS
        # print(self.contenido)
        print("El archivo .data ah sido cargado con éxito c:")
