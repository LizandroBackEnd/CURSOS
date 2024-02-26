class Perro:  
    def __init__(self, name, edad): 
        self.__name = name  #atributo privado
        self.edad = edad  
         
    def get_name(self): 
        return self.__name 
     
    def set_name(self, name): #Validación de name 
        self.__name = name
         
    def habla(self): 
        print(f"{self.__name} dice: Guau") 
         
    @classmethod  #factory method
    def factory(cls): 
        return cls("Firulais", 3) 
      
       
perro1 = Perro.factory() 
perro1.habla()