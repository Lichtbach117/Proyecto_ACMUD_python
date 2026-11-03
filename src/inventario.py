from tabulate import tabulate
from validaciones import ReglaNegocioError


def agregar_producto(inv, codigo, nombre, categoria, precio, stock, stock_minimo, proveedor):
    if codigo in inv:
        raise ReglaNegocioError(f"El código {codigo} ya existe.")
    if precio <= 0 or stock <= 0 or stock_minimo <= 0:
        raise ReglaNegocioError("Precio, stock y stock mínimo deben ser mayores que cero.")
    inv[codigo] = {"codigo": codigo, "nombre": nombre, "categoria": categoria,
                   "precio": precio, "stock": stock, "stock_minimo": stock_minimo,
                   "proveedor": proveedor}
    


def consultar_producto():
    persistencia.leer_inventario(ruta)

def modificar_producto():
    pass

def eliminar_producto():
    pass
