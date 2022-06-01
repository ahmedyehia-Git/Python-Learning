
x = int(input("Enter number, to end enter 0 \t"))
sum = 0
min = x
max = x
counter = 0
while x!= 0:
    counter = counter + 1
    if min> x:
        min = x
    if max < x:
        max = x
    sum = sum + x
    average = sum/counter
    x = float(input("Enter number, to end enter 0 \t"))
print("sum = ", sum)
print("counter = ", counter)
print("min = ", min)
print("max = ", max)
print("Average = ", average)