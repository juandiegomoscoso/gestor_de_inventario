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


def registrar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    categoria = input("Ingrese la categoria: ")

    cursor.execute('''INSERT INTO Producto (nombre, cantidad, precio, categoria)
                   VALUES (?, ?, ?, ?)''', (nombre, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()