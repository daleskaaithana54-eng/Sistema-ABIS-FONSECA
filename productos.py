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

def calcular_valor_total():
    lineas = leer_archivo("Datos/productos.txt")
    total = 0

    for linea in lineas:
        datos = linea.strip().split(";")
        total = total + float(datos[2])

    print("Valor total de los productos: S/", format(total, ".2f"))

def mostrar_producto_mas_caro():
    lineas = leer_archivo("Datos/productos.txt")
    
    if len(lineas) == 0:
        print("No hay productos disponibles.")
        return

    mayor = lineas[0].strip().split(";")

    for linea in lineas:
        datos = linea.strip().split(";")
        
        if float(datos[2]) > float(mayor[2]):
            mayor = datos
    
    print("\n---PRODUCTO MAS CARO---")
    print("Codigo:", mayor[0])
    print("producto:", mayor[1])
    print("precio: S/", mayor[2])
    
def mostrar_producto_mas_barato():
    lineas = leer_archivo("Datos/productos.txt")
    
    if len(lineas) == 0:
        print("No hay productos disponibles.")
        return

    menor = lineas[0].strip().split(";")

    for linea in lineas:
        datos = linea.strip().split(";")
        
        if float(datos[2]) < float(menor[2]):
            menor = datos
    
    print("\n---PRODUCTO MAS BARATO---")
    print("Codigo:", menor[0])
    print("producto:", menor[1])
    print("precio: S/", menor[2])

def mostrar_productos_por_precio():
    lineas = leer_archivo("Datos/productos.txt")
    productos = []

    if len(lineas) == 0:
        print("No hay productos disponibles.")
        return
    for linea in lineas:
        datos = linea.strip().split(";")
        productos.append(datos)

    for i in range(len(productos)):
        for j in range(i + 1, len(productos)):
            if float(productos[i][2]) > float(productos[j][2]):
                temporal = productos[i]
                productos[i] = productos[j]
                productos[j] = temporal
        
    print("\n---PRODUCTOS ORDENADOS POR PRECIO---")
    for producto in productos:
        print("Codigo:", producto[0],
              "|producto:", producto[1],
              "|precio: S/", producto[2])
def buscar_por_nombre():
    nombre_buscar = input("Nombre del producto: ").strip().lower()
    lineas = leer_archivo("Datos/productos.txt")
    encontrado = False
    
    for linea in lineas:
        datos = linea.strip().split(";")

        if nombre_buscar in datos[1].lower():
            print("Codigo:", datos[0])
            print("producto:", datos[1])
            print("precio: S/", datos[2])
            encontrado = True

    if encontrado == False:
        print("Producto no encontrado.")

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

    try:
        precio_numero = float(precio)
    except ValueError:
        print("El precio debe ser un numero.")
        return
    if precio_numero <= 0:
        print("El precio debe ser mayor que cero.")
        return

    texto = codigo + ";" + nombre + ";" + str(precio_numero)

    guardar_linea("Datos/productos.txt", texto)

    print("Producto registrado correctamente.")

def actualizar_producto():
        codigo = input("Codigo del producto: ").strip()
        lineas = leer_archivo("Datos/productos.txt")
        nuevos = []
        encontrado = False

        for linea in lineas:
            datos = linea.strip().split(";")

            if datos[0].lower() == codigo.lower():
                nombre = input("Nuevo nombre: ").strip()
                precio = input("Nuevo precio: S/ ").strip()
                
                if nombre == "" or precio == "":
                    print("Todos los campos son obligatorios.")
                    return
                try:
                    precio_numero = float(precio)
                except ValueError:
                    print("El precio debe ser un numero.")
                    return

                if precio_numero <= 0:
                    print("El precio debe ser mayor que cero.")
                    return

                nuevos.append(codigo + ";" + nombre + ";" + str(precio_numero))
                encontrado = True
            else:
                nuevos.append(linea.strip())

        if encontrado:
            guardar_archivo("Datos/productos.txt", nuevos)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

def eliminar_producto():
    codigo = input("Codigo del producto: ").strip()
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
        confirmar = input("Desea eliminar el producto? (s/n): ").strip().lower()

        if confirmar == "s":
            guardar_archivo("Datos/productos.txt", nuevos)
            print("Producto eliminado correctamente.")
        else:
            print("Eliminacion cancelada.")
    else:
        print("Producto no encontrado.")

def menu_productos():
    opcion = ""

    while opcion != "12":
        print("\n---MENU PRODUCTOS---")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Contar productos")
        print("7. Buscar por nombre")
        print("8. Mostrar productos por precio")
        print("9. Calcular valor total")
        print("10. Mostrar producto mas caro")
        print("11. Mostrar producto mas barato")
        print("12. volver")

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
            buscar_por_nombre()
        elif opcion == "8":
            mostrar_productos_por_precio()
        elif opcion == "9":
            calcular_valor_total()
        elif opcion == "10":
            mostrar_producto_mas_caro()
        elif opcion == "11":
            mostrar_producto_mas_barato()
        elif opcion == "12":
            print("Volviendo al menu principal.")
        else:
            print("Opcion  no valida.")