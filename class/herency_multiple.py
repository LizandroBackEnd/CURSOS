class Animal: 
    def comer(self): 
        print("comiendo") 
         
    def dormir(self): 
        print("durmiendo") 
  

class Perro: 
    def pasear(self): 
        print("paseando") 

# Herencia multiple de la clase Perro y Animal          
class Chanchito(Perro, Animal):      
    def programar(self): 
        print("programando") 
         
