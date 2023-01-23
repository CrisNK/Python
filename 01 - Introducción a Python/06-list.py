lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

print(lenguajes[1])

# Ordenar los elementos alfabéticamente
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Actualizar un elemento de una list (arreglo)
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar elementos a una list (arreglo)
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar elementos de una list (arreglo)
del lenguajes[1]
print(lenguajes)

# Eliminar el último elemento de una list (arreglo)
lenguajes.pop()
print(lenguajes)

# Eliminar un elemento específico de una list (arreglo) con pop
lenguajes.pop(0)
print(lenguajes)

# Eliminar un elemento específico mediante su nombre
lenguajes.remove('PHP')
print(lenguajes)