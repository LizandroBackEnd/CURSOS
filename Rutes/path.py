from pathlib import Path 
 
#Path(r"C:\Users\user\Documents\") Ruta absoluta 
#Path("one/__init__.py") Ruta relativa 
 
path = Path("hola-mundo/mi-archivo.py") 
path.is_file() 
path.is_dir() 
path.exists() 
 
print( 
    path.name,      #Nombre del archivo y su extensión 
    path.stem,      #Nombre del archivo
    path.suffix,    #Extensión del archivo
    path.parent,    #Ruta del archivo padre
    path.absolute() #Ruta absoluta del archivo
) 
 
p = path.with_name("Users.py") #Cambia el nombre del archivo 
print(p) 
p = path.with_suffix(".txt") #Cambia la extensión del archivo 
print(p) 
p = path.with_stem("Users") #Cambia el nombre del archivo sin extensión 
print(p)