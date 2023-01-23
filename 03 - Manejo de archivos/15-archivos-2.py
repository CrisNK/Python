def main():
    # Se abre automáticamente en modo de lectura
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())

main()