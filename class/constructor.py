class Perro: 
    def __init__(self, name, edad): 
        self.name = name  
        self.edad = edad

    def habla(self):  
        print(f" {self.name} dice: Guau") 



             
my_perro = Perro("Firulais", 3) 
my_perro.habla()
