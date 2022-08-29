class Usuario: 
    nombre_banco = 'chuchunco bank'
    def __init__(self):
        self.name = 'Michael'
        self.email = 'michael@schumacher.cl'
        self.balance_cuenta = 0

    def hacer_deposito(self, monto):
        self.balance_cuenta += monto

    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto

    def monstrar_balance_usuario(self):
        print(f"Usuario {self.name}: {self.balance_cuenta}")



    

Ignacio = Usuario()
Ignacio.name = 'Ignacio'
Victoria = Usuario()
Victoria.name = 'Victoria'
Pedro = Usuario()
Pedro.name = 'Pedro'


Ignacio.hacer_deposito(100)
Ignacio.hacer_deposito(200)
Ignacio.hacer_deposito(50)
Ignacio.hacer_retiro(350)
Ignacio.monstrar_balance_usuario()

Victoria.hacer_deposito(1000)
Victoria.hacer_deposito(200)
Victoria.hacer_retiro(200)
Victoria.hacer_retiro(400)
Victoria.monstrar_balance_usuario()


Pedro.hacer_deposito(1500)
Pedro.hacer_retiro(100)
Pedro.hacer_retiro(50)
Pedro.hacer_retiro(12)
Pedro.monstrar_balance_usuario()
