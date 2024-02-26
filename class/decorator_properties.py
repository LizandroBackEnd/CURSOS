class Perro: 
    def __init__(self, name): 
        self.name = name

    @property    
    def name(self): 
        return self.__name


    @name.setter     
    def name(self, name): 
        if name.strip(): 
            self.__name = name 
        return 
     