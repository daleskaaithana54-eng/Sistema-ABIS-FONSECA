#Modulo de ventas

from archivos import leer_archivo,guardar_linea

def registrar_venta():
    codigo = input("Codigo de venta: ")
    fecha=input("Fecha (dd/mm/aaaa): ")
    cliente=input("Nombre del cliente")
    producto=input("Producto vendido: ")
    cantidad=int(input("Cantidad vendida: "))
    precio=float(input("Precio por unidad: S/"))
    porcentaje=float(input("Descuento (%)"))
    metodo=input("Metodo de pago (Efectivo/Yape): ")

    subtotal = precio * cantidad
    descuento = subtotal * (porcentaje / 100)
    total = subtotal - descuento 

    estado= "Por verificar" if metodo.lower() == "yape" else "Registrado"
    
    texto = codigo + ";" + fecha + ";" + cliente + ";" + producto + ";" + str(cantidad) + ";" + str(precio) + ";" + str(total) + ";" + metodo + ";" + estado
    guardar_linea("datos/ventas.txt", texto)
    
    print("\nVenta registrada correctamente")
    print("Subtotal: S/", subtotal)
    print("Descuento: S/", descuento)
    print("Total: S/", total)

def consultar_ventas():
    lineas = leer_archivo("datos/ventas.txt")
    print("\nVENTAS REGISTRADAS")

    if len(lineas) == 0:
        print("No hay ventas registradas.")
        return
    for linea in lineas:
        datos= linea.strip().split(";")
        print("Codigo:" , datos[0])
        print("Fecha:" , datos[1])
        print("Cliente:" , datos[2])
        print("Producto:" , datos[3])
        print("Cantidad:" , datos[4])
        print("Total:S/", datos[6])
        print("Pago:" , datos[7])
        print("Estado:" , datos[8])

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
    if not encontrado:
        print("No se encontro una venta con ese codigo.")

def menu_ventas():
        while True:
            print("\nMENU DE VENTAS")
            print("1. Registrar venta")
            print("2. Consultar ventas")
            print("3. Buscar venta")
            print("4. Volver al menu principal")
            opcion = input("Selecciona una opcion: ")
            if opcion == "1":
                registrar_venta()
            elif opcion == "2":
                consultar_ventas()
            elif opcion == "3":
                buscar_venta()
            elif opcion == "4":
                break
            else:
             print("Opcion no valida.")

if __name__ == "__main__":
    menu_ventas()

