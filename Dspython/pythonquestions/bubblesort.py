l=[]

n=int(input('enter the size of the list:'))
for i in range(0,n):
    l.append(int(input()))
print('the list elements are :')
for i in l:
    print(i)
temp=0
for i in range(0,n):
    for j in range(0,n-1):
        if(l[j]>l[j+1]):
            temp = l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)     
l1=[]
for num in l:
    if num not in l1:
        l1.append(num)
print(l1)
            
# bubble sort in pyhton using temp variable      
  
 

  