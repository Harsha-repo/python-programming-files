# consider a three digit number now armstrong number is that three digit number 
# which is returned when u multiply each number with itself for three times and add all them 
# gives the same digit you have taken

num = 153
num2=num
s=len(str(num))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+pow(rem,s)
    num=num//10
    
print(sum)  

if sum==num2:
    print('yes iam armstrong')
else:
    print('not an armstrong')
 
