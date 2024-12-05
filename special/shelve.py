import shelve
sfile=shelve.open('filehandling.txt')
print(sfile)
shelve.close()
