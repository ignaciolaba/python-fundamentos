
class Mascota: 
    
    def __init__(self, name, tipo, golosinas, sonido):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 500
        self.energía = 200
        self.sonido = sonido
    
    def dormir(self):
        self.energía += 25
        return self
    
    def comer(self):
        self.energía += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        return self

    def ruido(self):
        print(self.sonido)
