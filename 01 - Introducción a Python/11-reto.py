# Realiza un exámen con 3 preguntas que tu desees, el usuario deberá responder 'si' o 'no' y al final otorgarle una calificación
# (la calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)

print('Examen')
puntos = 0

pregunta1 = input('¿Un número escrito por el usuario por teclado puede ser usado directamente para una comparación en un if?\n')
if pregunta1 == 'si':
    puntos+=1

pregunta2 = input('El tipo de escritura principal en Python en la escritura de variables es CamelCase\n')
if pregunta2 == 'no':
    puntos+=1
    
pregunta3 = input('Sólamente se puede programar con Python en Windows\n')
if pregunta3 == 'no':
    puntos += 1

if puntos == 3:
    print('Excelente trabajo!, tuviste el máximo puntaje, felicitaciones!!')
elif puntos < 3 and puntos > 0:
    print('Tuviste algunos errores, sigue intentándolo!!')
else:
    print('Deberías estudiar más para la próxima, suerte!!')