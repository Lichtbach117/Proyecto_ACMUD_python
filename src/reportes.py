from tabulate import tabulate
from collections import Counter
"""me recomendaron usar counter para facilitarme la sumas de las unidades en el codigo"""


def alertas_stock(inventario):
    """funcion que muestra los productos cuyo stock actual es menor o igual al minimo permitido, agrupandolos por proveedor

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos
    """
    proveedores = {}
    for productos in inventario.values():
        if productos["stock"] <= productos["stock_minimo"]:
            proveedores.setdefault(productos["proveedor"], []).append(productos)

    if not proveedores:
        print("No hay productos con stock bajo.")
        return
    for proveedores, productos in sorted(proveedores.items()):
        print(f"\nProveedor: {proveedores}")
        filas = [[producto["codigo"], producto["nombre"], producto["stock"], producto["stock_minimo"],
                  "AGOTADO" if producto["stock"] == 0 else "Stock bajo"] for producto in productos]
        print(tabulate(filas, headers=["Código", "Nombre", "Stock", "Mínimo", "Estado"],
                       tablefmt="grid"))

def cierre_del_dia(inventario, ventas, fecha):
    """funcion que genera un reporte resumido del cierre del dia incluyendo total vendido, numero de ventas, ticket promedio, producto mas vendido y categorias con movimiento

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos
        ventas (lista): lista con el historico de ventas
        fecha (str): fecha en formato ISO para filtrar el cierre
    """
    ventas_del_dia = [venta for venta in ventas if venta["fecha"] == fecha]
    total = sum(venta["total"] for venta in ventas_del_dia)
    numero_ventas = len(ventas_del_dia)
    promedio = total / numero_ventas if numero_ventas else 0

    unidades = Counter()
    for venta in ventas_del_dia:
        unidades.update(venta["items"])

    if unidades:
        codigo_top = unidades.most_common(1)[0][0]
        nombre = inventario[codigo_top]["nombre"] if codigo_top in inventario else codigo_top
        mas_vendido = f"{nombre} ({unidades[codigo_top]} unidades)"
    else:
        mas_vendido = "N/A"

    sin_ventas = [producto["nombre"] for codigo, producto in inventario.items() if codigo not in unidades]
    categorias = sorted({inventario[codigo]["categoria"] for codigo in unidades if codigo in inventario})

    print(f"\n=== Cierre del día {fecha} ===")
    print(tabulate([
        ["Total vendido", f"${total:,.0f}"],
        ["Número de ventas", numero_ventas],
        ["Ticket promedio", f"${promedio:,.0f}"],
        ["Producto más vendido", mas_vendido],
        ["Categorías con movimiento", ", ".join(categorias) or "Ninguna"],
        ["Productos sin ventas", ", ".join(sin_ventas) or "Ninguno"],
    ], tablefmt="grid"))