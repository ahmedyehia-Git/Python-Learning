
#Y = int(input("Please enter the multiplier\t "))

#for i in range(1, 13, 1):
#    x = Y * i
#    print(Y, "*", i, "=", x)

Y = int(input("Please enter the multiplier\t "))

for i in range(1, (Y+1), 1):
    x = Y * i
    print(Y, "*", i, "=", x)