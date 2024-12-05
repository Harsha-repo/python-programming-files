a = (input("enter the number :"))

product = 1
sum=0

for i in a:
    product = product*int(i)
    sum=sum+int(i)

if product==sum :
    print("spy number")

else:
    print("no a spy number")
