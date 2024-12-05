""" three methods of reading a file 
1. read()
2.readline()
3. readlines()
read() is to read the data from a file and return it as a string . you can give a size as argument that will 
print the txt respective to the size 
read() will read the entire txt of file but returns the output inthe string form

readline ()  is the method used to print single line of txt file , it can acess a single line at time, returns
the out put  in the form of string 


readlines() this is same as the readline() 
function but it will read the entire txt in the file at time 
and it returns you the output in the form of lists  

also you can use loops to acesss the file txt line by line see the example code below  """

f = open('filehandling.txt','r')
data=f.readlines() # will return list of lines ,each line of file are   SEPERATED USING COMMA INSIDE THE RETURNED LIST
print(list(data))
# for line in list(data):
#     print(line)
# f=open('filehandling.txt','r')
# data1=f.readline()
# print(data1)
# f.close()

# f= open('filehandling.txt','r')
# c=f.read()
# print(c)