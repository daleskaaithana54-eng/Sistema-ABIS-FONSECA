# Validaciones

def validar_dni(dni):
        return len(dni) == 8 and dni.isdigit()

def validar_nombre(nombre):
        return nombre.replace(" ", "").isalpha()

def validar_telefono(telefono):
        return len(telefono) == 9 and telefono.isdigit()

# Leer clientes
def leer_clientes():
    try: 
        archivo = open("Datos/clientes.txt", "r", encoding="utf-8")
        clientes = archivo.readlines()
        archivo.close()
        return clientes
    except FileNotFoundError:
         return []
    
# Verificar si el DNI ya existe
def dni_existe(dni):
    clientes = leer_clientes()

    for liena in clientes:
     datos = datos.strip().split(",")

    if len(datos) == 4 and datos[0] == dni:
         return True
    return False
  
# Registrar clientes 
def registrar_cliente():
      print("\n--- REGISTRO DE CLIENTES ---")

      dni = input("Ingrese DNI: ")

      while validar_dni(dni) == False or dni_existe(dni) == True:
            print("DNI incorrecto o ya registrado.")
      dni = input("Ingrese DNI nuevamente: ")

      nombre = input("Ingrese nombre: ")

      while validar_nombre(nombre) == False:
            print("Ingrese solamente letras. ")
      nombre = input("Ingrese nombre nuevamente: ")

      apellido = input("Ingrese apellido: ")

      while validar_nombre(apellido) == False:
            print("Ingrese solamente letras. ")
      apellido = input("Ingrese apellido nuevamente: ")

      telefono = input("Ingrese telefono: ") 

      while validar_telefono(telefono) == False:
       print("El telefono debe tener 9 numeros.")
       telefono = input("Ingrese telefono: ")    

      archivo = open("Datos/clientes.txt", "a", encoding="utf-8")
      archivo.write(dni + "," + nombre + "," + apellido + "," + telefono + "\n")
      archivo.close()

print("Cliente registrado correctamente.")

# Consultar clientes 
def consultar_clientes():
      print("\n--- CONSULTA DE CLIENTES ---")
      clientes = leer_clientes()

      if not clientes:
            print("No hay clientes registrados.")
            return

      for linea in clientes:
            datos = linea.strip().split(",")
            if len(datos) == 4:
                  print("\nDNI:", datos[0])
                  print("Nombre:", datos[1])
                  print("Apellido:", datos[2])
                  print("Telefono:", datos[3])
                
# Buscar clientes
def buscar_clientes():
      dni = input("Ingrese DNI: ")

      for linea in leer_clientes():
            datos = linea.strip().split(",")
            if len(datos) == 4 and datos[0] == dni:
                  print("DNI:", datos[0])
                  print("Nombre:", datos[1])
                  print("Apellido:", datos[2])
                  print("Telefono:", datos[3])
                  return

      print("Cliente no encontrado.")

# Contar clientes
def contar_clientes():
      cantidad = 0
      for linea in leer_clientes():
            if len(linea.strip().split(",")) == 4:
                  cantidad += 1
      print("Cantidad de clientes:", cantidad)


# Actualizar clientes
def actualizar_clientes():
        dni = input("Ingrese DNI del cliente: ")  
        clientes = leer_clientes()
        encotrado = False       


        for i in range(len(clientes)):
              datos = clientes[i].strip().split(",")

              if len(datos) == 4 and datos[0] == dni:
                nombre = input("Nuevo nombre: ")
                while not validar_nombre(nombre):
                      print("Ingrese solamente letras.")
                      nombre= input("Nuevo nombre: ")

              apellido = input("Nuevo apellido: ")
              while not validar_nombre(apellido):
                    print("Ingrese solamente letras.")
                    apellido= input("Nuevo apellido: ")

              telefono = input("Nuevo telefono: ")
              while not validar_telefono(telefono):
                    print("El telefono debe tener 9 numeros.")
                    telefono = input("Nuevo telefono: ")

              clientes[1] = dni + "," + nombre + "," + apellido + "," + telefono + "\n"
              encontrado = True
              break

        if encontrado:
              archivo = open("Datos/clientes.txt", "w", encoding="utf-8")
              archivo.writelines(clientes)
              archivo.close()
              print("Cliente actualizado correctamente.")
        else:
              print("Cliente no encontrado. ")

# Eliminar clientes
def eliminar_clientes():
      dni = input("Ingrese DNI del cliente: ")
      clientes = leer_clientes()
      nuevos = []
      encontrado = False

      for linea in clientes:
            datos = linea.strip().split(",")
            if len(datos) == 4 and datos[0] == dni:
                  encontrado = True
            else:
                  nuevos.append(linea)

            if encontrado:
                  archivo =open("Datos/clientes.txt", "w", encoding="utf-8")
                  archivo.writelines(nuevos)
                  archivo.close()
                  print("Cliente eliminado correctamente.")
      else:
            print("Cliente no encontrado")

# Menu de clientes
def menu_clientes():
    while True:
          print("\n--- MENU DE CLIENTES ---")
          print("1. Registrar cliente")
          print("2. Consultar cliente")
          print("3. Buscar cliente")
          print("4. Contar clientes")
          print("5. Actualizar cliente")
          print("6. Eliminar cliente")
          print("7. Salir")

          opcion = input("Seleccione una opción: ")

          if opcion == "1":
             registrar_cliente()
          elif opcion == "2":
            consultar_clientes()
          elif opcion == "3":
            buscar_clientes()
          elif opcion == "4":
            contar_clientes()
          elif opcion == "5":
           actualizar_clientes()
          elif opcion == "6":
            eliminar_clientes()
          elif opcion == "7":
            print("Saliendo del programa...")
          break

    else:
     print("Opcion incoreecta.")

if __name__ == "__main__":
   menu_clientes()

              


    
                  
