def conectar_base_datos():
    """
    Esta función conecta con la base de datos.
    """

    global conn
    global cursor

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def desconectar_base_datos():
    """
    Esta función desconecta de la base de datos.
    """

    global conn
    global cursor

    conn.close()
    cursor.close()

def consultar_productos():
    """
    Esta función consulta los productos de la base de datos.
    """

    global conn
    global cursor

    # Conectamos con la base de datos
    conectar_base_datos()

    # Consultamos los productos
    cursor.execute("""
SELECT * FROM productos
""")

    # Obtenemos los resultados
    productos = cursor.fetchall()

    # Desconectamos de la base de datos
    desconectar_base_datos()

    # Devolvemos los resultados
    return productos

def consultar_proveedores():
    """
    Esta función consulta los proveedores de la base de datos.
    """

    global conn
    global cursor

    # Conectamos con la base de datos
    conectar_base_datos()

    # Consultamos los proveedores
    cursor.execute("""
SELECT * FROM proveedores
""")

    # Obtenemos los resultados
    proveedores = cursor.fetchall()

    # Desconectamos de la base de datos
    desconectar_base_datos()

    # Devolvemos los resultados
    return proveedores

def consultar_ventas():
    """
    Esta función consulta las ventas de la base de datos.
    """

    global conn
    global cursor

    # Conectamos con la base de datos
    conectar_base_datos()

    # Consultamos las ventas
    cursor.execute("""
SELECT * FROM ventas
""")

    # Obtenemos los resultados
    ventas = cursor.fetchall()

    # Desconectamos de la base de datos
    desconectar_base_datos()

    # Devolvemos los resultados
    return ventas

def insertar_producto(nombre, cantidad):
    """
    Esta función inserta un producto en la base de datos.
    """

    global conn
    global cursor

    # Conectamos con la base de datos
    conectar_base_datos()

    # Insert
def insertar_producto(nombre, cantidad):
    """
    Esta función inserta un producto en la base de datos.
    """
    global conn
    global cursor
    # Conectamos con la base de datos
    conectar_base_datos()
    # Insertamos el producto en la tabla de productos
    cursor.execute("""
INSERT INTO productos (nombre, cantidad)
VALUES (?, ?)
""", (nombre, cantidad))
    # Guardamos los cambios en la base de datos
    conn.commit()
    # Desconectamos de la base de datos
    desconectar_base_datos()

# # Conectamos con la base de datos
# conectar_base_datos()

# # Insertamos un nuevo producto
# insertar_producto("Martillo", 10)

# # Conectamos con la base de datos
# conectar_base_datos()
# insertar_proveedor("David", 940638884)  

# # Conectamos con la base de datos
# conectar_base_datos()
# insertar_venta(1, 20,"11/10/2023")

# # Desconectamos de la base de datos
# desconectar_base_datos()
