primer = {1, 2, 3, 4} 
segundo = [3, 4, 5] 
segundo = set(segundo) 
 
print(primer | segundo) # Union
print(primer & segundo) # Interseccion 
print(primer - segundo) # Diferencia 
print(primer ^ segundo) # Diferencia simetrica