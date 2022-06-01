# x = float(input("Please enter first number "))
# Y = float(input("Please enter the second number "))
# operation = input("Please enter the required operation [+, -, *. /] ")

x = float(input("Please enter first number\n" ))
Y = float(input("Please enter the second number\n"))
operation = input("Please enter the required operation [+, -, *. /]\t")

if (operation == "+"):
    A = x+Y
    print(x,"+", Y,"= ",  A)
elif (operation == "-"):
    A = x-Y
    print(x,"-", Y,"= ",  A)
elif (operation == "*"):
    A = x * Y
    print(x,"*", Y,"= ",  A)
elif (operation == "/"):
    if Y !=0:
        A = x/Y
        print(x,"/", Y,"= ",  A)
    else: print("Error; system can't divide by 0")

else: print("Error; you should enter operation from [+, -, *, /]")
