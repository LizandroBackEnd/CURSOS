from abc import ABC, abstractmethod
 
class Model(ABC): 
    @property 
    @abstractmethod
    def table(self): 
        pass
 
    @abstractmethod
    def save(self): 
        pass

    @classmethod    
    def search_id(self, _id): 
        print(f"Searching for id {_id} in the tabble {self.table}")
         
class User(Model): 
    table = "User"  
     
    def save(self): 
        print("Saving User") 
         
user = User() 
User.search_id(1)
     


