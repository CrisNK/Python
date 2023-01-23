nombre = input('Cuál es tu nombre: \r\n') # No entiendo por qué le agregar el \r, creo que es innnecesario

print(f'Hola {nombre}')

edad = input('Cuál es tu edad: ')
# Convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('No puedes votar')
    
# Mezclarlo con operadores
numero = input('Agrega un número y te diré si es par o no: ')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')