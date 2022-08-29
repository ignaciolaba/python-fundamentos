class Usuario: 
    nombre_banco = 'chuchunco bank'
    def __init__(self):
        self.name = 'Michael'
        self.email = 'michael@schumacher.cl'
        self.balance_cuenta = 0

    def hacer_deposito(self, monto):
        self.balance_cuenta += monto
        return self

    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario {self.name}: {self.balance_cuenta}")
        return self



    

Ignacio = Usuario()
Ignacio.name = 'Ignacio'
Victoria = Usuario()
Victoria.name = 'Victoria'
Pedro = Usuario()
Pedro.name = 'Pedro'


Ignacio.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_retiro(350).mostrar_balance_usuario()



Victoria.hacer_deposito(1000).hacer_deposito(200).hacer_retiro(200).hacer_retiro(400).mostrar_balance_usuario()


Pedro.hacer_deposito(1500).hacer_retiro(100).hacer_retiro(50).hacer_retiro(12).mostrar_balance_usuario()
