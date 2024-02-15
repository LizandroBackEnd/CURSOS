def saludo (nombre, apellido="Santos"): #Parametros
    print("Hola!") 
    print(f"mi nombre completo es {nombre} {apellido}") 
     
      
saludo("Lizandro", "Antonio") #Argumentos
saludo("Lizandro") 
 
saludo(apellido="Hernandez", nombre="Pedro")