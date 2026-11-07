from tabulate import tabulate


def alertas_stock(inventario):
    """Productos con stock <= mínimo, agrupados por proveedor."""
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