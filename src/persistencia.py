import os
from tabulate import tabulate

def crear_archivo(ruta):
    """Crea el archivo si no existe y añade la primera interaz sin los datos"""

    tabla = tabulate("", headers=["Codigo", "Nombre", "Stock",])

    if not os.path.exists("data"):
        os.makedirs("data")
        
    ruta_completa = os.path.join("data", ruta) if not ruta.startswith("data") else ruta
    if not os.path.exists(ruta_completa):
        try:
            with open(ruta_completa, "w", encoding='utf-8') as archivo:
                archivo.write(tabla)
            print("Se ha creado el archivo")
        except Exception as error:
            print(f"No se pudo crear el archivo: {error}")


def leer_inventario(ruta):
    """
    abre inventario.txt o ventas.txt para leer su contenido
    """

    ruta_completa = os.path.join("data", ruta) if not ruta.startswith("data") else ruta

    if not os.path.exists(ruta_completa):
        print("No existe ninguna archivo")
        while True:
            try:
                desision = int(input("Desea crearlo? 1=si, 2=no:\n"))
                if desision == 1:
                    crear_archivo(ruta)
                    break
                elif desision == 2:
                    print("saliendo...")
                    break
            except ValueError:
                print("ingrese un numero entero 1/2 \n")
    else:
        try:
            archivo = open(ruta_completa, 'r', encoding='utf-8')
            for fila in archivo:
                print(fila)
            print("\n\n")
            archivo.close()
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

def editar_inventario(ruta, info):
    """
    abre inventario.txt para editar su contenido
    """
    if not os.path.exists("data"):
        os.makedirs("data")
    ruta_completa = os.path.join("data", ruta)
    try:
        archivo = open(ruta_completa, 'w', encoding='utf-8')
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