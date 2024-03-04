import json 
from pathlib import Path 
 
""" Write Json 
 
products = [
     {"id": 1, "name": "Computer"}, 
     {"id": 2, "name": "Mouse"},
     {"id": 3, "name": "Keyboard"},
] 
 
data = json.dumps(products)
Path("files/products.json").write_text(data) """ 
 
# Read Json 
 
data = Path("files/products.json").read_text("utf-8") 
products = json.loads(data) 
print(products) 
 
# Change Json
  
products[0]["name"] = "Update name" 
Path("files/products.json").write_text(json.dumps(products))