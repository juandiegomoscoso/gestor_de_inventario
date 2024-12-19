import sqlite3
from tabulate import tabulate

# Encabezados para mostrar la información del producto
producto_headers = ["ID", "Nombre", "Descripcion", "Cantidad", "Precio", "Categoria"]

def main():
    # Crear la base de datos si no existe
    crear_base_datos()
    while True:
        # Mostrar el menú y obtener la opción del usuario
        opcion = mostrar_menu()
        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            consultar_listado_completo()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            consultar_producto()
        elif opcion == 6:
            reporte_bajo_stock()
        elif opcion == 7:
            break
        else:
            print("Opcion no valida")

def crear_base_datos():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Crear la tabla Producto si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            cantidad INTEGER,
            precio REAL,
            categoria TEXT
        )
    """)
    
    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Base de datos creada con exito.")

def registrar_producto():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Obtener los detalles del producto del usuario
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return
    precio = float(input("Ingrese el precio: "))
    if precio < 0:
        print("El precio no puede ser negativo.")
        return
    categoria = input("Ingrese la categoria: ")

    # Insertar el nuevo producto en la base de datos
    cursor.execute('''INSERT INTO Producto (nombre, descripcion, cantidad, precio, categoria)
                   VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria))

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def consultar_producto():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Obtener el ID del producto del usuario
    producto_id = int(input("Ingrese el ID del producto: "))
    cursor.execute("SELECT * FROM Producto WHERE id = ?", (producto_id,))
    fila = cursor.fetchone()

    # Mostrar los detalles del producto si se encuentra
    if fila:
        print("\nProducto encontrado:")
        print(tabulate([fila], headers=producto_headers, tablefmt="grid"))
    else:
        print(f"\nProducto con ID '{producto_id}' no encontrado.")
    conexion.close()

def actualizar_producto():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Obtener el ID del producto y la nueva cantidad del usuario
    producto_id = int(input("Ingrese el ID del producto: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

    if nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return

    # Actualizar la cantidad del producto en la base de datos
    cursor.execute("UPDATE Producto SET cantidad = ? WHERE id = ?", (nueva_cantidad, producto_id))

    if cursor.rowcount == 0:
        print(f"Producto con ID '{producto_id}' no encontrado.")
    else:
        print(f"Producto con ID '{producto_id}' actualizado exitosamente.")

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def eliminar_producto():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Obtener el ID del producto del usuario
    producto_id = int(input("Ingrese el ID del producto: "))
    cursor.execute("DELETE FROM Producto WHERE id = ?", (producto_id,))

    if cursor.rowcount == 0:
        print(f"\nProducto con ID '{producto_id}' no encontrado.")
    else:
        print(f"\nProducto con ID '{producto_id}' eliminado.")

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def consultar_listado_completo():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Recuperar todos los productos de la base de datos
    cursor.execute("SELECT * FROM Producto")
    tabla = cursor.fetchall()

    # Mostrar la lista de productos
    if tabla:
        print("\nListado completo:")
        print(tabulate(tabla, headers=producto_headers, tablefmt="grid"))
    else:
        print("\nNo hay productos registrados.")

    conexion.close()

def reporte_bajo_stock():
    # Conectar a la base de datos SQLite
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Recuperar productos con bajo stock de la base de datos
    cursor.execute("SELECT * FROM Producto WHERE cantidad < 5")
    tabla = cursor.fetchall()

    # Mostrar la lista de productos con bajo stock
    if tabla:
        print("\nProductos con bajo stock:")
        print(tabulate(tabla, headers=producto_headers, tablefmt="grid"))
    else:
        print("\nNo hay productos con bajo stock.")

    conexion.close()

def mostrar_menu():
    # Mostrar las opciones del menú
    print("""
    MENU:
    1. Registrar producto
    2. Consultar listado productos
    3. Actualizar cantidad de producto
    4. Eliminar producto
    5. Buscar producto
    6. Reporte bajo stock
    7. Salir
    """)

    # Obtener la opción del usuario
    opcion = int(input("Ingrese la opcion: "))
    return opcion

# Ejecutar la función principal
main()
