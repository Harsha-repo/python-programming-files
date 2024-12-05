'''ren=moving the punctuation from the string that is entered by the user make it plane 
we use iteration and run on each character and if the charcter is not a alphbet then we do not print it '''

s='what\'s ur name how\'s you'
print(s)
emptystr=''
pun = ''''"-!<>.,:;{}[]()'''
for i in s:
    if i not in pun:
        emptystr=emptystr+i

print(emptystr)
