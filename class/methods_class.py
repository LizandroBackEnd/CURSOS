class Perro:  
    patas = 4
    def __init__(self, name, edad): 
        self.name = name  
        self.edad = edad 
         
    @classmethod #metodo de clase
    def habla(cls): 
        print("Guau") 
         
    @classmethod  #factory method
    def factory(cls): 
        return cls("Firulais", 3) 
      
       
Perro.habla() 
perro1 = Perro("Boby", 5) 
perro2 = Perro("Rex", 7) 
perro3 = Perro.factory() 
print(perro3.edad, perro3.name)