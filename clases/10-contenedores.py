class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("kayak", 110)
bici = Producto("bici", 11011)
sur = Producto("sur", 1101)
deportes = Categoria("Deportes", [kayak, bici])
deportes.agregar(sur)
deportes.imprimir()
