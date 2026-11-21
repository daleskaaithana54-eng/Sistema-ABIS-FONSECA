def guardar_datos():
    archivo =open("datos.txt","w")
    archivo.write("sistema de mesa de partes")
    archivo.close()
    print("datos guardados correctamente.")

def leer_datos():
    archivo =open("datos.txt","r")
    datos =archivo.read()
    archivo.close()
    print(datos)

def buscar_datos():
    buscar =input("ingrese el dato que desea buscar:")
    archivo =open("datos.txt","r")
    datos =archivo.read()
    archivo.close()
    if buscar in datos:
      print("datos encontrados:")
    else:
     print("datos no encontrados")

def generar_resumen():
    archivo =open("datos.txt","r")
    datos =archivo.red()
    archivo.close()
    print("----RESUMEN----")
    print(datos)

def calcular_estadisticas():
    archivo =open("datos.txt","r")
    datos =archivo.read()
    archivo.close()
    cantidad =len(datos)
    print("cantidad de caracteres:", cantidad)

def mostrar_estadisticas():
    calcular_estadisticas()