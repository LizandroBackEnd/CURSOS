name = "lizandro" 
name2 = "LIZANDRO"   
name3 = "   Lizandro Antonio   "
 
#Metodos de strings 
 
print(name.upper()) #El metodo upper() nos permite convertir un string a mayusculas 
print(name2.lower()) #El metodo lower() nos permite convertir un string a minusculas 
print(name.capitalize()) #El metodo capitalize() nos permite convertir la primera letra de un string a mayuscula 
print(name.title()) #El metodo title() nos permite convertir la primera letra de cada palabra a mayuscula 
print(name3.strip()) #El metodo strip() nos permite eliminar los espacios en blanco al inicio y al final de un string  
print(name3.lstrip()) #El metodo lstrip() nos permite eliminar los espacios en blanco al inicio de un string 
print(name3.rstrip()) #El metodo rstrip() nos permite eliminar los espacios en blanco al final de un string 
print(name.find("z")) #El metodo find() nos permite buscar un caracter en un string y nos devuelve la posicion de la primera ocurrencia,Si el caracter no se encuentra en el string, el metodo find() nos devuelve - 
print(name.replace("l","L")) #El metodo replace() nos permite reemplazar un caracter por otro en un string 
print("liz" in name) #El operador in nos permite verificar si un string se encuentra en otro string, nos devuelve True si se encuentra y False si no se encuentra 
print("liz" not in name) #El operador not in nos permite verificar si un string no se encuentra en otro string, nos devuelve True si no se encuentra y False si se encuentra
 
#Encadenamiento de metodos  
 
print(name.strip().capitalize()) #Encadenamos el metodo strip() con el metodo capitalize()