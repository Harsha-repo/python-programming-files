n = int(input("enter the size of the list"))
l=[]
print('enter the array elements')
for i in range(0,n):
    l.append(int(input()))

print(l)
#reapeat check
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            print(l[i])