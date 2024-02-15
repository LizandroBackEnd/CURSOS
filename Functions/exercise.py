#Ejercio Palindromo 

def palindromo(palabra): 
    palabra = palabra.replace(' ', '') 
    palabra = palabra.lower() 
    palabra_invertida = palabra[::-1] 
    if palabra == palabra_invertida: 
        return True 
    else: 
        return False 
     
      
print("Bola", palindromo("Bola"))
