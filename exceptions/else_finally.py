try: 
    n1 = int(input("Enter a number: ")) 
except ValueError as e: 
    print("Ocurred error!!")  
else: 
    print("No error ocurred 😊") 
finally: 
    print("Dates saved correctly 😊😊😊")
