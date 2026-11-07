# Registro de clientes

def registrar_cliente():
    print("\n--- REGISTRO DE CLIENTES ---")
    
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    archivo = open("clientes.txt", "a", encoding="utf-8")

    archivo.write(dni + "," + nombre+"," + apellido + ","+telefono+"\n")
    
    archivo.close()

    print("\nCliente registrado correctamente.")


# Consulta de clientes

def consultar_clientes():
    print("\n--- CONSULTA DE CLIENTES ---")

    try:
        archivo = open("clientes.txt", "r", encoding="utf-8")

        clientes = archivo.readlines()
        archivo.close()

        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for dato in clientes:
                datos = dato.strip().split(",")

                print("\nDNI:", datos[0])
                print("Nombre:", datos[1])
                print("Apellidos:", datos[2])
                print("Telefono:", datos[3])
    except FileNotFoundError:
        print("No existe el archivo de clientes.") 

# Busqueda de clientes

def buscar_clientes():
    print("\n--- BUSQUEDA DE CLIENTES ---")

    dni_buscar = input("Ingrese el DNI del cliente: ")
    encontrado = False     

    try:
        archivo = open("clientes.txt", "r", encoding="utf-8")
        clientes = archivo.readlines()
        archivo.close()

        for dato in clientes:
            datos = dato.strip().split(",")

            if datos[0] == dni_buscar:
                print("\nCliente encontrado")
                print("DNI:", datos[0])
                print("Nombre:", datos[1])
                print("Apellidos:", datos[2])
                print("Telefono:", datos[3])
                encontrado = True

    except FileNotFoundError:
        print("No existe el archivo de clientes.")
        return

    if encontrado == False:
        print("Cliente no encontrado.")

# Contar clientes registrados 

def contar_clientes():
    print("\n--- TOTAL DE CLIENTES ---")

    try: 
        archivo = open("clientes.txt", "r", encoding="utf-8")

        clientes = archivo.readlines()
        archivo.close()

        print("Cantidad de clientes registrados:", len(clientes))

    except FileNotFoundError:
     print("No hay clientes registrados.")

    
# Menu de clientes 

while True:
    print("\n--- MENU DE CLIENTES ---")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Buscar cliente")
    print("4. Contar clientes")
    print("5. salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        consultar_clientes()
    elif opcion == "3":
        buscar_clientes()
    elif opcion == "4":
        contar_clientes()
    elif opcion == "5":
        print("Saliendo del programa...")
        break 
    else:
        print("opcion incorrecta.")    
