import random 
import string
 
list = [20, 16, 10, 5] 
random.shuffle(list) 

print( 
    random.random(), 
    random.randint(1, 10), 
    list
) 
 
# Example PASSWORD 
 
chars = string.ascii_letters 
digits = string.digits 
selection = random.choices(chars + digits, k=12) 
 
password = "".join(selection) 
print(f"Your password is: {password}")