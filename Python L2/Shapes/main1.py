from circle1 import circle
from square1 import squere
from rectangle1 import rectangle

shape = int(input("Please select the shape number, 1 for circle, 2 for rectanguler, 3 for square: "))

if shape == 1:
    c = circle()
    c.printResult()

elif shape == 2:
    r = rectangle()
    r.printResult()

elif shape == 3:
    s = squere()
    s.printResult()