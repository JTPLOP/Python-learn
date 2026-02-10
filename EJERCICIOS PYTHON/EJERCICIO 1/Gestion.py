from Inmueble import *
from Piso import *
from LocalComercial import *

class Gestion:
    def __init__(self, lista): # En el enunciado nos piden trabajar con diccionarios

        Inmueble.__lista= [] # AQUI AGREGAMOS TODOS LOS INMUEBLES INDIFERENTE DE LOS CLIENTES
        self.__clientes={} #AQUI PODRIAMOS METER LOS DATOS DE LOS CLIENTES Y EL ID DE SU INMUEBLE

    def buscarID(self,idBuscado):
        
        i = 0
        encontrado = False
        while (i < len(lista) and not encontrado):
            if (idBuscado == Inmueble.getid):
                pass

