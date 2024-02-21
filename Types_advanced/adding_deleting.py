mascotas = [ 
    "perro",  
    "gato",  
    "loro",  
    "perro",  
    "pez", 
    "gato",  
    "conejo" 
] 
 
mascotas.insert(1, "tortuga") # Inserta "tortuga" en la posición 1
mascotas.append("hamster") # Añade "hamster" al final de la lista 
 
mascotas.remove("gato") # Elimina la primera ocurrencia de "gato"
mascotas.pop(1) # Elimina el elemento en la posición 1
del mascotas[0] # Elimina el primer elemento de la lista 
mascotas.clear() # Elimina todos los elementos de la lista
print(mascotas)