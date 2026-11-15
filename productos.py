from archivos import leer_archivo, guardar_linea


def mostrar_productos():
    lineas = leer_archivo("datos/productos.txt")
    
    print("\n---PRODUCTOS DISPONIBLES---")
    if len (lineas) == 0:
        print("No hay productos disponibles.")
    else:
        for linea in lineas:
            datos = linea.strip().split(",")
            print("Codigo:", datos[0],
                   "|producto:", datos[1],
                   "|precio: S/", datos[2],)

def buscar_producto():
    codigo_buscar = input("Codigo del producto: ")
    lineas = leer_archivo("datos/productos.txt")
    encontrado = False
    
    for linea in lineas:
        datos = linea.strip().split(",")

        if datos[0].lower() == codigo_buscar.lower():
            print("producto:", datos[1])
            print("precio: S/", datos[2])
            encontrado = True

    if encontrado == False:
        print("No se encontro el producto.")

def agregar_producto():
    codigo = input("Codigo nuevo: ")
    nombre = input("Nombre del producto: ")
    precio = input("Precio de venta: S/ ")

   texto = codigo + "," + nombre + "," + precio

    guardar_linea("datos/productos.txt", texto)

    print("Producto registrado correctamente.")

def menu_productos():
    opcion = ""

    while opcion != "4":
        print("\n---MENU PRODUCTOS---")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. volver")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            print("Volviendo al menu principal.")
        else:
            print("Opcion  no valida.")