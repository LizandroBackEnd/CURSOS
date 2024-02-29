"""Ejemplo sin inyección de dependencias 
import User 
 
def save(): 
    User.save() 
      
Ejemplo con inyección de dependencias 
def save(entity): 
    entity.save() """ 
 
#Ejemplo con un framework 
def init_app(bbdd):  
    #Inicialización de la modulo 
    bbdd.connect()