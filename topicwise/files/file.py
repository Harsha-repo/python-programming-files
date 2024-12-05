""" files are used to store the data permanently inside the computer '
to retrieve the data when ever required 
 data is stored in an non voaltile memory
 they are named locations on the disks that store inforamtion

types of files
    1 text files : to store the data in  the form of characters used to store strings and 
        numbers 
    binary files : those files that are stored in the form of bits 
        these are audio files ,video files , others  


files handling : the meaning 
   opening the file
   doing some operation on  the file
   and closing the file properly 

   these steps carried properly comprises file handling
below there is a sample code
"""
fp = open('filehandling.txt',mode='r+',buffering = 10)
if fp :
	print('file successfully opened')
print(fp)
print(fp.name,'encoding is :',fp.encoding,'buffering is:',fp.buffer,'mode is :',fp.mode)
# encoding='cp1252'> or windows 
# while giving key word argument position dont matter 
# in position agument position are fixed to their key words so you need to give exact arguments at the right places
print(fp.readable())
print(fp.writable())


 