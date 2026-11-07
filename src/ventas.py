from datetime import date
from tabulate import tabulate
from validaciones import ReglaNegocioError, pedir_texto, pedir_numero, pedir_si_no
from persistencia import registrar_venta

def calcular_descuento(subtotal):
    """calcula y devuelve el porcentaje de descuento aplicable segun el subtotal de la compra

    Args:
        subtotal (float): el valor total acumulado sin descuentos
    """
    if subtotal >= 100000:
        return 0.10
    if subtotal >= 50000:
        return 0.05
    return 0.0

def agregar_al_carrito(inventario, carrito, codigo, cantidad):
    """agrega un producto y su cantidad al carrito de compras validando stock y existencia

    Args:
        inventario (diccionario): diccionario con los datos de los productos
        carrito (diccionario): diccionario que almacena los productos en curso {codigo: cantidad}
        codigo (str): codigo del producto a agregar
        cantidad (int): cantidad de unidades a llevar

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    if cantidad <= 0:
        raise ReglaNegocioError("La cantidad debe ser mayor que cero.")
    total_pedido = carrito.get(codigo, 0) + cantidad
    if total_pedido > inventario[codigo]["stock"]:
        raise ReglaNegocioError(
            f"Stock insuficiente de {inventario[codigo]['nombre']} (disponible: {inventario[codigo]['stock']}).")
    carrito[codigo] = total_pedido

def verificar_pago(pago, total):
    """verifica si el dinero entregado por el cliente cubre el total de la compra y calcula el cambio

    Args:
        pago (float): dinero entregado por el cliente
        total (float): valor total a pagar despues de descuentos

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    if pago < total:
        raise ReglaNegocioError(f"Pago insuficiente: faltan ${total - pago:,.0f}.")
    return pago - total



def nueva_venta(inventario, ruta_ventas):
    """Flujo completo de una venta. Devuelve True si se confirmó, si se escribe fin, se termina la operacion

    Args:
        inventario (diccionario): diccionario con los datos de los productos
        ruta_ventas (str): ruta del archivo de texto donde se registran las ventas
    """
    carrito = {}
    print("Agregue productos. Escriba 'fin' para terminar.")
    while True:
        codigo = pedir_texto("Código del producto: ").upper()
        if codigo == "FIN":
            break
        if codigo not in inventario:
            print("Ese producto no existe.")
            continue
        cantidad = pedir_numero("Cantidad: ", int)
        try:
            agregar_al_carrito(inventario, carrito, codigo, cantidad)
        except ReglaNegocioError as e:
            print(f"Error: {e}")

    if not carrito:
        print("Venta cancelada: el carrito está vacío.")
        return False

    subtotal = sum(inventario[codigo]["precio"] * cantidad for codigo, cantidad in carrito.items())
    porcentaje = calcular_descuento(subtotal)
    descuento = subtotal * porcentaje
    total = subtotal - descuento

    print(f"Subtotal:  ${subtotal:,.0f}")
    print(f"Descuento ({porcentaje:.0%}): ${descuento:,.0f}")
    print(f"TOTAL:     ${total:,.0f}")

    while True:
        pago = pedir_numero("Pago recibido: ", float)
        try:
            cambio = verificar_pago(pago, total)
            break
        except ReglaNegocioError as e:
            print(f"Error: {e}")
            if not pedir_si_no("¿Reintentar el pago?"):
                print("Venta cancelada.")
                return False

    for codigo, cantidad in carrito.items():
        inventario[codigo]["stock"] -= cantidad
    registrar_venta(ruta_ventas, date.today().isoformat(), total, carrito)
    print(f"Venta registrada. Cambio: ${cambio:,.0f}")
    return True