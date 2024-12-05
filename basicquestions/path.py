from pathlib import Path
import os
c=os.path.abspath('filehandling.txt') # this is absolute path that starts from drive name 
print(c)
r=os.path.relpath('filehandling.txt','coding')  # this gives only the relative path to the original

print(r)     