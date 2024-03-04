from io import open 
 
""" Writing 
text = "New text to write in the file" 
 
file = open("files/new_file.txt", "w") 
file.write(text) 
file.close() """ 
 
""" Reading 
file = open("files/new_file.txt", "r") 
text = file.read() 
file.close() 
print(text) """ 
 
""" Readind with lines 
file = open("files/new_file.txt", "r") 
text = file.readlines() 
file.close() 
print(text) """ 

""" Readind with lines
with open("files/new_file.txt", "r") as file:  
    for line in file: 
        print(line)"""  
 
""" add  
file = open("files/new_file.txt", "a+") 
file.write("Bye world :|") 
file.close() """ 
 
# Readind and writing  
with open("files/new_file.txt", "r+") as file: 
    text = file.readlines() 
    file.seek(0) 
    text[0] = "New line in file" 
    file.writelines(text)
