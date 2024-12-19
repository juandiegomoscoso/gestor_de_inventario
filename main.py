import sqlite3

def main():
    crear_base_datos()
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            consultar_producto()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            consultar_listado_completo()
        elif opcion == 6:
            reporte_bajo_stock()
        elif opcion == 7:
            break
        else:
            print("Opcion no valida")



def crear_base_datos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            cantidad INTEGER,
            precio REAL,
            categoria TEXT
        )
    """)
    
    conexion.commit()
    conexion.close()
    print("Base de datos creada con exito.")



def registrar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return
    precio = float(input("Ingrese el precio: "))
    if precio < 0:
        print("El precio no puede ser negativo.")
        return
    categoria = input("Ingrese la categoria: ")

    cursor.execute('''INSERT INTO Producto (nombre, cantidad, precio, categoria)
                   VALUES (?, ?, ?, ?)''', (nombre, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()



def consultar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    producto_id = int(input("Ingrese el ID del producto: "))
    cursor.execute("SELECT * FROM Producto WHERE id = ?", (producto_id,))
    fila = cursor.fetchone()

    if fila:
        print("\nProducto encontrado:")
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Cantidad: {fila[2]}, Precio: {fila[3]}, Categoria: {fila[4]}")
    else:
        print(f"\nProducto con ID '{producto_id}' no encontrado.")
    conexion.close()



def actualizar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del producto: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

    if nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return

    cursor.execute("UPDATE Producto SET cantidad = ? WHERE nombre = ?", (nueva_cantidad, nombre))

    if cursor.rowcount == 0:
        print(f"Producto '{nombre}' no encontrado.")

    conexion.commit()
    conexion.close()



def eliminar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del producto: ")
    cursor.execute("DELETE FROM Producto WHERE nombre = ?", (nombre,))

    if cursor.rowcount:
        print(f"\nProducto '{nombre}' no encontrado.")
    else:
        print(f"\nProducto '{nombre}' eliminado.")
        

    conexion.commit()
    conexion.close()



def consultar_listado_completo():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Producto")
    tabla = cursor.fetchall()

    if tabla:
        print("\nListado completo:")
        for fila in tabla:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Cantidad: {fila[2]}, Precio: {fila[3]}, Categoria: {fila[4]}")
    else:
        print("\nNo hay productos registrados.")

    conexion.close()



def reporte_bajo_stock():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Producto WHERE cantidad < 5")
    tabla = cursor.fetchall()

    if tabla:
        print("\nProductos con bajo stock:")
        for fila in tabla:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Cantidad: {fila[2]}, Precio: {fila[3]}, Categoria: {fila[4]}")
    else:
        print("\nNo hay productos con bajo stock.")

    conexion.close()



def mostrar_menu():
    print("""
    MENU:
    1. Registrar producto
    2. Consultar producto
    3. Actualizar producto
    4. Eliminar producto
    5. Consultar listado completo
    6. Reporte bajo stock
    7. Salir
    """)

    opcion = int(input("Ingrese la opcion: "))
    return opcion


main()