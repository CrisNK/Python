class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio # Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
        
    # Getters y setters - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        # print(self.__precio) no se usa comúnmente de esta forma, pero si se puede.
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio
        

restaurant = Restaurant('Pizza Hut', 'Pizzas', 50)
# restaurant.__precio = 80 # No será posible modificarlo con PRIVATE (__)
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('Asere Sushi', 'Comida china', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()