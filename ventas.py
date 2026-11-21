#Modulo de ventas

#Registrar los pedidos que se ingresen desde menu.py
Ventas=[]

def calcular_subtotal(precio,cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal,porcentaje):
    return subtotal *(porcentaje/100)

    
def calcular_total(subtotal,descuento):
    return subtotal - descuento
    
def registrar_venta():
    print("\n=== REGISTRAR VENTA ===")

    codigo=input("Ingrese codigo de venta:")
    producto=input("Ingrese producto:")
    precio=float(input("Ingrese precio: S/ "))
    cantidad=int(input("Ingrese cantidad: "))
    porcentaje=float(input("Ingrese descuento (%): "))
    subtotal=calcular_subtotal(precio,cantidad)
    descuento=aplicar_descuento(subtotal,porcentaje)
    total=calcular_total(subtotal,descuento)

    venta = {
        "codigo": codigo,
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total
    }

    ventas.append(venta)
    
print("\nVenta registrada correctamente")
print("Subtotal: S/",subtotal)
print("Descuento: S/",descuento)
print("Total: S/",total)

def consultar_ventas():
    print("\n=== CONSULTAR VENTAS ===")
    if len(ventas) == 0:
       print("No hay ventas registradas.")
       return
for venta in ventas:
    print("\nCodigo:", venta["codigo"])
    print("Producto:", venta["producto"])
    print("Precio: S/", venta["precio"])
    print("Cantidad:", venta["cantidad"])
    print("Subtotal: S/", venta["subtotal"])
    print("Descuento: S/", venta["descuento"])
    print("Total: S/", venta["total"])

    def buscar_venta():
        print("\n=== BUSCAR VENTA ===")
        codigo = input("Ingrese codigo de venta:")
        for venta in ventas:
            if venta["codigo"] == codigo:
                print("\nVenta encontrada:")
                print("Codigo:",venta["codigo"])
                print("Producto:",venta["producto"])
                print("Cantidad:", venta["cantidad"])
                print("Total: S/", venta["total"])
                return
        print("No se encontro la venta")

    def menu_ventas():
        while True:
            print("\n=== MENU DE VENTAS ===")
            print("1. Registrar venta")
            print("2. Consultar ventas")
            print("3. Buscar venta")
            print("4. Regresar al menu principal")

            opcion = input("Seleccione una opcion:")

            if opcion == "1":
                registrar_venta()

            elif opcion == "2":
                consultar_ventas()

            elif opcion == "3":
                buscar_venta()

            elif opcion == "4":
                break

            else:
                print("Opcion invalida.")
    
