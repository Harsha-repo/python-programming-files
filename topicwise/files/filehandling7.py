'''tell() method and seek() method
 file pointer is what which reads the charcters from starting to end of file 
that cursor is what which reads or writes the files 
tell()  this method is to find the current position of the file pointer fromthe beginnig 
of the file 

position starts from 0 it is jsut like indexing in string
syntx : file_object.tell()  

seek()  this method is to change the position of file pointer to required index position
remember file pointer always starts from the beginnig 
syntax : file_object.seeek()  inside a size argument where you seek the cursor wants to be  '''

fp=open('filehandling.txt','r')
 # initially the file pointer is at 0 index 
#fp.read(5)

#fp.read()
#c=fp.tell()
d =fp.seek(50)
print(d) 
print(fp.read())
fp.seek(0)
print(fp.read(6))
print(fp.tell())
fp.close()
