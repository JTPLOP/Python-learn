
class Clientes:
    def __init__(self, id, nombre, direccion, cartera):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cartera = cartera

    @property
    def getid (self):
        return self.__id
    
    @property  
    def getNombre(self):
        return self.__nombre
    
    @property
    def getDireccion(self):
        return self.__direccion
    
    @property
    def getcartera(self):
        return self.__saldo
    
    # SETTERS

    @getid.setter
    def id(self, id):
        self.__id= id

    @getNombre.setter
    def nombre(self, nombre):
        self.__nombre= nombre
    
    @getDireccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @getcartera.setter 
    def cartera(self, cartera):
        self.__cartera = cartera


    # MOSTRAR DATOS DEL CLIENTES

    def mostrarDatos (self):
        print("Datos del cliente:")
        print(f"ID: {self.__id}")
        print(f"Nombre: {self.__nombre}")
        print(f"Direccion: {self.__direccion}")
        print(f"Cartera: {self.__cartera}")