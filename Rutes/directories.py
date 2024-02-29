from pathlib import Path 
 
path = Path("Directory") 
path.exists() #Comprueba si el directorio existe 
path.mkdir() #Crea el directorio 
path.rmdir() #Elimina el directorio 
path.rename("NewDirectory") #Renombra el directorio