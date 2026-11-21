gastos =[]

def registrar_gasto():
    descripcion = input("Ingrese la descricion del gasto:")
    monto = float(input("Ingrese el monto:"))

    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente.")


def consultar_gastos():
    print("\n--- GASTOS REGISTRADOS ---")

    for gasto in gastos:
        print("Descripcion:", gasto["descripcion"])
        print("Monto: S/", gasto["monto"])