# Polimorfismo
class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio  # Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    # Getters y setters - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        # print(self.precio) no se usa comúnmente de esta forma, pero si se puede.
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        # Utilizando super() se hace referencia a la clase padre, para heredar sus métodos y atributos
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
        
    # Reescribiendo un método (debe llamarse igual a la clase padre para ser sobreescrita)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')
        
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)