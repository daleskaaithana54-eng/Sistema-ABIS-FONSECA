def leer_archivo(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    return lineas


def guardar_linea(nombre, texto):
    archivo = open(nombre, "a", encoding="utf-8")
    archivo.write(texto + "\n")
    archivo.close()

