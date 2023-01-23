class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio  # Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    # Getters y setters - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        # print(self.__precio) no se usa comúnmente de esta forma, pero si se puede.
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre,categoria,precio) # Utilizando super() se hace referencia a la clase padre, para heredar sus métodos y atributos

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()