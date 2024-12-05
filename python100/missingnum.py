# we have given a string of numbers in which there is missing number inbetween sequence find and print the missing number
s=input()
l=[]
for i in s:
    l.append(int(i))

# METHOD 1
# for i in range(len(l)-1):
#     if (l[i]+1!=l[i+1]):
#         print(l[i]+1)

# METHOD 2
# l1=[]
# print(l)
# for i in range(l[0],l[len(l)-1]):
#     l1.append(i)
# for i in l1:
#     if i not in l :
#      print(i)

# METHOD 3
# for i in range(len(l)-1):
#     if l[i]==l[i+1]-1:
#         continue
#     else:
#         print(l[i+1]-1)

# METHOD 4
# Another efficient approach is to use the XOR operation. The approach is based on the idea that XOR 
# of a number with itself is 0, and XOR of a number with 0 is the number itself.
#  This means that if we find XOR of first N natural numbers and then take XOR of each array elements with this,
#  then the resultant will be the missing number.


