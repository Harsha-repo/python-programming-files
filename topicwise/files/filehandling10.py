'''x mode file writing 
used to write data in file 
it writes only in a new file '''
data='rama'
f = open('filehandling2.txt',mode='x')
f.write(data)
f.close()
