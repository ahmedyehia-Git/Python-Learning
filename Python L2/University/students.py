class students:
    # any calss should contain 3 main items
    # 1- Attreputes (group of variables that)
    fName = ' '
    lName = ' '
    dateOfBirth = ' '
    id = 1111
    
# the above section is a must in all programing languges but not for Paython so we can amke class without this section
# and define variables in the constructor section directly
    
    # 2- Constructors (to intiate class)
    def __init__(self):
        self.fName = 'Ahmed'
        self.lName = 'Yehia'
        self.dateOfBirth = '20 Aug. 1965'
        self.id = 2020101
        self.__motherName = ' Layla'
# we do not need to intiate all variables, in the main file we can create new variable for the object
# this is only valid for python not anyother programing languge 
    
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