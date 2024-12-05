n = int(input('enter required range of fibonacci required:'))
a = 0
b = 1
c = 0

for i in range(0,n+1) :
    print(c)
    a=b
    b=c
    c=a+b
    