# Proyecto_ACMUD_python

# Notas aclaratorias:
- los Docstrings los uso por constumbre de mi profesor de programación que me los pedia, ¡NO SON HECHOS POR IA!, ademas uso una extensión que ayuda a eso, llamada "autoDocstring - Python Docstring Generator"
- por la misma razón, coloco el .gitignore para no enviar la carpeta .venv
- A pesar de que esto es el proyecto final me gustaria preguntar y pedir revision de nota por uso de IA en el trabajo 2, no se porque se me marco con IA, razon por la cual coloco la primera aclaración.

# Descripción del Proyecto:
Sistema de administración y gestión para la tiendita de "Don Aurelio". Permite llevar el control completo de inventarios, registro de ventas con descuentos automáticos por subtotal, validaciones robustas, control de stock mínimo con alertas por proveedor, y reportes de cierre del día. Todo respaldado mediante persistencia en archivos de texto (`data/inventario.txt` y `data/ventas.txt`). El proyecto lo decidi hacer sin clases (programacion orientada a objetos), por tema de simplicidad y para poder entender mejor el funcionamiento de las funcionalidades.

# Instalacion:
1. tal y como se pidio en el proyecto, el sistema requiere de la biblioteca tabulate, su instalación se hace con:
- python -m venv .venv
- source .venv\Scripts\activate o source .venv/bin/activate.fish en mi caso (linux)
- pip install -r requirements.txt
- python src/main.py

# Estructura del Proyecto:
- `src/main.py`: Menú principal e interfaz de usuario en consola.
- `src/inventario.py`: Lógica para agregar, buscar, modificar y eliminar productos.
- `src/ventas.py`: Gestión del carrito de compras, cálculo de descuentos y validación de pagos.
- `src/persistencia.py`: Manejo de archivos de texto para guardar y cargar inventarios y ventas.
- `src/reportes.py`: Generación de alertas de stock y estadísticas para el cierre del día.
- `src/validaciones.py`: Funciones auxiliares para validar entradas del usuario y reglas de negocio.

# Ejecución:
- Requerimientos:
1. Al ejecutar es necesario activar el entorno virtual venv, seguido a eso hay dos formas de ejectuar el proyecto, oprimiendo f5 en el teclado o colocando en terminal "python src/main.py"

# Observación:
1. durante la ejecucion del proyecto, al agregar uno o varios productos, los cambios no se veran reflejados automaticamente en el inventario.txt, para verlos se devera seleccionar la opcion 10 de guardar inventario o la opcion 0 para salir ya que estos se guardan automaticamente.
2. Teniendo en cuenta la observación anterior, durante la ejecucion si en la terminal se oprime la combinacion de teclas "ctrl + c", el programa se interrumpira y se perderan los cambios realizados hasta ese momento, por lo que porfavor evitar hacer esto si ya realizaron alguna funcion y no guardaron los cambio con la opción 10 previamente. 