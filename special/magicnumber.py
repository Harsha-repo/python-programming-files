import string
import random
A = string.digits

n = int(input('enter a number:'))
for i in range(n):
    l=[]
    for j in range(n):
        l.append(random.choice(A))

    for element in l:
        print(element,end=('\t'))
    print()