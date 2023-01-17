#!python3

#guess game version 2
#using git/github for versions & repo

print('enter a guess upper range:')
u = int(input())

print('enter a guess lower range:')
l = int(input())

import random
m = random.randrange(l, u)

print('guess the secret number between',l,'and',u,'?')
n = int(input())

i = 1
while n != m :
    
     if n > m :
          print('guess lower:')
     else:
          print('guess higher:')
      
     i = i+1
     n = int(input())
    
print('Right! It took you',i,'guesses to find the secret number:',m)

