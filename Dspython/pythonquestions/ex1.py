#lets say we have list with reapeated elements to remove and ensure that they are in same order

l=[2,4,5,4,5,6,8]
l1=[]
for num in l:
    if num not in l1:
        l1.append(num)
#print(l1)
        



#there is a short cut oneliner

new_list =list(dict.fromkeys(l).keys())
print(new_list)