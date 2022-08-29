from typing_extensions import Self


class Producto: 
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if (esta_elevado == True):
            self.precio = self.precio * (1+cambio_porcentaje)
        if(esta_elevado == False):
            self.precio = self.precio *  (1-cambio_porcentaje)
    
    def print_info(self):
        print(self)

Alcachofa = Producto('alcachofa', 1000, 'fruta')

Print_info(self)