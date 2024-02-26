class Animal: 
    def comer(self): 
        print("comiendo") 
         
    def dormir(self): 
        print("durmiendo") 
  
#Herencia de la clase Animal
class Perro(Animal): 
    def pasear(self): 
        print("paseando") 

# Herencia de la clase Perro             
class Chanchito(Perro):      
    def programar(self): 
        print("programando") 
         
