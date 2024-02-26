class Perro:  
    patas = 4
    def __init__(self, name, edad): 
        self.name = name  
        self.edad = edad

    def habla(self):  
        print(f" {self.name} dice: Guau") 



Perro.patas = 3 #Cambia el valor de la propiedad patas           
my_perro = Perro("Firulais", 3)   
my_perro.patas = 5 
my_perro2 = Perro("Chispas", 2) 
print(Perro.patas) 
print(my_perro.patas) 
print(my_perro2.patas)
