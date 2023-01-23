# Reto 1: Crear una función que imprima un mensaje de bienvenida.
# Reto 2: Crear una función que tome un nombre de un usuario y lo muestre como mensaje de bienvenida.
# Reto 3: Craer una fucnión que tome la última actividad que hiciste.

# Reto 1:
def mensaje_bienvenida():
    print('Bienvenido Cristóbal')
    
mensaje_bienvenida()

# Reto 2:
def mensaje_bienvenida2(nombre):
    print(f'Bienvenido a Python {nombre}')

mensaje_bienvenida2('Cristóbal')

# Reto 3:
def ultima_actividad(actividad):
    print(f'La ultima actividad que hiciste fue {actividad.upper()} en Python')
    
ultima_actividad('programar')