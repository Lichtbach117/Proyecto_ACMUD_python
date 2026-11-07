from tabulate import tabulate
from validaciones import ReglaNegocioError


def agregar_producto(inventario, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor):
    """agrega un nuevo producto al diccionario del inventario si el codigo no existe y los valores son validos

    Args:
        inventario (diccionario): diccionario del inventario
        codigo (str): codigo del producto
        nombre (str): nombre del producto
        categoria (str): categoria del producto
        precio (float): precio del producto
        stock (int): stock inicial
        stock_minimo (int): stock minimo permitido
        proveedor (str): nombre del proveedor

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    if codigo in inventario:
        raise ReglaNegocioError(f"El código {codigo} ya existe.")
    if precio <= 0 or stock <= 0 or stock_minimo <= 0:
        raise ReglaNegocioError("Precio, stock y stock mínimo deben ser mayores que cero.")
    inventario[codigo] = {"codigo": codigo, "nombre": nombre, "categoria": categoria,
                   "precio": precio, "stock": stock, "stock_minimo": stock_minimo,
                   "proveedor": proveedor}
    
def mostrar_productos(productos):
    """muestra una tabla bonita en consola con la lista de productos que se le pasen

    Args:
        productos (list): lista de diccionarios con la informacion de los productos
    """
    if not productos:
        print("No hay productos para mostrar.")
        return
    filas = [[p["codigo"], p["nombre"], p["categoria"], f"${p['precio']:,.0f}",
              p["stock"], p["stock_minimo"], p["proveedor"]] for p in productos]
    print(tabulate(filas, headers=["Código", "Nombre", "Categoría", "Precio",
                                   "Stock", "Mínimo", "Proveedor"], tablefmt="grid"))

def buscar_por_codigo(inventario, codigo):
    """busca y devuelve el diccionario de un producto usando su codigo en el inventario

    Args:
        inventario (diccionario): diccionario del inventario
        codigo (str): codigo del producto a buscar
    """
    return inventario.get(codigo)

def modificar_producto(inventario, codigo, precio=None, stock=None):
    """actualiza el precio o el stock de un producto existente en el inventario

    Args:
        inventario (diccionario): diccionario del inventario
        codigo (str): codigo del producto a modificar
        precio (float, optional): nuevo precio del producto
        stock (int, optional): nuevo stock del producto
    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error
    """
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    if (precio is not None and precio <= 0) or (stock is not None and stock <= 0):
        raise ReglaNegocioError("Los valores deben ser mayores que cero.")
    if precio is not None:
        inventario[codigo]["precio"] = precio
    if stock is not None:
        inventario[codigo]["stock"] = stock

def eliminar_producto(inventario, codigo):
    """borra un producto del diccionario del inventario usando su codigo

    Args:
        inventario (diccionario): diccionario del inventario
        codigo (str): codigo del producto a eliminar

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    del inventario[codigo]
