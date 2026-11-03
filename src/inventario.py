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
    
def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    filas = [[p["codigo"], p["nombre"], p["categoria"], f"${p['precio']:,.0f}",
              p["stock"], p["stock_minimo"], p["proveedor"]] for p in productos]
    print(tabulate(filas, headers=["Código", "Nombre", "Categoría", "Precio",
                                   "Stock", "Mínimo", "Proveedor"], tablefmt="grid"))

def buscar_por_codigo(inventario, codigo):
    return inventario.get(codigo)

def modificar_producto():
    pass

def eliminar_producto():
    pass
