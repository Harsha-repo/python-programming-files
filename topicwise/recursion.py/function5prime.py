
def prime(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return False
    else :
        return True
n = int(input("enter the number:"))
if prime(n):
    print('prime number')
else:
    print('not a prime')

