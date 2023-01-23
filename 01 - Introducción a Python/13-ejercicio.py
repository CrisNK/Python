playlist = {} # Diccionario vacío.
playlist['canciones'] = [] # Lista vacía de canciones

# Funcion principal
def main():
    
    # Agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Ingrese el nombre de la playlist: ')
        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            # Ya tenemos el nombre, desactivamos el ciclo iterativo.
            agregar_playlist = False

            # Mandar a llamar la función para agregar canciones.
            agregar_canciones()
            
            
def agregar_canciones():
    # Bandera para agregar canciones.
    agregar_cancion = True
    
    while agregar_cancion:
        # Preguntar al usuario que canción desea agregar.
        nombre_playlist = playlist['nombre']
        pregunta = f'\nAgrega canciones para la playlist {nombre_playlist}: \n'
        pregunta += 'Escribe "X" para dejar de agregar canciones.\n'
    
        cancion = input(pregunta)
        if cancion == 'X':
            # Dejar de agregar canciones a la playlist.
            agregar_cancion = False
            
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar canciones a la playlist.
            playlist['canciones'].append(cancion)
            
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'\nPlaylist: {nombre_playlist}')
    print('Canciones: ')
    
    for cancion in playlist['canciones']:
        print(f'- {cancion}')
        
main()