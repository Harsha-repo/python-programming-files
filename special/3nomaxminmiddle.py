n=3
l=[]
for i in range(n):
    l.append(int(input('append elements:')))
print(l)
print('the maximum element is :',max(l))
print('the minimum element is :',min(l))
print('the middle element is :', sum(l)-max(l)-min(l))