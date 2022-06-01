# this not CS50 but from Udacity introduction to Python, data scince profissional track
doc = "Some collection classes are mutable. the methods that add, the subtract, or rearrange their members in place, and\n don’t return a specific item, never return the collection instance itself but None"

print(len(doc))#to know leangth of the string
print(doc.split()) # this separate string to list of separated word, this one separatd by sapce
print(doc.split('.')) # this one separated by '.'
print(doc.split(' ',3)) # make separation for texts with sapces, 3 only then the rest of text all together as one item

firstInd = doc.find("the") # return the first index of a defind word in string, note that it is case sensitive
lastInd = doc.rfind("the") # return the last index of the word
theCount = doc.count("the") # return the numnber of defind word in the string
print(f"The firs the is palced at index {firstInd}, and the last the is at {lastInd}, number of 'the' is {theCount}")
# f equal to format