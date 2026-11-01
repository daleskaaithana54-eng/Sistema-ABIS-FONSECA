def seleccionar_tipo_ingreso():
    tipos = ["Sueldo", "Venta", "Otros"]

    print("Tipos de ingreso:")
    for i in range(len(tipos)):
        print(f"{i + 1}. {tipos[i]}")

    texto = input("Elige un tipo: ").strip()
    while not texto.isdigit() or int(texto) < 1 or int(texto) > len(tipos):
        texto = input("Opcion invalida. Elige un tipo: ").strip()
    opcion = int(texto)

    return tipos[opcion - 1]


def registrar_ingreso(ingresos):
    tipo = seleccionar_tipo_ingreso()

    texto_monto = input("Monto: S/ ").strip()
    while not texto_monto.replace(".", "", 1).isdigit() or float(texto_monto) <= 0:
        texto_monto = input("Monto invalido (debe ser un numero mayor que 0). Monto: S/ ").strip()
    monto = float(texto_monto)

    descripcion = input("Descripcion: ").strip()
    while len(descripcion) == 0:
        descripcion = input("La descripcion no puede estar vacia. Descripcion: ").strip()

    ingreso = {"tipo": tipo, "monto": monto, "descripcion": descripcion}
    ingresos.append(ingreso)
    print("Ingreso registrado.")


def calcular_total_ingresos(ingresos):
    total = 0
    for ingreso in ingresos:
        total = total + ingreso["monto"]
    return total


def consultar_ingresos(ingresos):
    if len(ingresos) == 0:
        print("No hay ingresos registrados.")
    else:
        print("--- Ingresos registrados ---")
        for i in range(len(ingresos)):
            ingreso = ingresos[i]
            print(f"{i + 1}. {ingreso['tipo']} - S/ {ingreso['monto']} - {ingreso['descripcion']}")
        print(f"Total: S/ {calcular_total_ingresos(ingresos)}")


def buscar_ingreso(ingresos):
    print("Buscar ingresos")
    print("1. Por tipo")
    print("2. Por descripcion")
    criterio = input("Elige una opcion: ").strip()
    while criterio != "1" and criterio != "2":
        criterio = input("Opcion invalida. Elige 1 o 2: ").strip()

    encontrados = []
    if criterio == "1":
        tipo = seleccionar_tipo_ingreso()
        for ingreso in ingresos:
            if ingreso["tipo"] == tipo:
                encontrados.append(ingreso)
    else:
        texto = input("Texto a buscar: ").strip().lower()
        for ingreso in ingresos:
            if ingreso["descripcion"].lower().find(texto) != -1:
                encontrados.append(ingreso)

    if len(encontrados) == 0:
        print("No se encontraron ingresos.")
    else:
        for ingreso in encontrados:
            print(f"{ingreso['tipo']} - S/ {ingreso['monto']} - {ingreso['descripcion']}")

    return encontrados


if __name__ == "__main__":
    lista_ingresos = []
    registrar_ingreso(lista_ingresos)
    registrar_ingreso(lista_ingresos)
    consultar_ingresos(lista_ingresos)
    buscar_ingreso(lista_ingresos)
    