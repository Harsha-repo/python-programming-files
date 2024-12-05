''''merging text files '''
files=[]
merged_data=''
while True:
    f_name=input('enter a file name:')
    files.append(f_name)
    ans=input('want to add another file?')
    if ans!='y':
        break
for file in files:
    filename=file+'.txt'
    f=open(filename,mode='r',encoding='utf-8')
    merged_data=merged_data+f.read()
    f.close()
print(merged_data)