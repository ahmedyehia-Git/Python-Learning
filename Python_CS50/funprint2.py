def draw(x):
    for i in range (x):
        print('#')

    for i in range (x):
        print("@", end=" ") # 'end' use to add parameter to print the defult (end="\n")
    print("")

x = int(input("Please enter number of blocks: "))

draw(x)
