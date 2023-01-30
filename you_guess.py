#!python3

#guess game version 1

b=100
a=0

import random
m = random.randrange(1, 100)
#print(m)

print('guess my number between 1-100?')
n = input()

i=1
while int(n) != m :
    
    if int(n) > m :
        print('guess lower:')
    else:
        print('guess higher:')
        
    i = i+1
    n = input()
    
print('Right! It took you',i, 'times to find',m)


