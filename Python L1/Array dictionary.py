# use {}
# contain key (variable name) and its value
# can be accessed, add, delete and update

d = {"Name": "Ahmed",
     "Age" : "55",
     "Last Name": "Yehia"}
print(d)
print(".................")
print(d["Name"])
print(".................")

# keys is case sensitive
d["Name"] = "Ahmed Sobhy"
for x, y in d.items():
    print(x+":", y)
print(".................")
d.pop("Age")
for x, y in d.items():
    print(x+":", y)
print(".................")