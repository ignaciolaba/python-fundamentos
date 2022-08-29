from producto import Producto

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def agregar_producto(self, nuevo_producto):
        self.lista.append(nuevo_producto)
        print(self.lista) 

    def vender_producto(self, producto):
        self.lista.remove(producto) 
        print(self.lista) 

