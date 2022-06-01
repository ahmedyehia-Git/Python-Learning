# same as list different in () not [].
# data in tuple can be accessed but could not be changed.

l1 = (1, 2, 7, 8)
print(l1[:2])
print(".............")

# we can change tuple to list to have copy of dat that we can change without changing main data
# and then we can change it again tobe tuple

l = list(l1)
print(l1)
print(l)
print(".............")
l.reverse()
t = tuple(l)
print(l1)
print(l)
print(t)