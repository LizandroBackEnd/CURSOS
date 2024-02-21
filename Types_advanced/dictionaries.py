punto = {"x": 25, "y":50}  
print(punto)
print(punto["x"]) # 25 
 
punto["z"] = 45 
  
  
print(punto.get("z")) #La función get() devuelve el valor de la clave especificada. 
del punto["x"] # Elimina la clave x 
del (punto["y"]) # Elimina la clave y 
 
punto["x"] = 25 # Añade la clave x  
 
# Formas de acceder a los diccionarios
 
for valor in punto.items(): #Devuelve una lista de tuplas, cada tupla contiene un par de valores clave-valor
    print(valor) 
     
for llave, valor in punto.items(): 
    print(llave, valor) 
     
#Uso real de los diccionarios 
     
usuarios = [ 
    {"id": 1, "nombre": "Lizandro"}, 
    {"id": 2, "nombre": "Jesus"},
    {"id": 3, "nombre": "Antonio"},
    {"id": 4, "nombre": "Nate"},
    {"id": 5, "nombre": "Juan"},
] 
 
for usuario in usuarios: 
    print(usuario["id"], usuario["nombre"])