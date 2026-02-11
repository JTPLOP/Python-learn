from Inmueble import *
from Piso import *
from LocalComercial import *

class Gestion:
    def __init__(self, lista, clientes): # En el enunciado nos piden trabajar con diccionarios

        self.__lista= [] # AQUI AGREGAMOS TODOS LOS INMUEBLES INDIFERENTE DE LOS CLIENTES
        self.__clientes={} #AQUI PODRIAMOS METER LOS DATOS DE LOS CLIENTES Y EL ID DE SU INMUEBLE

    def buscarID(self,idBuscado):
        for i, inmueble in enumerate(self.__lista):
            if Inmueble.getid == idBuscado:
                return i
        return -1
    #AGREGAR INMUEBLE A LA LISTA

    def agregarInmu (self, Inmueble):

        self.__lista.append(Inmueble)
    
    def agregarCliente (self, numClientes, nombre, telefono):
         self.__clientes[numClientes] = {
            "Nombre": nombre,
            "Telefono": telefono,
            "Inmuebles": [Inmueble[2].getid]
        }
    
    def calcularGanancias(self,idBuscado, impuesto, extAsc, extEscap):
        idx = self.buscarID(idBuscado)
        
        return self.__lista[idx].calcularIngresos(impuesto, extAsc, extEscap)




