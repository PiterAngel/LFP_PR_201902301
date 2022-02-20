

from tkinter import Tk
from tkinter.filedialog import askopenfilename


class abrir3():

    def Leer_Lfp(self, extension):
        self.contenido = ""
        Tk().withdraw()

        filename = askopenfilename(title='Porfavor selecciona un archivo correspondiente', filetypes=[
            ('ARCHIVOS Lfp', '.*lfp'), ('TODOS LOS ARCHIVOS', '.*')])

        with open(filename) as infile:
            self.contenido = infile.read().strip()

        self.contenido = self.contenido.upper()  # -> MAYUSCULAS
        # print(self.contenido)
        print("El archivo .lfp ah sido cargado con éxito c:")
