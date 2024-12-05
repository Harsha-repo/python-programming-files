'''after performing some opertaion on file 
files should be closed so we use in built python function called close()

syntax = filehandler.close()
what happens is the file object which is created to access the file is now deleted 
so no access through objectt is possible hence file closed 

when we do not close file : there is garbage collector in the python which will destroy file 
object and close the file automatically
this happens only when execution is complete and then g.c works properly

note : do not rely on garbage collector 0
please close the file as soon as operation on it completes '''