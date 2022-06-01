class circle:

    def __init__(self):
        self.__r = 0
        self.readData()
               
    def readData(self):
        radius = float(input("Radius in cm = "))
            
        if radius < 0:
            print("Please enter positive number!")
            self.readData()
        #elif radius > 0:
        #    self.__r = radius
        else:
            self.__r = radius
                 
        
    def getArea(self):
        from math import pi
        return pi * (self.__r)**2 
        
    def getPrimeter(self):
        from math import pi
        return 2 * pi * self.__r
        
    def printResult(self):
        print("Area = ", self.getArea(), 'Cm^2' )
        print("Primeter = ", self.getPrimeter(), 'Cm' )
    
    
        
# we make all needed operations within the class
# we need to add (self) for all methods within the class
# In this way we have to forget about get and set methods
# good example for encapsulation and validating data before use it in the program 