
x = int(input("How many number you will use: "))
nums = []

for i in range (x):
    nums.append(int(input(f"Enter number {i+1}: ")))

print(f"Avarage = {sum(nums)/len(nums)}")
