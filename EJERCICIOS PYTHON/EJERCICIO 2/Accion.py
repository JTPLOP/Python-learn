from Activos import *

class Accion(Activo):
    def __init__(self, id, nombre, valIni, valAct, fechaAdq,nomEmpr):
        super().__init__(id, nombre, valIni, valAct, fechaAdq)
        self.__nomEmpr=nomEmpr

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Nombre Empresa: {self.__nomEmpr}")

    def calcularRendimiento(self,bonificacion,volatilidad):
        den=100
        if(self.__valIni < self.__valAct):
            return super().calcularRendimiento(bonificacion,volatilidad) + (super().calcularRendimiento(bonificacion,volatilidad)*bonificacion/den)
        else: 
            return super().calcularRendimiento(bonificacion,volatilidad)
        