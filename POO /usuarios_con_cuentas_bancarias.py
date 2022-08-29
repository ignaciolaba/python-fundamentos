class Usuarios:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        self.cuenta = CuentasBancarias(0.01 , 0)

    def deposito(self, monto):
        self.cuenta.balance += monto
        return self

    def retiro(self, monto):
        self.cuenta.balance -= monto
        return self
    
    def mostrar_info_cuenta(self):
        print(f'Usuario: {self.name}, {self.cuenta.balance}')
        return self

    def generar_interes(self):
        self.cuenta.balance = self.cuenta.balance +self.cuenta.tasa_de_interes
        return self


class CuentasBancarias: 

    def __init__(self, tasa_de_interes, balance):
        self.tasa_de_interes = tasa_de_interes
        self.balance = balance




    

    
    
Ignacio = Usuarios('Ignacio', 'Labarca')
Pedro = Usuarios('Pedro', 'Silva')

Ignacio.deposito(100).deposito(300).deposito(100).retiro(500).mostrar_info_cuenta()
Pedro.deposito(200).deposito(700).retiro(100).retiro(100).retiro(300).retiro(300).generar_interes().mostrar_info_cuenta()