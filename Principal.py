from Producto import Producto

lista = []

def buscarProducto(Nombre):
    for Producto in lista:
            if Producto.nombre == Nombre:
                return Producto
            else:
                print("Producto no encontrado!")
                return False

def validarEntrada(lista):
    if len(lista) == 0:
            print("No hay producto para agregar Stock!")
            return False
    else: return True
            

while True:
    print("="*20)
    print("1.Registrar Producto")
    print("2.Agregar Stock")
    print("3.Retirar Stock")
    print("4.Mostrar Informacion")
    print("5.Salir")
    print("="*20)
    opc = int(input("Digite una opcion:"))


    match opc:
        case 1:
            p = Producto()
            lista.append(p)
        case 2:
            if not validarEntrada(lista):
                continue
            else:
                Nombre = input("Digite el nombre que desea encontrar:")
                p = buscarProducto(Nombre)
                if not p:
                    continue
                cantidad = int(input("Digite la cantidad que desea sumar:"))
                p.agregarStock(cantidad)
        case 3: 
            if not validarEntrada(lista):
                continue
            else:
                Nombre = input("Digite el nombre que desea encontrar:")
                p = buscarProducto(Nombre)

                cantidad = int(input("Digite la cantidad que desea retirar:"))
                p.retirarStock(cantidad)
        case 4: 
            if not validarEntrada(lista):
                continue
            else:
                Nombre = input("Digite el nombre que desea encontrar:")
                p = buscarProducto(Nombre)

                p.mostrarInfo()
        case 5:
            print("Saliendo del programa")
            break


        

