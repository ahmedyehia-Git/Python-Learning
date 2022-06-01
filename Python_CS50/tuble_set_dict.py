# list = [1,2,3]
# tuble = (1,2,3)
# set = {1,2,3}
# in set you could not access internal item or change it, used for high secure data
# in tuble you can access internal items but you could not change it 
# in list you can access and change internal items
# list and tuble allow repeated items e.g. [3,3,3] but in set this is npt allowed, it will return 3 only 
# dict = dictionary each record contain Key:Value

dict = {
    "name":"Ahmed",
    "age": 55,
    "country":"Egypt"
}
print(dict)
print(dict["name"]) # we refere to item by its key not index
print(dict["age"])
print(dict["country"])