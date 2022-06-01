
from students2 import students
from Date import DOB


s1 = students()  
s1.fName = input('Enter the student first name: ')
s1.lName = input('Enter the student last name: ')
#s1.dateOfBirth = input('Enter the student date of birth: ')
s1.dateOfBirth = DOB(25,12,96)
s1.id = int(input('Enter the student ID: '))

s2 = students() 
s2.fName = input('Enter the student first name: ')
s2.lName = input('Enter the student last name: ')
#s2.dateOfBirth = input('Enter the student date of birth: ')
s2.dateOfBirth = DOB(12,9,96)
s2.id = int(input('Enter the student ID: '))

print(s1.dateOfBirth)
print(s1.fName + ' ' + s1.lName + '\n' ,s1.dateOfBirth , '\n',s1.id)
print(s2.fName + ' ' + s2.lName + '\n' ,s2.dateOfBirth , '\n',s2.id)
print(students.number)

# we need tomake DOB input like other parameters,this need more data this will tried in main3 