from pathlib import Path
import os

absolutepath=os.path.abspath('filehandling.txt')
print(absolutepath)  # it takes only  path as argument only one 
relativepath=os.path.relpath('filehandling1.txt')
print(relativepath)   # it takes two arguments that is (path,start) if start is not mentiones then
                     # current working directory is considered as start 