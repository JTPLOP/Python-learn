

class Inmueble:
    def __init__(self, id, direccion, metros2, precMen, estado): #ATRIBUTOS
        self.__id=id
        self.__direccion=direccion
        self.__metros2= metros2
        self.__precMen= precMen
        self.__estado=estado

#RECORDAR QUE LOS DOS GUIONES BAJO LO QUE NOS INDICA ES QUE EL ATRIBUTO SERA PRIVADO

    # HACEMOS LOS GETTERS 

    @property
    def getid(self):
        return self.__id
    
    @property
    def getdireccion(self):
        return self.__direccion
    
    @property
    def getmetros2(self):
        return self.__metros2
    
    @property
    def getprecMen(self):
        return self.__precMen
    
    @property 
    def isestado(self):
        return self.__estado
    
    # HACEMOS LOS SETTERS

    @getid.setter
    def setid(self,id):
        self.__id=id
    
    @getdireccion.setter
    def setdireccion(self,direccion):
        self.__direccion=direccion

    @getmetros2.setter
    def setmetros2(self,metros2):
        self.__metros2=metros2

    @getprecMen.setter
    def setprecMen(self,precMen):
        self.__precMen=precMen
    
    @isestado.setter
    def setestado(self, estado):
        self.__estado=estado


    # METODOS DE LA CLASE INMUEBLE 

    # METODO MOSTRAR

    def mostrarInformacion(self):
        print("Informacion del inmueble: ")
        print(f"Id: {self.__id}")
        print(f"Direccion: {self.__direccion}")
        print(f"Metros cuadrados: {self.__metros2}")
        print(f"Precio mensual: {self.__precMen}")
        print(f"Alquilado: {self.__estado}")

    # METODO 

    def calcularIngresos (self, impuesto, extAsc, extEscap):
        den = 100
        return self.__precMen - (self.__precMen*impuesto/den) # NOS DEVUELVE LA BASE DE LO QUE PAGAREMOS
