usuarios = [ 
    ["Lizandro", 4], 
    ["Juan", 1], 
    ["Angel", 6]
]  
 
#nombres = [] 
#or usuario in usuarios: 
#    nombres.append(usuario[0]) 
#print(nombres) 
  
#Transformacion MAP
#nombres = [usuario[0] for usuario in usuarios] 
 
#Filtar  FILTER
#nombres = [usuario for usuario in usuarios if usuario[1] > 2] 
 
#Filtrar y transformar 
#nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] 
 
  
#MAP 
#nombres = list(map(lambda usuario: usuario[0], usuarios)) 
 
#FILTER  
nombres = list(filter(lambda usuario: usuarios[1] > 2, usuarios))  
print(nombres) 
