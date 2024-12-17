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


def consultar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    producto = input("Ingrese el nombre del producto: ")
    cursor.execute("SELECT * FROM Producto WHERE nombre = ?", (producto,))
    tabla = cursor.fetchall()

    for fila in tabla:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Cantidad: {fila[2]}, Precio: {fila[3]}, Categoria: {fila[4]}")

    conexion.close()


def actualizar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    id = int(input("Ingrese el ID del producto: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    cursor.execute("UPDATE Producto SET cantidad = ? WHERE id = ?", (nueva_cantidad, id))

    conexion.commit()
    conexion.close()


