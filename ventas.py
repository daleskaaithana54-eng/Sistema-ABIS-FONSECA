#Modulo de ventas

from archivos import leer_archivo,guardar_linea

def registrar_venta():
    codigo=input("Codigo de venta: ")
    fecha=input("Fecha (dd/mm/aaaa): ")
    cliente=input("Nombre del cliente")
    producto=input("Producto vendido: ")
    cantidad=input("Cantidad vendida: ")
    precio=float(input("Precio por unidad: S/"))
    total=cantidad * precio
    metodo=input("Metodo de pago (Efectivo/Yape): ")


    codigo=input("Ingrese codigo de venta:")
    producto=input("Ingrese producto:")
    precio=float(input("Ingrese precio: S/ "))
    cantidad=int(input("Ingrese cantidad: "))
    porcentaje= float(input("Ingrese descuento (%): "))
    subtotal=calcular_subtotal(precio,cantidad)
    descuento=aplicar_descuento(subtotal,porcentaje)
    total=calcular_total(subtotal,descuento)

    estado= "Regiszstrado"

    if metodo.lower() == "yape":
        estado = "Por Verificar"
    texto = codigo + ";" + fecha + ";" + cliente + ";" + producto + ";" + str(cantidad) + ";" + str(precio) + ";" + str(total) + ";" + metodo + ";" + estado


    ventas.append(venta)
    
    print("\nVenta registrada correctamente")
    print("Subtotal: S/", subtotal)
    print("Descuento: S/", descuento)
    print("Total: S/", total)

def consultar_ventas():
    print("\nVENTAS REGISTRADAS")

    if len(ventas) == 0:
       print("No hay ventas registradas.")
       return
    for venta in ventas:

    guardar_linea("datos/ventas.txt",texto)

print("\nVenta registrada correctamente.")
print("Total de la venta: S/", total)

if metodo.lower() == "yape":
    print("Estado:Por verificar")
    print("Verifica el pago en la aplicacion de Yape.")

def mostrar_ventas():
    lineas = leer_archivo("datos/ventas.txt")

    print("\nHISTORIAL DE VENTAS")

    if len(lineas) ==0:
        print("No hay ventas registradas.")
    else:
        for linea in lineas:
            datos = linea.strip().split(";")

        print("Codigo:", datos[0])
        print("Fecha:", datos[1])
        print("Cliente:", datos[2])
        print("Producto:", datos[3])
        print("Cantidad:", datos[4])
        print("Total:S/", datos[6])
        print("Pago:", datos[7])
        print("Estado:", datos[8])
def buscar_venta():
    codigo_buscar = input("Codigo de la venta que buscas: ")
    lineas=leer_archivo("datos/ventas.txt")
    encontrado = False

    for linea in lineas:
        datos = linea.strip().split(";")

        if datos[0] == codigo_buscar.lower():
            print("\nDETALLE DE LA VENTA")
            print("Codigo:", datos[0])
            print("Fecha:", datos[1])
            print("Cliente:", datos[2])
            print("Producto:", datos[3])
            print("Cantidad:", datos[4])
            print("Precio por unidad: S/", datos[5])
            print("Total:S/", datos[6])
            print("Pago:", datos[7])
            print("Estado:", datos[8])

            encontrado = True

    if encontrado ==False:
        print("No se encontro una venta con ese codigo.")

        print("\nCodigo:", venta["codigo"])
        print("Producto:", venta["producto"])
        print("Precio: S/", venta["precio"])
        print("Cantidad:", venta["cantidad"])
        print("Subtotal: S/", venta["subtotal"])
        print("Descuento: S/", venta["descuento"])
        print("Total: S/", venta["total"])
def menu_ventas():
        while True:
            print("\nMENU DE VENTAS")
            print("1. Registrar venta")
            print("2. Consultar ventas")
            print("3. Regresar al menu principal")

opcion=""

while opcion != "4":
        print("\nMenu de ventas")
        print("1. Registrar venta")
        print("2. Ver historial de ventas")
        print("3. Buscar venta")
        print("4. Volver al menu principal")


        if opcion == "1":
                registrar_venta()

        elif opcion == "2":
                consultar_ventas()

        elif opcion == "3":
                break

        else:
                print("Opcion invalida.")

        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            registar_venta()
        elif opcion == "2":
            mostrar_venta()
        elif opcion == "3":
            buscar_venta()
        elif opcion == "4":
            print("Volviendo al menu principal.")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu_ventas()

