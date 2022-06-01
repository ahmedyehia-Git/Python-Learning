l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[-1])
print(l1[0:4])
print(l1[:6])
print(l1[3:])

l2 = l1.copy()

l1[2] = 30
l1.append(10)
l1.insert(0, 50)
print(l1)
print(l2)