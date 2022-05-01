import os
import shutil

#Write the name of the directory here
#Which needs to be sorted
#Path=""
path=input("Enter the name of the directory to be sorted")

#This will create a proper ogrinized list with 
#all the file names which has directory
list_of_files=os.listdir(path)

#This will go through each and every file
for file in list_of_files:
    name,ext=os.path.splitext(file)

    ext=ext[1:]

    #This forces the next iteration 
    if ext=="":
        continue

    #this will move the file to the directory
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    
    