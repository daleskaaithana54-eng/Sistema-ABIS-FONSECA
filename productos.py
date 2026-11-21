from archivos import leer_archivo, guardar_linea, guardar_archivo


def mostrar_productos():
    lineas = leer_archivo("Datos/productos.txt")
    
    print("\n---PRODUCTOS DISPONIBLES---")
    if len (lineas) == 0:
        print("No hay productos disponibles.")
    else:
        for linea in lineas:
            datos = linea.strip().split(";")
            print("Codigo:", datos[0],
                   "|producto:", datos[1],
                   "|precio: S/", datos[2],)

def contar_productos():
    lineas = leer_archivo("Datos/productos.txt")
    print("Total de productos:", len(lineas))

def buscar_producto():
    codigo_buscar = input("Codigo del producto: ").strip()
    lineas = leer_archivo("Datos/productos.txt")
    encontrado = False
    
    for linea in lineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == codigo_buscar.lower():
            print("producto:", datos[1])
            print("precio: S/", datos[2])
            encontrado = True

    if encontrado == False:
        print("No se encontro el producto.")


def agregar_producto():
    codigo = input("Codigo nuevo: ").strip()

    lineas = leer_archivo("Datos/productos.txt")

    for linea in lineas:
        datos = linea.strip().split(";")
        if datos[0].lower() == codigo.lower():
            print("El codigo ya existe.")
            return
    nombre = input("Nombre del producto: ").strip()
    precio = input("Precio de venta: S/ ").strip()

    if codigo == "" or nombre == "" or precio == "":
        print("Todos los campos son obligatorios.")
        return

    texto = codigo + ";" + nombre + ";" + precio

    guardar_linea("Datos/productos.txt", texto)

    print("Producto registrado correctamente.")

def actualizar_producto():
        codigo = input("Codigo del producto:")
        lineas = leer_archivo("Datos/productos.txt")
        nuevos = []
        encontrado = False

        for linea in lineas:
            datos = linea.strip().split(";")

            if datos[0].lower() == codigo.lower():
                nombre = input("Nuevo nombre: ")
                precio = input("Nuevo precio: S/ ")
                nuevos.append(codigo + ";" + nombre + ";" + precio)
                encontrado = True
            else:
                nuevos.append(linea.strip())

        if encontrado:
            guardar_archivo("Datos/productos.txt", nuevos)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

def eliminar_producto():
    codigo = input("Codigo del producto: ")
    lineas = leer_archivo("Datos/productos.txt")
    nuevos = []
    encontrado = False

    for linea in lineas:
        datos = linea.strip().split(";")

        if datos[0].lower() == codigo.lower():
            encontrado = True
        else:
            nuevos.append(linea.strip())

    if encontrado:
        guardar_archivo("Datos/productos.txt", nuevos)
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

def menu_productos():
    opcion = ""

    while opcion != "6":
        print("\n---MENU PRODUCTOS---")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Contar productos")
        print("7. volver")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            contar_productos()
        elif opcion == "7":
            print("Volviendo al menu principal.")
        else:
            print("Opcion  no valida.")