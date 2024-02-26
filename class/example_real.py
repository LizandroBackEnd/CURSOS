class Model(): 
    table = False 
    def __init__(self):  
        if not self.table: 
            print("Error, defined the table")  

    def save(self): 
        print(f"Saving {self.table} in BBDD")  

    @classmethod    
    def search_id(self, _id): 
        print(f"Searching for id {_id} in the tabble {self.table}")
         
class User(Model): 
    table = "User" 
     
usuario = User() 
usuario.save() 
 
User.search_id(1)