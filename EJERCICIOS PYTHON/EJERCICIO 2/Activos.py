
class Activo:
    def __init__(self,id, nombre, valIni, valAct, fechaAdq):
        self.__id = id
        self.__nombre = nombre
        self.__valIni = valIni
        self.__valAct = valAct
        self.__fechaAdq = fechaAdq
    
    @property
    def getid (self):
        return self.__id
    
    @getid.setter
    def id(self, id):
        self.__id=id

    #METODOS 

    def calcularRendimiento(self, bonificacion,volatilidad):
        num=100

        if (self.__valIni > 0):
            return (self.__valAct - self.__valIni)/self.__valIni*100
        else: 
            return 0
        
    def mostrarDatos (self):
        print("Información del activo: ")
        print(f"ID: {self.__id}")
        print(f"Nombre: {self.__nombre}")
        print(f"Valor Inicial: {self.__valIni}")
        print(f"Valor Actual: {self.__valAct}")
        print(f"Fecha de Adquisicion: {self.__fechaAdq}")
         




    
    