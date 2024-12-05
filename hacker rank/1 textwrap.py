str = 'abcdefghijklmnopqrstuvwxyz'
c=0
i=1
while(i<len(str)and str[i-1]!='\0'):
    i+=1
   
    if(i%4==0 and i!=len(str)):
        for c in range(c,i):
            print(str[c],end='')
        c=i
        print('\n',end='')
        #print('c = ',c , ' i ' ,i)

    if i%4!=0 and i==len(str):
        for j in range(c,i):
            print(str[j],end ='')
    
        
        