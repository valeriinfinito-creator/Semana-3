from servicios import *
from archivos import *

inventario = []

while True:
    print("MENÚ PRINCIPAL")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        p = buscar_producto(inventario, nombre)
        print(p if p else "Producto no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a actualizar: ")
        nuevo_precio = input("Nuevo precio (enter para dejar igual): ")
        nueva_cantidad = input("Nueva cantidad (enter para dejar igual): ")

        actualizar_producto(
            inventario,
            nombre,
            float(nuevo_precio) if nuevo_precio else None,
            int(nueva_cantidad) if nueva_cantidad else None
        )

    elif opcion == "5":
        nombre = input("Nombre a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == "6":
        calcular_estadisticas(inventario)

    elif opcion == "7":
        ruta = input("Ruta del archivo CSV a guardar: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Ruta del archivo CSV a cargar: ")
        cargado, errores = cargar_csv(ruta)

        if cargado:
            decision = input("¿Sobrescribir inventario? (Si/No): ").upper()

            if decision == "Si":
                inventario = cargado
            else:
                for p in cargado:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)

            print("Carga completada")
            print(f"{errores} filas inválidas omitidas")

    elif opcion == "9":
        print("Saliendo")
        break

    else:
        print("Opción inválida")
