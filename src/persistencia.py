def leer_inventario(ruta):
    """
    abre inventario.txt para leer su contenido
    """
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        archivo.close()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def editar_inventario(ruta, info):
    """
    abre inventario.txt para editar su contenido
    """
    try:
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(info)
        archivo.close()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def leer_ventas(ruta):
    """
    abre ventas.txt para leer su contenido
    """
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        archivo.close()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")

def editar_inventario(ruta, info):
    """
    abre ventas.txt para editar su contenido
    """
    try:
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(info)
        archivo.close()
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")