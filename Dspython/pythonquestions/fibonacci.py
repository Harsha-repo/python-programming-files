n = int(input('size of fibonacci'))
a=0
b=1
res=0
for i in range(0,n):
    print(res)
    a=b
    b=res
    res=a+b
    
