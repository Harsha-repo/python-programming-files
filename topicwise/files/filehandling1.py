age = input('enter your age :')
f = open('filehandling.txt','r+')
#f.write(age)
#f.close()
if f:
    print('file opened')

print(f.name,'encoding is :',f.encoding,'mode is :',f.mode)  # knowing the file name

print(f.readable())
print(f.writable())
if f.readable():
    print('file is readable')
 