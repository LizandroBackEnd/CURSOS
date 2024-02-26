class Coordenadas: 
    def __init__(self, lat, lon): 
        self.lat = lat
        self.lon = lon 
         
    def __eq__(self, otro): 
        return self.lat == otro.lat and self.lon == otro.lon  
     
    #def __ne__(self, otro): 
    #    return self.lat != otro.lat or self.lon != otro.lon  

    def __lt__(self, otro): 
        return self.lat + self.lon < otro.lat + otro.lon 
     
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon 

        
     
      
cords = Coordenadas(2, 15) 
cords2 = Coordenadas(12, 15)
 
#print(cords != cords2)  
print(cords <= cords2)