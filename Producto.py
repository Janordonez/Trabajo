class Producto:
    lista = []
    def __init__(self):
        self.nombre = input("Digite el nombre del producto:")
        self.categoria = input("Digite la categoria: ")
        self.precio = float(input("Digite el precio de su producto:"))
        self.stock = int(input("Digite el stock: "))
        Producto.lista.append(self)
        
    def __repr__(self):
        return f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}, Valor: {self.stock * self.precio}"
    
    def agregarStock(self, Cantidad):
            self.stock += Cantidad
            return print(self)
    def retirarStock(self, Cantidad):
        if (self.stock - Cantidad) < 0:
             print("Stock insuficiente!")
             return False
        self.stock -= Cantidad
        return print(self)

    def mostrarInfo(self):
        print(self)
    

    
    
