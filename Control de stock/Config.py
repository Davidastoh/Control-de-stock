# Importamos las librerías necesarias
import sqlite3
from tkinter import *

# Configuración

# Definimos las variables globales
db_name = "stock.db"

# Creamos la conexión con la base de datos
conn = sqlite3.connect(db_name)

# Creamos el cursor
cursor = conn.cursor()

# Creamos la tabla de productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL
)
""")

# Creamos la tabla de proveedores
cursor.execute("""
CREATE TABLE IF NOT EXISTS proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL
)
""")

# Creamos la tabla de ventas
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL
)
""")

# Cerramos la conexión con la base de datos
conn.close()
