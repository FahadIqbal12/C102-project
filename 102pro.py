# This project is made for sorting different types of files in a folder
# It can sort many files at once
# This project helps to make our work easier

import os
import shutil
path=input('Enter the name of directry to be sorted : ')
list_of_files =os.listdir(path)

for file in list_of_files :
    name,ext=os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else :
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
