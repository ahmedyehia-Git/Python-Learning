# elements in set should be between these brackets {}
# you could not access items in set but you can add to it
# set does not accept duplications so if there is (2 , 2) set will use only one of them
# unlike list and tuple st has no indexing

s = {6, 3, 5, 10, 98, 2}
s.add(55)
s.update([45, 3, 65])
print(s)
print("................")

s.remove(2)
s.discard(100) #if item not ther it does not give error while remove give
print(s)
print("................")

# del s, delete s or ny other
# s.pop(), remove any element of set randomly
# s.clear, remove data but set still there

y = {3 ,5, 40, 11}
t = s.union(y)
print(t)