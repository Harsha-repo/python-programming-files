s = 'abcdABCD'
l=[]
for i in s:
   if i.islower():
       i = i.upper()
       l.append(i)
   elif i.isupper():
       i=i.lower()
       l.append(i)
s1=str(l)
print(s1)