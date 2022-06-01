mark=float(input("Please enter your mark"))

if 0 <= mark < 50:
    print("Your grade is F")
elif 50 <= mark < 65:
    print("Your grade is D")
elif 65 <= mark < 75:
    print("Your grade is C")
elif 75 <= mark < 85:
    print("Your grade is B")
elif 85 <= mark <= 100:
    print("Your grade is A")
else: print("Error, Your mark should be between 0 and 100")