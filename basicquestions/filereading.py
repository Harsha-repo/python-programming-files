fp=open('Ram siya Ram.yml','r')  # way to initialize the file and read it 
for line in fp.readlines():  #read() function reads the file text completely
    print(line,end="") #end ="" do not allow new line 