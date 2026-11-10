# MODULO DE GESTION DE PRODUCTOS 

PRODUCTOS = [ 
    {"codigo": "P001", "nombre": "Lomo saltado", "precio": 18.00},
    {"codigo": "P002", "nombre": "Arroz chaufa", "precio": 14.00},
    {"codigo": "P003", "nombre": "Menu del dia", "precio": 11.00},
    {"codigo": "P004", "nombre": "Jugo de papaya", "precio": 8.00},
    {"codigo": "P005", "nombre": "Jugo de fresa", "precio": 8.00},
    {"codigo": "P006", "nombre": "pollo broaster", "precio": 15.00},
    {"codigo": "P007", "nombre": "Caldo de gallina", "precio": 10.00},
    {"codigo": "P008", "nombre": "Ceviche", "precio": 20.00},
    {"codigo": "P009", "nombre": "Aji de gallina", "precio": 17.00},
    {"codigo": "P010", "nombre": "Arroz con pollo", "precio": 15.00},
    {"codigo": "P011", "nombre": "Papa a la huancaina", "precio": 9.00},
    {"codigo": "P012", "nombre": "Anticuchos", "precio": 12.00},
    {"codigo": "P013", "nombre": "Chicharron de pollo", "precio": 16.00},
    {"codigo": "P014", "nombre": "salchipapa", "precio": 12.00},
    {"codigo": "P015", "nombre": "Pollo al horno", "precio": 12.00},
    {"codigo": "P016", "nombre": "Inka cola", "precio": 5.00},
    {"codigo": "P017", "nombre": "Coca cola", "precio": 5.00},
    {"codigo": "P018", "nombre": "Limonada", "precio": 5.00},
    {"codigo": "P019", "nombre": "Jugo de naranja", "precio": 8.00},
    {"codigo": "P020", "nombre": "Cafe pasado", "precio": 4.00},
]


# REGISTRAR PRODUCTO
def registrar_producto():
    print("\n---- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese codigo: ").upper().strip()
    
    if codigo == "":
        print("Debe ingresar un codigo.")
        return

    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            print("El producto ya existe.")
            return

    nombre = input("Ingrese nombre: ").strip()

    if nombre == "":
        print("Debe ingresar un nombre.")
        return

    try:
        precio = float(input("Ingrese precio: "))

        if precio <=0:
            print("El precio debe ser mayor que cero.")
            return

    except ValueError:
        print("Ingrese un precio numerico.")
        return

    nuevo = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio
    }
    PRODUCTOS.append(nuevo)
    print("Producto registrado correctamente.")

# CONSULTAR PRODUCTOS
def consultar_productos():
    print("\n---- PRODUCTOS REGISTRADOS ---")
    
    for producto in PRODUCTOS:
        print(producto["codigo"],"-", producto["nombre"],"-S/", producto["precio"])

#BUSCAR PRODUCTO
def buscar_producto():
    print("\n---- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese codigo del producto: ").upper().strip()

    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Precio: S/", producto["precio"])
            return

    print("Producto no encontrado.")


#ACTUALIZAR PRODUCTO
def actualizar_producto():
    print("\n---- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese codigo: ").upper().strip()

    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            nombre = input("nuevo nombre: ").strip()

            if nombre == "":
                print("Debe ingresar un nombre.")
                return
            
            if nombre == "":
                print("Debe ingresar un nombre.")
                return

            try:
                precio=float(input("nuevo precio: "))

                if precio <=0:
                    print("El precio debe ser mayor que cero.")
                    return

            except ValueError:
                print("Ingrese un precio numerico.")
                return
            
            producto["nombre"] = nombre
            producto["precio"] = precio

            print("Producto actualizado correctamente.")
            return

    print("Producto no encontrado.")


#ELIMINAR PRODUCTO
def eliminar_producto():
    print("\n---- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese codigo: ").upper().strip()

    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            PRODUCTOS.remove(producto)
            print("Producto eliminado correctamente.")
            return

    print("Producto no encontrado.")


#MOSTRAR MENU DE PRODUCTOS
def menu_productos():
    print("\n---- MENU DE PRODUCTOS ---")

    for producto in PRODUCTOS:
        print(producto["codigo"],"-", producto["nombre"],"-S/", producto["precio"])


#MENU PRINCIPAL DE PRODUCTOS
def mostrar_menu():
 
    while True:
        print("\n================================")
        print("        GESTION DE PRODUCTOS")
        print("================================")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Mostrar menu del restaurante")
        print("7. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            consultar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            actualizar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            menu_productos()

        elif opcion == "7":
            print("Saliendo del modulo de productos.")
            break

        else:
            print("Opcion incorrecta.")

if __name__ == "__main__":
    mostrar_menu()