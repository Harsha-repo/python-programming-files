"""syntax of file 
f = open('filename','mode='',buffering,encoding=None,errors = None , newline=None,closf=True)"""

'''buffering : used to set bufffer size for a file where sharing of the file rate is determined 
in text mode befering size must be 1 or more than 1  
i byte at eavery time 
default value of buffering = 4096-8192


encoding : this is used to decode or encode files 
should be used in text mode only 
default value on os 
for windows : 1252


errors : represents how encoding and decoding errors are handled 
cannot be used in binary mode
some standard values are : strict ,ignore,replace


newline : \n,\r,\r\n  '''