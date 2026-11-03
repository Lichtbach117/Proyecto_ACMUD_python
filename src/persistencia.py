import os
from tabulate import tabulate

ENCAVESADO=["id", "Codigo", "Nombre", "Stock", "Categoria", "Precio"]

def crear_archivo(ruta):
    """Crea el archivo y la carpeta si no existen"""

    if not os.path.exists("data"):
        os.makedirs("data")
        
    ruta_completa = os.path.join("data", ruta) if not ruta.startswith("data") else ruta
    if not os.path.exists(ruta_completa):
        try:
            with open(ruta_completa, "w", encoding='utf-8') as archivo:
                archivo.write("")
            print("Se ha creado el archivo")
        except Exception as error:
            print(f"No se pudo crear el archivo: {error}")

def cargar_inventario(ruta):
    """Devuelve un dict {codigo: producto}, esto devuelve o 
    sirve para mirar la informacoin del archivo si ya existe o no para crearlo
    """
    
    inventario = {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for n, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    campos = linea.split("|")
                    if len(campos) != 7:
                        raise ValueError
                    codigo, nombre, categoria, precio, stock, minimo, proveedor = campos
                    producto = {
                        "codigo": codigo, "nombre": nombre, "categoria": categoria,
                        "precio": float(precio), "stock": int(stock),
                        "stock_minimo": int(minimo), "proveedor": proveedor,
                    }
                    if not codigo or codigo in inventario:
                        raise ValueError
                    if producto["precio"] <= 0 or producto["stock"] < 0 or producto["stock_minimo"] < 0:
                        raise ValueError
                    inventario[codigo] = producto
                except ValueError:
                    print(f"Advertencia: la línea {n} de {ruta} está corrupta y se omite.")
    except FileNotFoundError:
        crear_archivo(ruta)
    return inventario


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
            with open(ruta_completa, 'a', encoding='utf-8') as archivo:
                datos = [[str(info[0]), str(info[1]), str(info[2]), str(info[3]), str(info[4])]]
                tabla = tabulate(datos, tablefmt="plain")
                archivo.write(tabla)
                print(tabla)
                archivo.close()
            print ("Producto agregado correctamente")
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