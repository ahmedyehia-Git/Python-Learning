

x = 1
l = []
print("Enter numbers you need to add to list, to exit enter any letter")

while True:
    x = input()
    if x.isdigit():
        x = float(x)
        l.append(x)
    elif x.isalpha():
        print(l)




















