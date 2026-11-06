from datetime import date
from tabulate import tabulate
from validaciones import ReglaNegocioError, pedir_texto, pedir_numero, pedir_si_no
from persistencia import registrar_venta

def calcular_descuento(subtotal):
    """Devuelve el porcentaje de descuento según el subtotal."""
    if subtotal >= 100000:
        return 0.10
    if subtotal >= 50000:
        return 0.05
    return 0.0

def agregar_al_carrito(inventario, carrito, codigo, cantidad):
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    if cantidad <= 0:
        raise ReglaNegocioError("La cantidad debe ser mayor que cero.")
    total_pedido = carrito.get(codigo, 0) + cantidad
    if total_pedido > inventario[codigo]["stock"]:
        raise ReglaNegocioError(
            f"Stock insuficiente de {inventario[codigo]['nombre']} (disponible: {inv[codigo]['stock']}).")
    carrito[codigo] = total_pedido

def verificar_pago(pago, total):
    if pago < total:
        raise ReglaNegocioError(f"Pago insuficiente: faltan ${total - pago:,.0f}.")
    return pago - total



def nueva_venta(inventario, ruta_ventas):
    """Flujo completo de una venta. Devuelve True si se confirmó, si se escribe fin, se termina la operacion"""
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

    #mostrar_detalle(inventario, carrito)
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

    for codigo, cantidad in carrito.items():          # confirmar: descontar stock
        inventario[codigo]["stock"] -= cantidad
    registrar_venta(ruta_ventas, date.today().isoformat(), total, carrito)
    print(f"Venta registrada. Cambio: ${cambio:,.0f}")
    return True