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

registrar_cliente()
    
