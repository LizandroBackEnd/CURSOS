from pathlib import Path 
from zipfile import ZipFile 
  

with ZipFile("files/compacting.zip", "w") as zip:
    for path in Path().rglob("*.*"): 
        if str(path) != "files/compacting.zip": 
            zip.write(path) 
             
with ZipFile("files/compacting.zip") as zip: 
    info = zip.getinfo("files/compacting.py") 
    print(info.file_size, info.compress_size) 
     
    zip.extractall("files/compacting")