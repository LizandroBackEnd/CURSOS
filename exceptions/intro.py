try: 
    n1 = int(input("Enter a number: ")) 
except ValueError as e: 
    print("Type valor correct") 
except NameError as e: 
    print("Name error")