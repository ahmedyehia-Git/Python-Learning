from circle import circle

shape = int(input("Please select the shape number, 1 for circle, 2 for rectanguler, 3 for square: "))

if shape == 1:
    c = circle()
    c.printResult()
