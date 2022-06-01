n = 0
t = 0

def PrintMyName():
    for x in range(1,11):
        print("Ahmed Sobhy")

def PrintYear():
    for x in range(1, 11):
        print("2020")

def PrintN(n, t):
    for x in range(0, n):
        print(t)

def CallNT(n, t):
    n = int(input("please inter number of copies\n"))
    t = input("Please inter the text to be copied\n")
    for x in range(0, n):
        print(t)

PrintMyName()
PrintYear()
print("..............")

CallNT(n, t)
