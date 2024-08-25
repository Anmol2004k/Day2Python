import os

# this also problem 5 in problem 5 we have to just write comment for this programme

#specify the disconery you want to list 
directory_path = '/'

#list all files and directories in the specific path 
contents = os.listdir(directory_path)

#print each file and directory name 
for item in contents:
    print(item)