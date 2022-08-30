
class MathDojo():
    
    def __init__(self):
        self.resultado = 0
    
    def suma(self, numero, *numeros):
        for x in numeros:
            numero += x
        self.resultado += numero
        # print(self.resultado)
        return self

    def resta(self, numero, *numeros):
        for x in numeros:
            numero += x
        self.resultado -= numero
        return self


Numeros = MathDojo()
# Numeros.resta(1,2,3,4)
# Numeros.resta(10,2,3,4)
# Numeros.resta(1,3,5,0)
# Numeros.suma(1,2,6,4)
# Numeros.suma(1,9,3,8)
# Numeros.suma(9,2,6,4)
# Numeros.suma(1,5,3,7)

x = Numeros.suma(12,68,8).resta(88, 9, 1, 10).resultado
print(x)