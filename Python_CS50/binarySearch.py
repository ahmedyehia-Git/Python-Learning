# binry search go to the middle to find the number, if found it is fdone, if not it sshould look if the number less or more than the number in mid
# if smaller he will deal with the numbers less than middle as new list and start look for the number in he new middle
# if mor it will deal with the numbers more than the one in the middle as a new list
# to do binary search list should be sorted from min to max

import sys

def mid(start, end): # this function it math equation to calculate the middle of any 2 numbers
    return start + (end - start) // 2 # // mean all equation result will be divided by 2 and return integer numbewr

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

start = 0
end = len(num) - 1
i = 0
x = int(input("Please enter the number that you search for: "))

while start <= end:
    i += 1
    m = mid(start, end)
    if x == num[m]:
        print(f"Number {num[m]} found after {i} loop")
        sys.exit(0)
    elif x < num[m]:
        end  = m -1
    elif x > num[m]:
        start = m + 1
        
if x not in num:
    print(f"{x} not found") 
    sys.exit(1)   
    