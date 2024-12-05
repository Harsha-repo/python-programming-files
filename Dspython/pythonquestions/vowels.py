s = input("enter a string :")
s1="aeiouAEIOU"
c=0
for i in s:
    for j in s1:
        if i==j:
            c=c+1
            
print(c)