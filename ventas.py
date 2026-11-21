#Modulo de ventas

#Registrar los pedidos que se ingresen desde menu.py
listas_ventas = []

def calcular_subtotal(precio_unitario:float,cantidad:int)->float:
    "Calcula el subtotal multiplicando el precio unitario por la cantidad"
    subtotal = precio_unitario * cantidad
    return round(subtotal,2)

def aplicar_descuento(subtotal:float, porcentaje_descuento:float = 0.0) -> float:
    "Calcula el descuento aplicando el porcentaje de descuento al subtotal"
    return round(subtotal* (porcentaje_descuento/100),2)

    
def calcular_total(subtotal:float,descuento:float)-> float:
    "Calcula el monto final a pagar tras aplicar descuentos"
    return round(subtotal - descuento,2)
    
def registrar_venta(id_venta:str,mesa_o_cliente:str,plato:str,cantidad:int,precio_unitario:float,porcentaje_descuento:float=0.0)->dict:
    "Recibe los datos capturados en el menu, calcula los montos y guarda la comanda en la lista general"
    subtotal = calcular_subtotal(precio_unitario,cantidad)
    descuento = aplicar_descuento(subtotal,porcentaje_descuento)
    total = calcular_total(subtotal,descuento)

    venta = {
        "id_venta": str(id_venta).strip(),
        "cliente": str(mesa_o_cliente).strip(),
        "plato": str(plato).strip(),
        "cantidad": int(cantidad),
        "precio_unitario": float(precio_unitario),
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total
    }
    listas_ventas.append(venta)
    return venta

def consultar_ventas()->list:
    "Retorna todas las ventas guardadas"
    return listas_ventas

def buscar_venta(id_venta:str)->dict:
    
    "Busca un ticket por su identificador"
    id_busqueda = str(id_venta).strip().lower()
    for venta in listas_ventas:
        if venta["id_venta"].lower() == id_busqueda:
            return venta
    return None
    
