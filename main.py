import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Producto (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   cantidad INTEGER,
                   precio REAL,
                   categoria TEXT
                   )""")
    
    conexion.commit()
    conexion.close()