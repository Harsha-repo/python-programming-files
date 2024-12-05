n1 = int(input("enter first number:"))
n2 = int (input("enter the second number :"))
list=[]
if n1>n2:
    l = n1
else:
    l=n2
for i in range(1,l+1):
    for j in range(1,l+1):
        if n1*i == n2*j :
            k=n1*i
            list.append(k)

print((min(list)))
        
       