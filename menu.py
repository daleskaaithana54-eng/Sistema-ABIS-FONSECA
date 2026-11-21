def mostrar_menu():
    print("\n" + "=" * 45)
    print("          SISTEMA DE GESTION")
    print("=" *  45)
    print("1. Gestion de ventas")
    print("2. Gestion de ingresos")
    print("3. Gestion de gastos")
    print("4. Archivos y reportes")
    print("5. Resumen general")
    print("6. Estadistica")
    print("7. Salir")
    print("=" * 45)

def ejecutar_menu():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion:")
        if opcion == "1":
            print("\nGestion de ventas")
            # Lógica para gestionar ventas
        elif opcion == "2":
            print("\nGestion de ingresos")
            # Lógica para gestionar ingresos
        elif opcion == "3":
            print("\nGestion de gastos")
            # Lógica para gestionar gastos
        elif opcion == "4":
            print("\nArchivos y reportes")
            # Lógica para gestionar archivos y reportes
        elif opcion == "5":
            print("\nResumen general")
            # Lógica para mostrar resumen general
        elif opcion == "6":
            print("Estadistica")
            # Lógica para mostrar estadisticas
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no valida. Por favor, intente nuevamente.")
ejecutar_menu()