def sumnaturalnum(n) :
    if n<=0 :
        return n
    else:
        return n+sumnaturalnum(n-1)
    
n = int(input('enter a number : '))
if n<=0 :
    print('enter the positive number ')

else: 
    print('sum of natural numbers ')
    print(sumnaturalnum(n))
