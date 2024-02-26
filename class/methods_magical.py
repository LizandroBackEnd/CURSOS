class Perro: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age   
         
    def __del__(self): 
        print(f"Adios perro 😔 {self.name}")
         
    def __str__(self): 
        return f"Clase Perro: {self.name}"
         
    def habla(self): 
        print(f'{self.name} dice guau') 
         

perro = Perro('Firulais', 5)    
del Perro # Eliminamos la clase Perro