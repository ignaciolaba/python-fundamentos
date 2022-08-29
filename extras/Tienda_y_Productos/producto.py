

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
        print(self.nombre, self.categoria, self.precio)

    def inflación(self, procentaje_aumento):
        self.precio = self.precio * (1 + procentaje_aumento ) 

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        if (categoria == self.categoria):
            self.precio = self.precio * (1 - porcentaje_descuento) 

Alcachofa = Producto('Alcachofa', 1000, 'verdura')

