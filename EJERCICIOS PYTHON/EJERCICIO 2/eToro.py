from Accion import *
from Activos import *
from Criptomoneda import *
from clientes import *


class eToroManager: 
    def __init__(self, acciones, clientes):
        self.__clientes = {}
        self.__acciones = []


    #METODOS DE AGREGAR

    def agregarCliente (self, numCliente, nombre, direccion, bonificacion, volatilidad):
        self.__clientes [numCliente]= {
            Clientes.getNombre : nombre,
            Clientes.getDireccion : direccion,
            Clientes.getcartera : [], 
            "Ganancias totales" : self.rendCartera
        }   

    def agregarActivo(self,numAccion, Activos):
        self.__acciones[numAccion].append(Activos)

    # CARTERA CLIENTE 
    def rendCartera(self, bonificacion, volatilidad):   
        total = 0
        for i in range(len(Clientes.cartera)):
            total+=self.calcularRendAccion(Clientes.cartera[i], bonificacion, volatilidad)

        return total
    
    # BUSCAR MONEDA 

    def buscarID (self,idBuscar):
        i = 0
        encontrado = False

        while (i < self.__acciones or not encontrado):
            if (idBuscar == self.__acciones[i].getid):
                return i
            else: 
                i+=1

            return -1
        
    # CALCULAR RENDIMIENTO 

    def calcularRendAccion (self, idBuscado, bonificacion, volatilidad): 
        
        if (self.buscarID(idBuscado) == -1):
            return ValueError
        else: 
            return self.__acciones[self.buscarID(idBuscado)].calcularRendimiento(bonificacion,volatilidad)
    


    

    