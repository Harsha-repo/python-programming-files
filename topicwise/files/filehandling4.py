''' to check file exist or not 
this mothod belongs to path module which is sub module of os module 

import os 
os.path.isfile(filename )
this will check for the presence of that file inside memory
if present returns True 
else false '''
import os 
os.path.isfile('filehandling.txt')
''' read() fucntion to read the data and return string type 
if data is binary then returns bytes 
syntax = file_object.read(size) size is number of characters to be read '''
f = open('filehandling.txt',mode='r')
data = f.read(2) # this is starting point of the text where pointer points 
data1=f.read(7)   # but here again it wont go to the starting point but data1 starts from where data left its pointer
# hence we get the out put in that way
print(data)   
print(data1)
f.close()