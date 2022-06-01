from students import students


s1 = students()  # this create new object from the main class that can have specific data for a student
s1.fName = input('Enter the student first name: ')
s1.lName = input('Enter the student last name: ')
s1.dateOfBirth = input('Enter the student date of birth: ')
s1.id = int(input('Enter the student ID: '))
# we can add new variable like s1.emai; s1.address without intiating it in the class 
# this option only valid forPython 

#print(s1.stuData()) # this one if we use return function in stuData
s1.stuData() # this one of we use print function in stuData
#s1.privet(), this one will give error as it is privet not public 