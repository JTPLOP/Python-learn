from Activos import *

class Criptomonedas (Activo):
    def __init__(self, id, nombre, valIni, valAct, fechaAdq, blockchain):
        super().__init__(id, nombre, valIni, valAct, fechaAdq)
        self.__blockchain = blockchain

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"Blockchain: {self.__blockchain}")

    def calcularRendimiento(self, bonificacion, volatilidad):
        den = 100
        if(super().calcularRendimiento(bonificacion,volatilidad) >=0 ):
            return super().calcularRendimiento(bonificacion,volatilidad) - (super().calcularRendimiento(bonificacion,volatilidad)*volatilidad/den)
        else: 
            return super().calcularRendimiento(bonificacion, volatilidad)