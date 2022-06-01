X = float(input("Please enter first number\n" ))
Y = float(input("Please enter the second number\n"))
Z = float(input("Please enter the Third number\n"))

if Y <= X <= Z:
    print(Y, X, Z)
elif Y <= Z <= X:
    print(Y, Z, X)
elif Z <= Y <= X:
    print(Z, Y, X)
elif Z <= X <= Y:
    print(Z, X, Y)
elif X <= Z <= Y:
    print(X, Z, Y)
else: print(X, Y, Z)

