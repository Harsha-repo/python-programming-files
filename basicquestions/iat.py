from pathlib import Path
import os
print(str(Path('spam','bacon')))
homefolder = r'c:\users\ai'
subfolder='spam'
print(Path(homefolder)/Path(subfolder))
print(Path.cwd())
# you can also change the directory usiing os.chdir() it gives error if you try to change it to a absent directoryy
 # will hive the current working directory we nood to import os module
 os.makedirs() is to create new directoris with folders and subfoler