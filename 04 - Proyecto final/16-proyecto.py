# Condiciones del programa:
# 1. No es posible crear dos contactos con exactamente el mismo nombre.

# Mis planteamientos de posibles soluciones: 
# 1. Generar una ID única para cada contacto y que el archivo .txt tenga de nombre esa ID.
# 2. Usar una base de datos para almacenar los contactos. (Idea extraida del curso).

import os

CARPETA = '04 - Proyecto final/Contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
def main():
    # Revisa si la carpeta existe o no.
    crear_directorio()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    
    while preguntar:
        os.system('clear') # Limpia la terminal en Linux/Mac.
        # os.system('cls') # Limpia la terminal en Windows.

        # Muestra el menú de opciones y retorna la opción seleccionada.
        opcion = menu()

        if opcion == 1:
            os.system('clear')
            agregar_contacto()
        elif opcion == 2:
            os.system('clear')
            mostrar_contactos()
        elif opcion == 3:
            os.system('clear')
            actualizar_contacto()
        elif opcion == 4:
            os.system('clear')
            # eliminar_contacto()
        elif opcion == 5:
            os.system('clear')
            # buscar_contacto()
        elif opcion == 6:
            os.system('clear')
            print('*----------------------------------*\n'
                  '|           Hasta pronto!          |\n'
                  '*----------------------------------*')
            preguntar = False
        else:
            print('La opcion ingresada no es válida. Inténtelo nuevamente.')
            input()
# Funciones principales
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)
def menu():
    print('*----------------------------------*\n'
          '|             Contactos            |\n'
          '*----------------------------------*\n'
          '| 1) Agregar contacto              |\n'
          '| 2) Mostrar contactos             |\n'
          '| 3) Actualizar contacto           |\n'
          '| 4) Eliminar contacto             |\n'
          '| 5) Buscar contacto               |\n'
          '| 6) Finalizar programa            |\n'
          '*----------------------------------*')
    opcion = input(' Seleccione una opcion: ')
    opcion = int(opcion)
    return opcion
# Funciones CRUD
def agregar_contacto():
    print('*----------------------------------*\n'
          '|         Agregar contacto         |\n'
          '*----------------------------------*')
    nombre_contacto = input(' Nombre: ')
    
    # Revisar si el archivo ya existe antes de crearlo.
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    
    # Si no existe el archivo se continúa con el código.
    if not existe:    
        # Se crea una carpeta con el nombre del contacto ingresado por teclado.
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Rellenar los campos restantes.
            telefono_contacto = input(' Teléfono: ')
            categoria_contacto = input(' Categoría: ')

            # Instanciar la clase.
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir datos guardados en el archivo de texto.
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\n')
            archivo.write('Categoría: ' + contacto.categoria + '\n')

        # Mostrar mensaje de éxito.
        print('*----------------------------------*\n'
              '|  Contacto agregado exitosamente  |\n'
              '*----------------------------------*')
        input('Presione una tecla para continuar...')
    else:
        print('*----------------------------------*\n'
              '|   ERROR: El contacto ya existe   |\n'
              '*----------------------------------*')
        input('Presione una tecla para continuar...')
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contactos:
            for contacto in contactos:
                # Muestra los datos de los contactos.
                print(contacto.rstrip())
            print()
    input('Presione una tecla para volver al menú principal...')
def actualizar_contacto():
    
# def eliminar_contacto():

# def buscar_contacto():

main()
