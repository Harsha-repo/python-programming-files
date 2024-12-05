str = input("enter the binary number:")
count=0
for i in str:
    if i=='1':
        count+=1
if count%2==0:
    parity='1'
else:
    parity='0'

print(str+parity)