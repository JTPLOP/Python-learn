from Inmueble import * 

class LocalComercial(Inmueble):
    
    def __init__(self, id, direccion, metros2, precMen, estado, tipoNegoc, escaparate):
        super().__init__(id, direccion, metros2, precMen, estado)
        self.__tipoNegoc = tipoNegoc
        self.__escaparate = escaparate

    # GETTERS

    @property
    def gettipoNegoc(self):
        return self.__tipoNegoc
    
    @property
    def getescaparate (self):
        return self.__escaparate
    
    # SETTERS

    @gettipoNegoc.setter
    def settipoNegoc(self,tipoNegoc):
        self.__tipoNegoc= tipoNegoc

    @getescaparate.setter
    def setescaparate(self, escaparate):
        self.__escaparate= escaparate

    # METODOS 

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print("Extras: ")
        print(f"Tipo de negocio: {self.__tipoNegoc}")
        print(f"Escaparate: {self.__escaparate}")

    def calcularIngresos(self, impuesto, extAsc, extEscap): #AGREGAMOS UN EXTRA SI NO TIENE ESCAPARATE
        den=100

        if (self.__escaparate):
            return super().calcularIngresos(impuesto, extAsc, extEscap) - (super().calcularIngresos(impuesto, extAsc, extEscap)*extEscap/den)
        else:
            devuelto = (super().calcularIngresos(impuesto, extAsc, extEscap) + 100)
            return devuelto  

    