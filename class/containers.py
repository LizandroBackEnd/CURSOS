class Producto:
    def __init__(self, name, price): 
        self.name = name
        self.price = price 
         
    def __str__(self): 
        return f"Producto: {self.name} - Precio: {self.price}" 
     
       
class Categoria: 
    productos = [] 
     
    def __init__(self, name, products): 
        self.name = name 
        self.products = products 
         
    def add(self, product): 
        self.products.append(product)  
         
    def print(self): 
        for product in self.products: 
            print(product) 
             
kayak = Producto("Kayak", 275) 
paddle = Producto("Paddle", 20) 
lifejacket = Producto("Lifejacket", 40) 
deportes = Categoria("Deportes", [kayak, paddle]) 
deportes.add(lifejacket) 
deportes.print()
         
          