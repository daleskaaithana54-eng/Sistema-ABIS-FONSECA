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
    lineas = leer_archivo("Datos/ingresos.txt")

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

def cargar_registros():
    registros = []

    for linea in leer_archivo("Datos/ingresos.txt"):
        datos = linea.strip().split(";")
        if len(datos) == 4:
            registros.append(datos)

    return registros

def guardar_registros(registros):
    with open("Datos/ingresos.txt", "w", encoding="utf-8") as archivo:
        for datos in registros:
            archivo.write(datos[0] + ";" + datos[1] + ";" + datos[2] + ";" + datos[3] + "\n")

def a_monto(texto):
    numero = texto.strip().replace(",", ".")
    if numero.replace(".", "", 1).isdigit():
        return float(numero)
    return 0

def mostrar_lista(registros):
    if len(registros) == 0:
        print("No hay ingresos para mostrar.")

    for i in range(len(registros)):
        datos = registros[i]
        print(i + 1, ". Fecha:", datos[0], "| Descripcion:", datos[1],
              "| Monto: S/", datos[2], "| Origen:", datos[3])

def buscar_ingresos():
    texto = input("Texto a buscar: ").strip().lower()
    encontrados = []

    for datos in cargar_registros():
        if datos[1].lower().find(texto) != -1 or datos[3].lower().find(texto) != -1:
            encontrados.append(datos)

    print("\n--- RESULTADOS ---")
    mostrar_lista(encontrados)

def ordenar_ingresos():
    registros = cargar_registros()
    n = len(registros)

    for pasada in range(n - 1):
        for i in range(n - 1 - pasada):
            if a_monto(registros[i][2]) < a_monto(registros[i + 1][2]):
                temp = registros[i]
                registros[i] = registros[i + 1]
                registros[i + 1] = temp

    print("\n--- DE MAYOR A MENOR ---")
    mostrar_lista(registros)

def modificar_ingreso():
    registros = cargar_registros()

    print("\n--- MODIFICAR INGRESO ---")
    mostrar_lista(registros)

    if len(registros) == 0:
        return

    numero = input("Numero de ingreso (0 para cancelar): ").strip()

    while not (numero.isdigit() and int(numero) <= len(registros)):
        numero = input("Numero no valido. Intenta de nuevo: ").strip()

    numero = int(numero)

    if numero == 0:
        print("Modificacion cancelada.")
        return

    nuevo = input("Nuevo monto: S/ ")
    if a_monto(nuevo) > 0:
        registros[numero - 1][2] = nuevo.strip()
        guardar_registros(registros)
        print("Ingreso modificado correctamente.")
    else:
        print("Monto no valido. No se hizo ningun cambio.")

def menu_ingresos():
    opcion = ""

    while opcion != "0":
        print("\n--- MENU DE INGRESOS ---")
        print("1. Registrar ingreso")
        print("2. Mostrar ingresos")
        print("3. Buscar ingresos")
        print("4. Ordenar por monto")
        print("5. Modificar ingreso")
        print("0. Volver")
        

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            mostrar_ingresos()
        elif opcion == "3":
            buscar_ingresos()
        elif opcion == "4":
            ordenar_ingresos()
        elif opcion == "5":
            modificar_ingreso()
        elif opcion == "0":
            print("Volviendo al menu principal.")
        else:
            print("Opcion no valida.")