# Al crear una clase, la idea es que la primera letra sea mayúscula.
class Restaurant:
    # Siempre se le debe entregar como parámetro "self" a los métodos de la clase.
    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo del método.
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        
# Las clases son como las funciones, las declaras y luegos las mandas a llamar, eso se llama:
# "Instanciar una clase"
restaurant = Restaurant()

# Mandar a llamar el método (función) una vez creada y llamada la clase.
# El self no se vuelve a entregar como argumento al llamar el método, se entrega automáticamente, hacerlo es entregarle dos veces el self,
# lo que termina dando error.
restaurant.agregar_restaurant('Pizza Hut')
restaurant.mostrar_informacion()

# Creación de otro objeto con la misma clase.
restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Papa John\'s')
restaurant2.mostrar_informacion()

# Otra forma de mostrar una información de una clase
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')