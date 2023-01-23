# Revisar si una condición es mayor a
balance = 500

if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')
    
# Likes
likes = 200
if likes >= 200:
    print('Excelente, 200 likes')
else:
    print('Casi llegas a los 200')
    
# If con texto
lenguaje = 'PHP'
if not lenguaje == 'Python': # Se puede usar if not ó en la condicional colocar '!='
    print('Excelente decisión')

# Evaluar un boolean
usuario_autenticado = True

if usuario_autenticado: # No es necesario comparar los booleanos, Python lo hace compara automáticamente si la condición es verdadera.
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')
    
# Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP']
if 'PHP' in lenguajes:
    print('PHP si está en la lista')
else:
    print('No está en la lista')
    
# If anidados
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    if usuario_admin:
        print('Acceso total')
    else:
        print('Acceso al sistema')
else:
    print('Acceso denegado')