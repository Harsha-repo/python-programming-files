fp = open('filehandling.txt',mode='r')
f2=open('filehandling1.txt',mode='w+')
for line in fp:
    f2.write(line)
f2 =open('filehandling1.txt','r')

print(f2.readlines())
''' we have write and write line functions that helps to write any lines of string into another file 
first we create a list of strings and then we use writelines funcitons on it to append the txt into the file
created 
'''
f2=open('filehandling1.txt','r+')
l=['harsha\n','arun\n','abhi\n']
f2.writelines(l)

