from ventas import menu_ventas
from productos import menu_productos
from clientes import menu_clientes
from ingresos import menu_ingresos
from archivos import leer_archivo, guardar_linea

def menu_principal():
    opcion = ""

    while opcion != "6":
        print("SISTEMA DE GESTION - ABIS FONSECA")
        print("Restaurant, Jugueria, Chifa")
        print("====================================")
        print("1. Ventas")
        print("2. Productos")
        print("3. Clientes")
        print("4. Ingresos")
        print("5. Gestion de archivos")
        print("6. Salir")

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
            submenu_archivos()
        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
        else:
            print("Opcion no valida")

def submenu_archivos():
    opcion_archivos = ""

    while opcion_archivos != "3":
        print("\n SUBMENU DE ARCHIVOS ")
        print("1. Guardar informacion")
        print("2. Leer informacion")
        print("3. Volver al menu principal")

        opcion_archivos = input("Selecciona una opcion: ")

        if opcion_archivos == "1":
            texto = input("Ingresa la informacion: ")
            guardar_linea("Datos/prueba_archivos.txt", texto)
            print("\nInformacion guardada correctamente.")

        elif opcion_archivos == "2":
            lineas = leer_archivo("Datos/prueba_archivos.txt")

            print("\n INFORMACION GUARDADA ")

            for linea in lineas:
                print(linea.strip())

        elif opcion_archivos == "3":
            print("Volviendo al menu principal.")

        else:
            print("Opcion no valida.")


            