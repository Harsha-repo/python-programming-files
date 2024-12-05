# NAME : HARSHA 
# USN  : 1CR22AI044

# HETEROGRMS 

s1 = 'abhi'
s2 = 'run'
count=0
for char in s1:
    if char in s2:
        count=count+1

if count==0 :
    print('heterogram')
else:
    print('not heterogram')