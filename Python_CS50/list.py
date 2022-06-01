# list can take any type of data including list as well

list = [1, "ahmed", 1.5 ,[1,2,5]]
print(list) # print full list
print(list[2]) # print item through it index
print(list[0])
print(list[1])
print(list[3][2]) # print item with list item using index of index

list[1]=["Sobhy"] # this how to change any item in the list
print(list[1])

for i in range(len(list)):
    print(type(list[i]))
    
    