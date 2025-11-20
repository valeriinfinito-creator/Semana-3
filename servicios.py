def agregar_producto(inventario, nombre, precio, cantidad):
    #Agrega un producto al inventario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print("Producto agregado con éxito")


def mostrar_inventario(inventario):
    #Muestra todos los productos del inventario
    if not inventario:
        print("El inventario está vacío.")
        return

    print("INVENTARIO")
    for p in inventario:
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: {p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        print("----------")


def buscar_producto(inventario, nombre):
    #Busca un producto por nombre y lo retorna
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    #Actualiza precio o cantidad de un producto
    producto = buscar_producto(inventario, nombre)
    if not producto:
        print("Producto no encontrado")
        return

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print("Producto actualizado con éxito")


def eliminar_producto(inventario, nombre):
    #Elimina un producto por nombre
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")


def calcular_estadisticas(inventario):
    #Calcula estadísticas generales del inventario
    if not inventario:
        print("No hay estadísticas: inventario vacío")
        return

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["cantidad"] * p["precio"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("ESTADÍSTICAS")
    print("Unidades totales:", unidades_totales)
    print("Valor total del inventario:", valor_total)
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Mayor stock: {producto_mayor_stock['nombre']} (cantidad {producto_mayor_stock['cantidad']})")
