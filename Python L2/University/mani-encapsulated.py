from students_encpsulated import students # we change the name of file

s1 = students()  # this create new object from the main class that can have specific data for a student
s = input('Enter the student first name: ') # we could not assign variable to method so we need to get the value first then added to the method in next step
s1.setfName(s)  # we call the function setName to access and change the fName
s1.lName = input('Enter the student last name: ') # by this method I can assigne value directly from input as usaal althou we deal with lname here as method

#s1.dateOfBirth = input('Enter the student date of birth: ')
#s1.id = int(input('Enter the student ID: '))
 # we can add new variable like s1.emai; s1.address without intiating it in the class 
 # this option only valid forPython 

 #print(s1.stuData()) # this one if we use return function in stuData
#s1.stuData() # this one of we use print function in stuData
#s1.privet(), this one will give error as it is privet not public 

print(s1.getfname()) # we use this method to get the data of fname
print(s1.lName) # again here we call the property method of lName 
