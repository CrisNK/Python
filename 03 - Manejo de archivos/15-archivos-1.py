def main():
    # Crear el archivo.
    archivo = open('archivo.txt', 'w') # w es para escritura, si no existe, lo crea.
    
    # Generar números en el archivo.
    for i in range(0,20):
        archivo.write("Esta es la linea " + str(i) + "\n")
    
    # Cerrar el archivo.
    archivo.close()
    
main()