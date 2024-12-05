import copy
a = 'harsha'

 # numeric memory address 
l = [1,2,3,4,5]

l.append('harsha')
print(id(l))   # even of the adding of the element the numeric address do not change
spam = ['s','b','c']
id(spam)
cheese = copy.copy(spam)
cheese.append('sorry')
print(id(cheese))
print(cheese) # this is the copy list 
print(spam)  # this is original list 
# if the list u copy contain a list then call deep copy function and then print it 
l2= [1,2,3,4,5,['s', 'b', 'c', 'sorry']]
l3 = copy.deepcopy(l2)
print(l3)   
# copy is used to make a copy of any original variable and make changes in them 
#keeping original as it is 
