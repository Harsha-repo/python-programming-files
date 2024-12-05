def prime(i,n):
    if i==n :
        return True
    elif n%i==0 :
        return False
    else :
        return prime(i+1,n)
    
n = int(input('enter the number'))
i=2
if prime(i,n) :
    print('is prime number ')
else :
    print('not a prime')