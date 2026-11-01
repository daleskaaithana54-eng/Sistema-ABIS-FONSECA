from ventas import menu_ventas
from productos import menu_productos
from clientes import menu_clientes
from ingresos import menu_ingresos

def menu_principal():
    opcion = ""

    while opcion != "5":
        print("SISTEMA DE GESTION - ABIS FONSECA")
        print("Restaurant, Jugueria, Chifa")
        print("====================================")
        print("1. Ventas")
        print("2. Productos")
        print("3. Clientes")
        print("4. Ingresos")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            menu_ventas()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_clientes()
        elif opcion == "4":
            menu_ingresos()
        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
        else:
            print("Opcion no valida.")
            