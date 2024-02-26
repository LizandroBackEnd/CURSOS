class Ave:  
    def __init__(self): 
        self.volador = True 

    def vuela(self):
        print('Volando voy') 
         
class Pato(Ave): 
    def __init__(self): 
        super().__init__() 
        self.nada = True 
         
   
   
         
          
pato = Pato() 
pato.vuela() 
print(pato.volador, pato.nada)