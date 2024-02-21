#Ejercicio 1: Eliminar los espacio en blanco de un string y devolver una lista con los caracteres restantes. 
  
string = "Hola Lizandro como estas" 
 
def delete_space(s): 
    return [char for char in s if char != " "]
  
#print(delete_space(string)) 
 
#Ejercicio 2: Contar en un diccionario cuanto se repiten los caracteres de un string 
  
def count_chars(s): 
    chars_dict = {} 
    for char in s: 
        if char in chars_dict: 
            chars_dict[char] += 1 
        else: 
            chars_dict[char] = 1 
    return chars_dict 
 
#print(count_chars(string)) 
 
#Ejercicio 3: Ordenar las llaves de un diccionario por el valor que tienen las tuplas y devolver una lista 
 
def order(dict): 
    return sorted( 
        dict.items(), 
        key=lambda key: key[1], 
        reverse=True,
    )  

#print(order(count_chars(string)))
 
  
#Ejercicio 4: De un listado de tuplas, devolver tuplas que tengan de el mayor valor 
 
def max_tuples(list): 
    max = list[0][1] 
    reply = {} 
    for order in list: 
        if max > order[1]: 
            break 
        reply[order[0]] = order[1] 
    return reply 
 
#print(max_tuples(order(count_chars(string))))  
 
#Crear un mensaje que diga: Los caracteres que mas se re3piten con 4 repeticiones son: -C , -D 
 
def create_message(dict): 
    message = "Los que mas se repiten son:  \n" 
    for key, valor in dict.items(): 
        message += f"El caracter {key} se repite {valor} veces\n" 
    return message 
 
#print(create_message(max_tuples(order(count_chars(string)))))
 
