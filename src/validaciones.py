



class ReglaNegocioError(Exception):
    """Se lanza cuando se viola una regla de negocio."""

def pedir_texto(mensaje):
    """Pide un texto que no tenga espacios vacios y que no tenga el simbolo (|) 
    nota_personal: el simbolo es el separador de txt por eso no puede estar al pedir texto
    
    Args:
        mensaje (str): texto que se muestra al usuario para solicitar la entrada
    """
    while True:
        texto = input(mensaje).strip()
        if texto and "|" not in texto:
            return texto
        print("Entrada inválida: no puede estar vacía ni contener '|'.")


def pedir_numero(mensaje, tipo=int):
    """Pide un número; repite hasta que sea válido si pongo algo que no sea numero.

    Args:
        mensaje (str): texto que se muestra al usuario para solicitar el numero
        tipo (type, optional): tipo de dato numerico (int o float)
    """
    while True:
        try:
            valor = tipo(input(mensaje).strip())
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        if valor <= 0:
            print("El valor debe ser mayor que cero.")
            continue
        return valor


def pedir_opcion(mensaje, opciones):
    """Muestra una lista numerada y devuelve la opción elegida.
    nota_personal: recuerda no quitar esto porque se usa al pedir la categoria del producto

    Args:
        mensaje (str): titulo o mensaje inicial a mostrar
        opciones (list): lista de opciones disponibles
    """
    print(mensaje)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    while True:
        n = pedir_numero("Elija el número: ", int)
        if n <= len(opciones):
            return opciones[n - 1]
        print("Esa opción no existe.")

def pedir_si_no(mensaje):
    """Devuelve True si el usuario responde 's'.

    Args:
        mensaje (str): pregunta a realizar al usuario
    """
    while True:
        desicion = input(mensaje + " (s/n): ").strip().lower()
        if desicion in ("s", "n"):
            return desicion == "s"
        print("Responda 's' o 'n'.")
