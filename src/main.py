import persistencia
import inventario


def main(): 
    while True:
        print("Bienvenido al sistema de administración de la tiendita de Don Aurelio\n")
        print("#########################################################################")
        print("INGRESE UN NUMERO PARA CONTINUAR")
        print("#########################################################################\n")
        print("1. Registrar un Producto: ")
        print("2. Consultar un Producto por su código: ")
        print("3. Consultar un Producto por su categoria: ")
        print("4. Modificar un Producto: ")
        print("5. Eliminar un Producto: ")
        print("6. Salir")

        try:
            seleccion = int(input("Ingrese el número de la opción que desea: "))
        except ValueError:
            print("Por favor, ingrese un numero entero")

        if seleccion == 1:
            inventario.registrar_producto()
        elif seleccion == 2:
            inventario.consultar_producto()
        elif seleccion == 3:
            pass
        elif seleccion == 4:
            pass
        elif seleccion == 5:
            pass
        elif seleccion == 6:
            print("Gracias por usar el sistema de administración")
            print("Saliendo....")
            break

if __name__ == "__main__":
    main()