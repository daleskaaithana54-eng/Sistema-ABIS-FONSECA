# Modulo de gestion de gastos

gastos = []


def registrar_gasto():
    print("\n--- REGISTRAR GASTO ---")

    descripcion = input("Ingrese la descripcion del gasto: ").strip()

    if not descripcion:
        print("Error: la descripcion no puede estar vacia.")
        return

    try:
        monto = float(input("Ingrese el monto del gasto: S/ "))

        if monto <= 0:
            print("Error: el monto debe ser mayor que cero.")
            return

    except ValueError:
        print("Error: ingrese un monto numerico valido.")
        return

    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }

    gastos.append(gasto)
    print("Gasto registrado correctamente.")


def consultar_gastos():
    print("\n--- GASTOS REGISTRADOS ---")

    if not gastos:
        print("No hay gastos registrados.")
        return

    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. Descripcion: {gasto['descripcion']}")
        print(f"   Monto: S/ {gasto['monto']:.2f}")

    print(f"Total de gastos: S/ {calcular_total_gastos():.2f}")


def calcular_total_gastos():
    total = 0

    for gasto in gastos:
        total += gasto["monto"]

    return total
def buscar_gasto():
    print("\n--- BUSCAR GASTO ---")

    if not gastos:
        print("No hay gastos registrados.")
        return

    busqueda = input(
        "Ingrese la descripcion que desea buscar: "
    ).strip().lower()

    if not busqueda:
        print("Error: la busqueda no puede estar vacia.")
        return

    encontrados = [
        gasto for gasto in gastos
        if busqueda in gasto["descripcion"].lower()
    ]

    if not encontrados:
        print("No se encontraron gastos con esa descripcion.")
        return

    print("\n--- RESULTADOS DE LA BUSQUEDA ---")

    for i, gasto in enumerate(encontrados, start=1):
        print(f"{i}. Descripcion: {gasto['descripcion']}")
        print(f"   Monto: S/ {gasto['monto']:.2f}")

    total = sum(gasto["monto"] for gasto in encontrados)
    print(f"Total encontrado: S/ {total:.2f}")
def mostrar_resumen_gastos():
    print("\n--- RESUMEN DE GASTOS ---")

    cantidad = len(gastos)

    if cantidad == 0:
        print("No hay gastos registrados para generar el resumen.")
        return

    total = calcular_total_gastos()
    promedio = total / cantidad

    print(f"Cantidad de gastos: {cantidad}")
    print(f"Total acumulado: S/ {total:.2f}")
    print(f"Promedio por gasto: S/ {promedio:.2f}")
def menu_gastos():
    while True:
        print("\n--- MENU DE GASTOS ---")
        print("1. Registrar gasto")
        print("2. Consultar gastos")
        print("3. Calcular total de gastos")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            consultar_gastos()
        elif opcion == "3":
            print(
                f"Total de gastos: S/ "
                f"{calcular_total_gastos():.2f}"
            )
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
     
# ==============================
# PRUEBAS AUTOMATIZADAS DE GASTOS
# ==============================

import unittest
from unittest.mock import patch


class TestModuloGastos(unittest.TestCase):

    def setUp(self):
        gastos.clear()

    @patch("builtins.input", side_effect=["Pasajes", "12.50"])
    def test_registrar_gasto_valido(self, mock_input):
        registrar_gasto()
        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]["descripcion"], "Pasajes")
        self.assertEqual(gastos[0]["monto"], 12.50)

    @patch("builtins.input", side_effect=["", "12.50"])
    def test_rechazar_descripcion_vacia(self, mock_input):
        registrar_gasto()
        self.assertEqual(len(gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "abc"])
    def test_rechazar_monto_no_numerico(self, mock_input):
        registrar_gasto()
        self.assertEqual(len(gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "0"])
    def test_rechazar_monto_cero(self, mock_input):
        registrar_gasto()
        self.assertEqual(len(gastos), 0)

    @patch("builtins.input", side_effect=["Pasajes", "-5"])
    def test_rechazar_monto_negativo(self, mock_input):
        registrar_gasto()
        self.assertEqual(len(gastos), 0)

    def test_calcular_total_gastos(self):
        gastos.extend([
            {"descripcion": "Pasajes", "monto": 12.50},
            {"descripcion": "Materiales", "monto": 7.50}
        ])
        self.assertEqual(calcular_total_gastos(), 20.00)

    def test_total_sin_gastos(self):
        self.assertEqual(calcular_total_gastos(), 0)

    @patch("builtins.input", side_effect=["pas"])
    def test_buscar_gasto_por_coincidencia(self, mock_input):
        gastos.extend([
            {"descripcion": "Pasajes", "monto": 12.50},
            {"descripcion": "Materiales", "monto": 7.50}
        ])

        buscar_gasto()

        self.assertEqual(len(gastos), 2)

    @patch("builtins.input", side_effect=[""])
    def test_buscar_gasto_con_busqueda_vacia(self, mock_input):
        gastos.append({"descripcion": "Pasajes", "monto": 12.50})

        buscar_gasto()

        self.assertEqual(len(gastos), 1)

    @patch("builtins.input", side_effect=["comida"])
    def test_buscar_gasto_sin_coincidencias(self, mock_input):
        gastos.append({"descripcion": "Pasajes", "monto": 12.50})

        buscar_gasto()

        self.assertEqual(len(gastos), 1)
    def test_resumen_con_gastos(self):
        gastos.extend([
            {"descripcion": "Pasajes", "monto": 12.50},
            {"descripcion": "Materiales", "monto": 7.50}
        ])

        with patch("builtins.print") as mock_print:
            mostrar_resumen_gastos()

        mensajes = [
            llamada.args[0]
            for llamada in mock_print.call_args_list
            if llamada.args
        ]

        self.assertIn("Cantidad de gastos: 2", mensajes)
        self.assertIn("Total acumulado: S/ 20.00", mensajes)
        self.assertIn("Promedio por gasto: S/ 10.00", mensajes)

    def test_resumen_sin_gastos(self):
        with patch("builtins.print") as mock_print:
            mostrar_resumen_gastos()

        mensajes = [
            llamada.args[0]
            for llamada in mock_print.call_args_list
            if llamada.args
        ]

        self.assertIn(
            "No hay gastos registrados para generar el resumen.",
            mensajes
        )

if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        unittest.main(argv=[sys.argv[0]])
    else:
        menu_gastos()
