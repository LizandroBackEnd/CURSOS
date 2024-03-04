from pathlib import Path  
from time import ctime
 
file = Path("files/file_test.txt")  
#file.exists() 
#file.rename() 
#file.unlink() 
 
#print(file.stat())
 
print("acces", ctime(file.stat().st_atime)) 
print("creation", ctime(file.stat().st_ctime))
print("change", ctime(file.stat().st_mtime))
