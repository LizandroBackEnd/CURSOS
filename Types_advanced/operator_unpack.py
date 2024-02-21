#Combiana dos listas en una sola lista usando el desempaquetado  
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
  
lists = [*lista1, *lista2]
 
print(lists)  
 
#Combina diccionarios usando el desempaquetado 
user = {"name": "Lizandro", "age": 25} 
user_info = {"id": 1, "email": "code@", "z": "User"} 
 
info = {**user, **user_info} 
 
print(info)
 
