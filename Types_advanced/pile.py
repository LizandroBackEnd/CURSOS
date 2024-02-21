pila = [] 
pila.append(1) 
pila.append(2)
pila.append(3)
print(pila) 
last_element = pila.pop() 
print(last_element) 
print(pila) 
print(pila[-1]) 
 
if not pila: 
    print("La pila está vacía") 
else: 
    print("La pila no está vacía")