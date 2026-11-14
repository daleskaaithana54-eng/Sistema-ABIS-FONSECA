# Registro de clientes

from archivos import leer_archivo, guardar_linea

def mostrar_clientes():
    lineas = leer_archivo("datos/clientes.txt")

    print("\n--- CLIENTES REGISTRADOS ---")

    if len(lineas) == 0:
        print("No hay clientes registrados.")
    else:
        for linea in lineas:
            datos = linea.strip().split(";")

            print("Codigo:", datos[0],
                  "| Nombre:", datos[1],
                  "| Telefono:", datos[2])


def buscar_cliente():
    codigo_buscar = input("Codigo del cliente: ")

    lineas = leer_archivo("datos/clientes.txt")
    encontrado = False

    for linea in lineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == codigo_buscar.lower():
            print("Cliente:", datos[1])
            print("Telefono:", datos[2])
            encontrado = True

    if encontrado == False:
        print("No se encontro el cliente.")


def registrar_cliente():
    codigo = input("Codigo del cliente: ")
    nombre = input("Nombre del cliente: ")
    telefono = input("Telefono: ")

    texto = codigo + ";" + nombre + ";" + telefono

    guardar_linea("datos/clientes.txt", texto)

    print("Cliente registrado correctamente.")


def menu_clientes():
    opcion = ""

    while opcion != "4":
        print("\n--- MENU DE CLIENTES ---")
        print("1. Mostrar clientes")
        print("2. Buscar cliente")
        print("3. Registrar cliente")
        print("4. Volver")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            registrar_cliente()
        elif opcion == "4":
            print("Volviendo al menu principal.")
        else:
            print("Opcion no valida.")
    
