from Inmueble import * # NO ME ESTABA DEJANDO HACER USO DEL SUPER PQ SE ME OLVIDO IMPORTAR LA CLASE

class Piso(Inmueble):
    def __init__(self, id, direccion, metros2, precMen, estado, numHab, numBath, ascensor):
        super().__init__(id, direccion, metros2, precMen, estado)
        self.__numHab = numHab
        self.__numBath = numBath
        self.__ascensor = ascensor

    # GETTERS 

    @property
    def getnumHab(self):
        return self.__numHab
    
    @property
    def getnumBath (self):
        return self.__numBath
    
    @property
    def getascensor(self):
        return self.__ascensor
    
    # SETTERS

    @getnumHab.setter
    def setnumHab(self,numHab):
        self.__numHab= numHab

    @getnumBath.setter
    def setnumBath(self, numBath):
        self.__numBath= numBath

    @getascensor.setter
    def setascensor(self,ascensor):
        self.__ascensor=ascensor


    # METODOS 

    #REESCRITURA DE METODOS

    def mostrarInformacion(self):
        super().mostrarInformacion() # TRAEMOS CON SUPER LO PROVENIENTE DE LA CLASE MADRE
        print("Extras: ")
        print(f"Numero Habitaciones: {self.__numHab} ")
        print(f"Numero Bathrooms: {self.__numBath} ")
        print(f"Ascensor: {self.__ascensor}")

    def calcularIngresos(self, impuesto, extAsc, extEscap): #PARA ESTE EJERCICIO VAMOS A AGREGAR QUE SI TIENE ASCENSOR PAGA UN PORCENTAJE EXTRA
        den=100

        if (self.__ascensor):
            return super().calcularIngresos(impuesto, extAsc, extEscap) - (super().calcularIngresos(impuesto, extAsc, extEscap)*extAsc/den)
        else:
            return super().calcularIngresos(impuesto, extAsc, extEscap)+10