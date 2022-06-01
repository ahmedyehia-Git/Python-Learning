# lower() change all input text to lower case
# upper() change all input text to upper case
# capitalize() change the first letter to capital

s = input("Are you agreed?")
if s.lower() in ['y','yes']:
    print("Agreed")
elif s.upper() in ['N', 'NO']:
    print("Not Agree")
else:
    print("Please use Yes or No")
