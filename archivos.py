import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    #Guarda el inventario en un archivo CSV.

    if not inventario:
        print("No se puede guardar: el inventario está vacío")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar el archivo:", e)


def cargar_csv(ruta):
    #Carga un archivo CSV y retorna una lista de productos válidos
    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Archivo CSV inválido: encabezado incorrecto")
                return [], 0

            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    filas_invalidas += 1

        return inventario_cargado, filas_invalidas

    except FileNotFoundError:
        print("Archivo no encontrado")
        return [], 0
    except Exception as e:
        print("Error al cargar el archivo:", e)
        return [], 0
