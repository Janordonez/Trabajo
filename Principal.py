# ---------------------------------------------------------------
# Nombre del archivo : inventario.py
# Autor             : Joshua Ordoñez
# Fecha             : 09/04/2025
# Versión           : 1.0
# Descripción       : Sistema de inventario básico para registrar productos,
#                     agregar y retirar stock, y mostrar información de productos.
# ---------------------------------------------------------------

from Producto import Producto

lista = []  # Lista para almacenar objetos de tipo Producto

# Función para buscar un producto por nombre
def buscarProducto(Nombre):
    for Producto in lista:
        if Producto.nombre == Nombre:
            return Producto
    print("Producto no encontrado!")
    return False

# Función para validar si la lista contiene productos
def validarEntrada(lista):
    if len(lista) == 0:
        print("No hay producto para agregar Stock!")
        return False
    else:
        return True

# Menú principal
while True:
    print("="*20)
    print("1. Registrar Producto")
    print("2. Agregar Stock")
    print("3. Retirar Stock")
    print("4. Mostrar Información")
    print("5. Salir")
    print("="*20)
    
    try:
        opc = int(input("Digite una opción: "))
    except ValueError:
        print("Por favor, digite un número válido.")
        continue

    match opc:
        case 1:
            # Registrar nuevo producto
            p = Producto()
            lista.append(p)

        case 2:
            # Agregar stock a un producto existente
            if not validarEntrada(lista):
                continue
            Nombre = input("Digite el nombre que desea encontrar: ")
            p = buscarProducto(Nombre)
            if not p:
                continue
            cantidad = int(input("Digite la cantidad que desea sumar: "))
            p.agregarStock(cantidad)

        case 3:
            # Retirar stock de un producto existente
            if not validarEntrada(lista):
                continue
            Nombre = input("Digite el nombre que desea encontrar: ")
            p = buscarProducto(Nombre)
            if not p:
                continue
            cantidad = int(input("Digite la cantidad que desea retirar: "))
            p.retirarStock(cantidad)

        case 4:
            # Mostrar información de un producto
            if not validarEntrada(lista):
                continue
            Nombre = input("Digite el nombre que desea encontrar: ")
            p = buscarProducto(Nombre)
            if p:
                p.mostrarInfo()

        case 5:
            # Salir del programa
            print("Saliendo del programa")
            break

        case _:
            print("Opción no válida. Intente nuevamente.")
