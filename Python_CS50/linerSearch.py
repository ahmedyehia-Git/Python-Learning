import sys

nums =[2,4,5,6,7,8,0]

if 9 in nums:
    print("found")
    sys.exit(0) # using (0) in case of found and (1) in case of not found
print("not found")
sys.exit(1)
### same for string 

# names = ['ahmed', 'adham' , 'eslam']

#if 'eslam' in names:
#    print('name found')
#    sys.exit(0)
#print('name not found')    
#sys.exit(1) 