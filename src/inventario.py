import persistencia

"""ruta consultar"""
ruta = "inventario.txt"

def registrar_producto():
    print("#################################################")
    print("INGRESE LOS DATOS DEL PRODUCTO")
    print("#################################################\n")
    datos1 = int(input("Ingrese el codigo del producto: "))
    datos2 = str(input("Ingrese el nombre del producto: "))
    datos3 = int(input("Ingrese el stock del producto: "))
    datos4 = str(input("Ingrese la categoria del producto: "))
    datos5 = int(input("Ingrese el precio del producto:"))
    info = (datos1, datos2, datos3, datos4, datos5)

    persistencia.editar_inventario(ruta, info)
    


def consultar_producto():
    persistencia.leer_inventario(ruta)

def modificar_producto():
    pass

def eliminar_producto():
    pass
