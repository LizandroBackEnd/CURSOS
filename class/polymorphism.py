from abc import ABC, abstractmethod 
 
class Model(ABC): 
    @abstractmethod 
    def save(self): 
        pass 
     
class User(Model): 
    def save(self): 
        print("Saving User") 
         
class Login(Model): 
    def save(self): 
        print("Saving Login") 
 
def save(entitys):  
    for entity in entitys:
        entity.save() 
     
user = User()  
login = Login()
save([login, user])