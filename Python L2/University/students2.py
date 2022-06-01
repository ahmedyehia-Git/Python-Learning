# this is clean version of the file, using the encpsulation in Python way
# it is ggod practice to makeall attrepute privet
# in this file we use composition, using class within another class, take dateof birth as example 
    # wheneverthe attrepute consist of more than one variable I should consederas class
    # date of Birth is complex attrepute consist of 'day' . 'month', 'year' so I should get this info through another class called for example "date"
    # this can allowus to make validation for input e.g. day should not be more than 31, month not more than 12
# we use a class variable that related tothe class no to the objects (attreputes) inside the clas

from builtins import property
from Date import DOB

class students:
    
    number = 0 # this is Class variable
    
    def __init__(self):
        self.__fName = 'Ahmed'
        self.__lName = 'Yehia'
        #self.__dateOfBirth = '20 Aug. 1965'
        self.__dateOfBirth = DOB(1,1,1)
        self.__id = 2020101
        students.number = students.number + 1 # this code tocount the number of students
        

    @property 
    def fName(self):
        return self.__fName
    
    @fName.setter 
    def fName(self, fName):  
        self.__fName = fName
    
    @property 
    def lName(self):
        return self.__lName
    
    @lName.setter 
    def lName(self, lName):  
        self.__lName = lName
        
    @property 
    def dateOfBirth(self):
        return self.__dateOfBirth
    
    @dateOfBirth.setter 
    def dateOfBirth(self, dateOfBirth):  
        self.__dateOfBirth = dateOfBirth
         

    @property 
    def id(self):
        return self.__id
    
    @id.setter 
    def id(self, id):  
        self.__id = id
        
