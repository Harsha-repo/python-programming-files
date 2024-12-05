n = int(input("enter the number :"))
c=0
l=[]
l1=[]
for i in range(2,n+1):
    
    for j in range(1,i+1):
        if(i%j==0):
            l.append(i)
for i in l:
    if(l.count(i)==2):
     l1.append(i)       
print(set(l1))
    
               
            
            

            
        
        

