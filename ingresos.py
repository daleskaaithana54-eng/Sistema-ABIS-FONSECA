from archivos import leer_archivo, guardar_linea


def registrar_ingreso():
    fecha = input("Fecha (dd/mm/aaaa): ")
    descripcion = input("Descripcion del ingreso: ")
    monto = input("Monto recibido: S/ ")
    origen = input("Origen del ingreso: ")

    texto = fecha + ";" + descripcion + ";" + monto + ";" + origen

    guardar_linea("datos/ingresos.txt", texto)

    print("Ingreso registrado correctamente.")


def mostrar_ingresos():
    lineas = leer_archivo("datos/ingresos.txt")

    print("\n--- INGRESOS REGISTRADOS ---")

    if len(lineas) == 0:
        print("No hay ingresos registrados.")
    else:
        for linea in lineas:
            datos = linea.strip().split(";")

            print("Fecha:", datos[0],
                  "| Descripcion:", datos[1],
                  "| Monto: S/", datos[2],
                  "| Origen:", datos[3])


def menu_ingresos():
    opcion = ""

    while opcion != "0":
        print("\n--- MENU DE INGRESOS ---")
        print("0. Volver")
        print("1. Registrar ingreso")
        print("2. Mostrar ingresos")
        

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            mostrar_ingresos()
        elif opcion == "0":
            print("Volviendo al menu principal.")
        else:
            print("Opcion no valida.")