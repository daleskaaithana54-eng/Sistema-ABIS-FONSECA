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

    estado= "Regiszstrado"

    if metodo.lower() == "yape":
        estado = "Por Verificar"
    texto = codigo + ";" + fecha + ";" + cliente + ";" + producto + ";" + str(cantidad) + ";" + str(precio) + ";" + str(total) + ";" + metodo + ";" + estado

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

def menu_ventas():
    opcion=""

    if not encontrado:
        print("Venta no encontrada.")

if __name__ == "__main__":
    menu_ventas()