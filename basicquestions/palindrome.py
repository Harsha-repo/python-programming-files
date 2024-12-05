n = int(input('enter a number:'))

res=0
temp=n
while temp>0:
    rem=temp%10
    res=res+rem*10
    temp=res//10

if temp==res:
    print(res)
    print('the number is palindrome')
else:
    
    print('the number is not palindrome')