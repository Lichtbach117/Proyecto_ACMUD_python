import os
from datetime import date
from inventario import (agregar_producto, modificar_producto, mostrar_productos, buscar_por_codigo, eliminar_producto, buscar_por_categoria)
from persistencia import (cargar_inventario, crear_archivo, guardar_inventario, cargar_ventas, easter_egg)
from validaciones import (ReglaNegocioError, pedir_numero, pedir_opcion, pedir_texto, pedir_si_no)
from ventas import nueva_venta
from reportes import (alertas_stock, cierre_del_dia)

ruta_de_inventario_txt = os.path.join("data", "inventario.txt")
rita_de_ventas_txt = os.path.join("data", "ventas.txt")

CATEGORIAS = ["Lacteos", "Bebidas", "Aseo", "Abarrotes", "Snacks"]

def registrar(inventario):
    """funcion que registra los productos en el txt con ayuda de la funcion agregar_producto de inventario, se piden los
        datos con las funciones de validaciones.py

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error
    """
    codigo = pedir_texto("Código: ").upper()
    if codigo in inventario:
        raise ReglaNegocioError(f"El código {codigo} ya existe.")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_opcion("Categoría:", CATEGORIAS)
    precio = pedir_numero("Precio (COP): ", float)
    stock = pedir_numero("Stock inicial: ", int)
    minimo = pedir_numero("Stock mínimo: ", int)
    proveedor = pedir_texto("Proveedor: ")
    agregar_producto(inventario, codigo, nombre, categoria, precio, stock, minimo, proveedor)
    print("Producto registrado.")

def consultar_codigo(inventario):
    """funcion que con ayuda de funciones de inventario.py, pide el codigo del producto a buscar y devuelve la informacion del mismo,
    si no existe el producto con ese codigo, muestra un mensaje

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos
    """
    producto = buscar_por_codigo(inventario, pedir_texto("Código: ").upper())
    if producto:
        mostrar_productos([producto])
    else:
        print("No existe un producto con ese código.")

def consultar_categoria(inventario):
    """funcion que pide una categoria y busca los productos que pertenecen a ella para mostrarlos en consola

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos
    """
    categoria = pedir_opcion("Categoría:", CATEGORIAS)
    encontrados = buscar_por_categoria(inventario, categoria)
    if encontrados:
        mostrar_productos(encontrados)
    else:
        print("No hay productos en esa categoría.")

def modificar(inventario):
    """funcion que permite cambiar el precio o stock del producto, pide el codigo del producto y lo modifica si existe.
    luego manda la info a inventario.py con la funcion modificar_producto.

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    codigo = pedir_texto("Código: ").upper()
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    if pedir_opcion("¿Qué desea modificar?", ["Precio", "Stock"]) == "Precio":
        modificar_producto(inventario, codigo, precio=pedir_numero("Nuevo precio: ", float))
    else:
        modificar_producto(inventario, codigo, stock=pedir_numero("Nuevo stock: ", int))
    print("Producto actualizado.")

def eliminar(inventario):
    """fucion que permite eliminar un producto del inventario preguntando su codigo y eliminandolo si existe

    Args:
        inventario (diccionario): diccionario con los elementos o datos de los productos.

    Raises:
        ReglaNegocioError: funcion externa que se manda/activa cuando hay un error.
    """
    codigo = pedir_texto("Código: ").upper()
    if codigo not in inventario:
        raise ReglaNegocioError(f"No existe el producto {codigo}.")
    if pedir_si_no(f"¿Eliminar {inventario[codigo]['nombre']}?"):
        eliminar_producto(inventario, codigo)
        print("Producto eliminado.")

def main():
    """funcion principal que se encarga de mostrar la interfaz/menu con las opciones de cada funcion del sistema
    """
    inventario = cargar_inventario(ruta_de_inventario_txt)
    while True:
        print("Bienvenido al sistema de administración de la tiendita de Don Aurelio\n")
        print("#########################################################################")
        print("INGRESE UN NUMERO PARA CONTINUAR")
        print("#########################################################################\n")
        print("1. Registrar producto")
        print("2. Consultar un Producto por su cddigo ")
        print("3. Consultar un Producto por su categoria ")
        print("4. Listar inventario")
        print("5. Modificar precio o stock")
        print("6. Eliminar producto")
        print("7. Nueva venta")
        print("8. Alertas de stock")
        print("9. Cierre del día")
        print("10. Guardar Inventario")
        print("0. salir")

        opcion = input("Eliga la opcion que desea elegir: ").strip()
        try:
            if opcion == "1":
                registrar(inventario)
            elif opcion == "2":
                consultar_codigo(inventario)
            elif opcion == "3":
                consultar_categoria(inventario)
            elif opcion == "4":
                mostrar_productos(list(inventario.values()))
            elif opcion == "5":
                modificar(inventario)
            elif opcion == "6":
                eliminar(inventario)
            elif opcion == "7":
                if nueva_venta(inventario, rita_de_ventas_txt):
                    guardar_inventario(ruta_de_inventario_txt, inventario)
            elif opcion == "8":
                alertas_stock(inventario)
            elif opcion == "9":
                cierre_del_dia(inventario, cargar_ventas(rita_de_ventas_txt),
                               date.today().isoformat())
            elif opcion == "10":
                guardar_inventario(ruta_de_inventario_txt, inventario)
                print("Inventario guardado.")
            elif opcion == "0":
                guardar_inventario(ruta_de_inventario_txt, inventario)
                print("Hasta luego")
                break
            elif opcion == "20251020175":
                easter_egg()
            else:
                print("Opción invalida, porfavor eliga una correcta (0-10).")
        except ReglaNegocioError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()