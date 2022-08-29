class CuentasBancarias: 

    def __init__(self, tasa_de_interes= 0.01 , balance = 0):
        self.name = ''
        self.tasa_de_interes = tasa_de_interes
        self.balance = balance


    def deposito(self, monto):
        self.balance += monto
        return self
    
    def retiro(self, monto):
        self.balance -= monto
        return self

    def mostrar_info_cuenta(self):
        print(f'Usuario: {self.name}, {self.balance}')
        return self

    def generar_interes(self):
        self.balance = self.balance +self.tasa_de_interes
        return self

    
    
Cuenta1 = CuentasBancarias()
Cuenta1.name = 'Cuenta 1'
Cuenta2 = CuentasBancarias()
Cuenta2.name = 'Cuenta 2'

Cuenta1.deposito(100).deposito(300).deposito(100).retiro(500).mostrar_info_cuenta()
Cuenta2.deposito(200).deposito(700).retiro(100).retiro(100).retiro(300).retiro(300).generar_interes().mostrar_info_cuenta()