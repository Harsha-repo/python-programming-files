l=[]                            # declare a list to store string when seperated using split 
dict1={}                        # dictionary to count and assign the number of repetaion in convinient manner
fp = open('Ram Siya Ram.yml','r') # file opening in reading mode
for line in fp.readlines():         # reading eachline inthe file
    l.extend(line.split())          # extending the readed lines into the list 
for j in set(l):                     # avoiding the repetaion using set() function 
    r=l.count(j)                     # the number of times each word repeated
    dict1[j]=r            # dict1[j] where j is refering to each word of the text and r is count of each word
print(dict1)             #printing the dictionary
a1=sorted(dict1,key=dict1.get,reverse=True)# sorting dictionary based on the value but not key using sorted()
#count=int(input('enter the number of words repetations wnted to know :'))# initializing count
count =0
for i in a1:                    
    print('the frequency of ',i,'is',dict1[i])      
    if count==10:
        break
    count=count+1
    