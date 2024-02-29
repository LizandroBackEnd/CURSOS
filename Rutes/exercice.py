from pathlib import Path 
 
path = Path() 
paths = [p for p in path.iterdir() if p.is_dir()]   
 
dependencies = { 
    "db": "Connect to the database", 
    "api": "Connect to the API", 
    "web": "Connect to the web server",
}
 
def load(p): 
    package = __import__(str(p).replace("/", "."))  
    try: 
        package.init(**dependencies) 
    except: 
        print("The package has no init function.")
 
list(map(load, paths))