import persistencia
import os
from inventario import (agregar_producto, modificar_producto, mostrar_productos)
from persistencia import (cargar_inventario, crear_archivo, guardar_inventario)
from validaciones import (ReglaNegocioError, pedir_numero, pedir_opcion, pedir_texto)

ruta_de_inventario_txt = os.path.join("data", "inventario.txt")
rita_de_ventas_txt = os.path.join("data", "ventas")

CATEGORIAS = ["Lacteos", "Bebidas", "Aseo", "Abarrotes", "Snacks"]

def registrar(inv):
    codigo = pedir_texto("Código: ").upper()
    if codigo in inv:
        raise ReglaNegocioError(f"El código {codigo} ya existe.")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_opcion("Categoría:", CATEGORIAS)
    precio = pedir_numero("Precio (COP): ", float)
    stock = pedir_numero("Stock inicial: ", int)
    minimo = pedir_numero("Stock mínimo: ", int)
    proveedor = pedir_texto("Proveedor: ")
    agregar_producto(inv, codigo, nombre, categoria, precio, stock, minimo, proveedor)
    print("Producto registrado.")

def main():
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
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                pass
            elif opcion == "8":
                pass
            elif opcion == "9":
                pass
            elif opcion == "10":
                guardar_inventario(ruta_de_inventario_txt, inventario)
                print("Inventario guardado.")
            elif opcion == "0":
                guardar_inventario(ruta_de_inventario_txt, inventario)
                print("Hasta luego")
                break
            else:
                print("Opción invalida, porfis eliga una correcta (0-10).")
        except ReglaNegocioError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()