
# LEER ARCHIVO
def leer_archivo(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    return lineas


# GUARDAR LINEA
def guardar_linea(ruta, texto):
    archivo = open(ruta, "a", encoding="utf-8")
    archivo.write(texto + "\n")
    archivo.close()

# GUARDAR ARCHIVO COMPLETO
def guardar_archivo(ruta, lineas):
    archivo = open(ruta, "w", encoding="utf-8")

    for linea in lineas:
        archivo.write(linea + "\n")

    archivo.close()
    