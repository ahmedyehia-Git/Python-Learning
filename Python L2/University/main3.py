
from students2 import students
from Date3 import DOB


s1 = students()  
s1.fName = input('Enter the student first name: ')
s1.lName = input('Enter the student last name: ')
#s1.dateOfBirth = input('Enter the student date of birth: ')
print("Please enter the DOB(day, Month, Year):\n")
day = int(input("Please enter the day as two digits:\n"))
month = int(input("Please enter the month as two digits:\n"))
year = int(input("Please enter the year as four digits:\n"))
s1.dateOfBirth = DOB(day, month, year)
s1.id = int(input('Enter the student ID: '))
s2 = students() 
s2.fName = input('Enter the student first name: ')
s2.lName = input('Enter the student last name: ')
#s2.dateOfBirth = input('Enter the student date of birth: ')
print("Please enter the DOB(day, Month, Year):\n")
day = int(input("Please enter the day as two digits:\n"))
month = int(input("Please enter the month as two digits:\n"))
year = int(input("Please enter the year as four digits:ahmed\n"))
s2.dateOfBirth = DOB(day, month, year)
s2.id = int(input('Enter the student ID: '))

print(s1.fName + ' ' + s1.lName + '\n' ,s1.dateOfBirth , '\n',s1.id)
print(s2.fName + ' ' + s2.lName + '\n' ,s2.dateOfBirth , '\n',s2.id)



# we need tomake DOB input like other parameters,this need more data this will tried in main3 
# manage to do by the above method, entering day, month & year sepretly, faild to get it as list 
# we need to make validation for the data input, days for example should be between 1 - 31, Month 1 - 12
# also we need to make sure that DOB input do not contain text
# in shapes program we will make validation and some other techniqus that manage all operation in the class file as we tried to do in this one but could not 