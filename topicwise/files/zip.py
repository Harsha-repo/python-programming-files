import os  # importing os module 
import zipfile  # import zipfile module
zf = zipfile.ZipFile('myzipfile.zip','w')  # zipfilename  as user need and in write mode
for dirname ,subdirs,files in os.walk(r'C:\Users\JAWID HUSSAIAN S\Desktop\project'): # path has to be given 
    zf.write(dirname)  # writing directory name in zip
    for filename in files:# files iteration
        zf.write(os.path.join(dirname,filename))# joining the paths
    zf.close()#closing the zip