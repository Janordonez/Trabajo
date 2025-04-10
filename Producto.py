class Producto:
    lista = []  # Lista general para almacenar todos los productos (no usada directamente en esta clase)

    def __init__(self):
        # Solicita al usuario los datos del producto
        self.nombre = input("Digite el nombre del producto: ")
        self.categoria = input("Digite la categoría: ")

        # Validación del precio (no puede ser negativo)
        while True:
            self.precio = float(input("Digite el precio de su producto: "))
            if self.precio >= 0:
                break
            else:
                print("El precio no puede ser negativo.")

        self.stock = int(input("Digite el stock: "))

    def __repr__(self):
        # Representación en texto del objeto Producto
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}, Valor: {self.stock * self.precio}"

    def agregarStock(self, Cantidad):
        # Suma la cantidad indicada al stock actual
        self.stock += Cantidad
        return print(self)

    def retirarStock(self, Cantidad):
        # Resta stock si hay suficiente disponible
        if (self.stock - Cantidad) < 0:
            print("¡Stock insuficiente!")
            return False
        self.stock -= Cantidad
        return print(self)

    def mostrarInfo(self):
        # Muestra la información del producto
        print(self)