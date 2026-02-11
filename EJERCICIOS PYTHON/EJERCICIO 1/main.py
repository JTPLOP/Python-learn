from Piso import *
from LocalComercial import *
from Gestion import *


#VARIABLES
opcion = ()
salida = False
idBuscado = ()

    #Variables calculo
impuesto = 0
extAsc = 0
extEscap = 0

    #CREAR GESTION
Inmuebles = []
Clientes = {}

miGestion = Gestion(Inmuebles, Clientes)

    #CREAR OBJETOS
Local1 = LocalComercial(100, "Babel Calle", 20, 10, False, "Supermercado", False)
Local2 = LocalComercial(230, "Babel Calle", 100, 10, False, "Gimnasio", True)
Piso1 = Piso(110, "Babel Calle", 100, 10, False, 4, 3, True)

miGestion.agregarInmu(Local1)
miGestion.agregarInmu(Piso1)
miGestion.agregarInmu(Local2)


print("Bienvenido a tu programa de confianza de gestiones de inmuebles.")
    
print(Local2.calcularIngresos(impuesto, extAsc, extEscap))
print(Piso1.calcularIngresos(impuesto, extAsc, extEscap))
print(Local1.calcularIngresos(impuesto, extAsc, extEscap))


while (not salida):
    print("Elija una opcion: ")
    print("1. Buscar por id")
    print("2. Calcular ganancias de un inmueble")
    print("3. Agregar clientes")
    print("4. Mostrar clientes")
    print("0. Salir del programa")

    opcion=int(input("Indicar: "))

    match(opcion):
        case 1:
                
            break
        case 2:
            idBuscado=(input("Indicame el id que busca: "))
            print(miGestion.calcularGanancias(idBuscado, impuesto, extAsc, extEscap))
            salida=True
            break
        case 0:
            print("Saliendo del programa.")
            salida=True
            break


print("El programa ha finalizado correctamente")






