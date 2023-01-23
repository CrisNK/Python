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

    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True

    while preguntar:
        opcion = input(' Seleccione una opcion: ')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            # mostrar_contactos()
            preguntar = False
        elif opcion == 3:
            # actualizar_contacto()
            preguntar = False
        elif opcion == 4:
            # eliminar_contacto()
            preguntar = False
        elif opcion == 5:
            # buscar_contacto()
            preguntar = False
        else:
            print('La opcion ingresada no es válida. Inténtelo nuevamente.')
# Funciones principales
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)
def mostrar_menu():
    print('*----------------------------------*\n'
          '|             Contactos            |\n'
          '*----------------------------------*\n'
          '| 1) Agregar contacto              |\n'
          '| 2) Mostrar contactos             |\n'
          '| 3) Actualizar contacto           |\n'
          '| 4) Eliminar contacto             |\n'
          '| 5) Buscar contacto               |\n'
          '*----------------------------------*')
# Funciones CRUD
def agregar_contacto():
    print('*----------------------------------*\n'
          '|         Agregar contacto         |\n'
          '*----------------------------------*')
    nombre_contacto = input(' Nombre: ')

    with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
        # Resto de los campos.
        telefono_contacto = input(' Teléfono: ')
        categoria_contacto = input(' Categoría: ')

        # Instanciar la clase.
        contacto = Contacto(
            nombre_contacto, telefono_contacto, categoria_contacto)

        # Escribir datos guardados en el archivo de texto.
        archivo.write('Nombre: ' + contacto.nombre + '\n')
        archivo.write('Teléfono: ' + contacto.telefono + '\n')
        archivo.write('Categoría: ' + contacto.categoria + '\n')

    # Mostrar mensaje de éxito
    print('*----------------------------------*\n'
          '|  Contacto agregado exitosamente  |\n'
          '*----------------------------------*')
# def mostrar_contactos():

# def actualizar_contacto():

# def eliminar_contacto():

# def buscar_contacto():

main()
