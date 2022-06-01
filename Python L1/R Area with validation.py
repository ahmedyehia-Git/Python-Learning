print("This program to calculate rectangular area")
print()
#L = input("Please enter the length ")
#W = input("Please enter the width ")

L = float(input("Please enter the length "))
W = float(input("Please enter the width "))

if L>=0 and W>=0:
    A = L * W
    print("Area =", A)
else: print("Error, please enter valid positive numbers")


