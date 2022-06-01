fact = 1
x= int(input("Please enter the number you need to multiply its factorial\n"))
for i in range(1, (x+1), 1):
    fact = fact * i
print("Factorial = ", fact)