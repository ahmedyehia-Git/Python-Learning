class students:
    # we remove the firstpart which is about declaration as this can be done directly in constractorsection
        
    # 2- Constructors (to intiate class,set the intial values for the different attreputes that I will use)
    # in tis coopy we makeall attreputes as privet and let user access it through method 
    # through this way I can make valedation of input before usig it in the class, e.g. the formate of birthdate or the id that could not contain letter
    # encapsulation aim to protect code and so data either in method section or attrepute section 
    # the main wahy to show the heddin variable is to use "get" and for modifining it is to use "Setting" methods, this is in all programing languages 
    # in Python there is additionalmor simple method to make this happened 
    def __init__(self):
        self.__fName = 'Ahmed'
        self.__lName = 'Yehia'
        self.__dateOfBirth = '20 Aug. 1965'
        self.__id = 2020101
        self.__motherName = ' Layla'
# we do not need to intiate all variables, in the main file we can create new variable for the object
# this is only valid for python not anyother programing languge 

# as we below methods is valid in Python and any other langage to access and change hidden attrepute 
    def getfname(self):
       # he we can add some other codes validate the credential of the user for example
        return self.__fName
    
    def setfName(self, fName): # user can change the value of fName
        # add any validation code that required
        self.__fName = fName
 
 # the following method is dedicated for Python only, it allow use the name of attrepute as the name of calling method so it will be easy
 # we make the lName using the Python style
    
    @property # this anotation that the following method is not reguler one it is special one
    def lName(self):
        return self.__lName
    
    @lName.setter # this annotation mean that the folloing method is to set the value of encapsulated attrepute 
    def lName(self, lName): # note that the 2 special method can have the same name although they make different function 
         self.__lName = lName
        
    # 3- Behaviors (group of methods) (methods is functions)
    
    def stuData(self):
        #return self.fName + ' '+ self.lName + ' ' + self.dateOfBirth + ' ', self.id
        print(self.fName + ' '+ self.lName, '\n' , self.dateOfBirth ,'\n', self.id)
        # in return it will add all data in one line we could not make it in separet lines
        # using print to make te data in separate lines 
        # in both concatonat using "+" work only for string, for id (int) we should use ","
    
    def __privet(self):
        print(self.__motherName)
        # this method is privet can not be called outside this calss
        # anything we need to make it privet, either variable or variable we should writ 2 underscore before it "__"