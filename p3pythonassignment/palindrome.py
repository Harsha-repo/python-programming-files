s = 'malayalam'
l = list(s)
count=0
print(l)
for i in l:
    count=count+1

for i in range(0,count):
    if l[i]==l[count-i-1]:
        flag=1
        
    else:
        flag=0
if flag:
    print('is palindrome')
else:
    print('not a palindrome')