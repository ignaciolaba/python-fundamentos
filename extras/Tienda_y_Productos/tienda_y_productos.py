from tienda import Tienda
from producto import Producto

Machucao = Tienda('Machucao')
Machucao.lista = ['Arroz', 'Lentejas', 'Lasaña', 'Apio']

Berenjena = Producto('Berenjena', 10000 , 'verdura')
Alcachofa = Producto('Alcachofa', 5000, 'verdura')


Machucao.agregar_producto(Berenjena.nombre)
Berenjena.actualizar_precio(0.1, False)
print(Berenjena.precio)
Berenjena.inflación(0.072)
print(Berenjena.precio)
Berenjena.hacer_liquidacion('verdura', 0.25)
print(Berenjena.precio)
Machucao.vender_producto(Berenjena.nombre)

