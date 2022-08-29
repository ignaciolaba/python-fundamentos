import Ninja
import Mascota

perro1 = Mascota('charlie', 'perro', 'galletas', 'guau')
Ignacio = Ninja('Ignacio', 'Labarca', 'galleta', 'sabrocan', perro1)

Ignacio.caminar().alimentar().bañar()
print(perro1.energía)
print(perro1.salud)