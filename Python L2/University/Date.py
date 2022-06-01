
class DOB:
    def __init__(self, day, month, year):
        self.__day = day 
        self.__month = month
        self.__year = year
        
    @property
    def day(self):
        return self.__day
        
    @day.setter
    def day(self, day):
        #if 1<= day >=31:
         self.__day = day
        #else:
         #   print("Please enter valid day (1 - 31)")
           # day
        
    @property
    def month(self):
        return self.__month
        
    @month.setter
    def month(self, month):
            #if 1<= month >=12:
        self.__month = month
            #else:
            #    print("Please enter valid month (1 - 12)")
            #    month
    @property
    def year(self):
        return self.__year
        
    @year.setter
    def year(self, year):
        self.__year = year 
        
# the out come of DOB came like this
# <Date.DOB object at 0x000001F40712BF40>
# it point to the placein memory that comntain this nformation
# we need to use one of magic methods to print it in the right way
# magic method is built in method start and end with doub underscore like __init__

    def __str__(self):
        return str(self.__day) +"/" + str(self.__month) +"/" + str(self.__year)
    # we should convert the DOB form int to str to be used in this magic method