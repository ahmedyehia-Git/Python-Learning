class squere:

    def __init__(self):
        self.__l = float
        self.readData()
               
    def readData(self):
        self.__l = self.validate()                
        
                     
    
        
    def getArea(self):
        
        return self.__l**2
        
        
    def getPrimeter(self):
        
        return 4 * self.__l
        
    def printResult(self):
        print("Area = ", self.getArea(), 'Cm^2' )
        print("Primeter = ", self.getPrimeter(), 'Cm' )
    
    #def validate(self): this another working code for positive and negatve input but not for string
    #    a = input("Radius in cm (use numbers only) = ")
    #    b = float(a)
    #    if b > 0:
    #        return float(a)
    #    elif b < 0:
    #        return self.validate()
    #    elif a == str:
    #       return self.validate()
               
    def validate(self): # this is the only way that make validation to input to be float (numbers) only
        while True:
            try:
                value = float(input("Length in CM: " ))
            except ValueError:
                print("Sorry, you have to enter numbers only.")
                continue

            if value < 0:
                print("Sorry, you have to enter positive numbers only!!")
                continue
            else:
                break
        return value

    
        
    
        
        
# we make all needed operations within the class
# we need to add (self) for all methods within the class
# In this way we have to forget about get and set methods
# good example for encapsulation and validating data before use it in the program 
# in circle1 try to validate the input if it is string we should ask user to make correction but could not do it yet

#def validate(self): this function work well for floats but it break and stop program if string
#        a = input("Radius in cm = ")
#        if float(a) > 0:
#            return float(a)
 #       elif float(a) < 0:
  #          print("Please enter positive number!")
   #         return self.validate()
    #    elif type(a) != float:
     #       print("Please enter numbers only!")
      #  self.validate()
      
