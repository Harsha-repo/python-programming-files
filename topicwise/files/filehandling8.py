fp=open('filehandling.txt','r')
l=[]
l2=[]
lines=0
for line in fp.readlines():
    word=l.extend(line.split())
    
    numofcharacters=l2.extend(line)
    
    lines+=1

    

print('number of words in file is ',l)
print('the charcters are :',l2)
print('the number of characters are :',len(l2))
print('the lines are ',fp.read())
print(lines)