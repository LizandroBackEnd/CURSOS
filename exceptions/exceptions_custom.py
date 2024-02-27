class Myerror(Exception): 
    "This class is for representing my Custom Exception" 

    def __init__(self, message, code): 
        self.message = message  
        self.code = code 
         
    def __str__(self): 
        return f"{self.message} - type error: {self.code}"

 
def division(n = 0): 
    if n == 0: 
        raise Myerror("Page not found", 404) 
    return 5 / n 
 
try: 
    division() 
except Myerror as e: 
    print(e)