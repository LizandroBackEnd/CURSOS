numeros = [12, 20, 11, 7, 8, 75, 34] 
 
#numeros.sort()  Ordena la lista de menor a mayor 
#numeros.sort(reverse=True)  Ordena la lista de mayor a menor
numeros2 = sorted(numeros, reverse=True) # Ordena la lista de menor a mayor 

print(numeros) 
print(numeros2) 
 
usuarios = [ 
    ["Lizandro", 4], 
    ["Juan", 1], 
    ["Angel", 6]
] 

usuarios.sort(key=lambda el:el[1], reverse=True) 
print(usuarios)
 
