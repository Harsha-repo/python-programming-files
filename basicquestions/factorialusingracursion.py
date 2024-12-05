def factorial(n)  :
    if n<=0 :
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input('enter number :'))

if n<=0 :
    print('enter a positive integer')

else:
    print('the fatorial is :')
    print(factorial(n))