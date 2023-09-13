import os
import shutil

from_dir = "C:/Users/PRIYA NAIR/OneDrive/Downloads"
to_dir = "C:/Users/PRIYA NAIR/OneDrive/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name, ext = os.path.splitext(file) 
    #print(name)
    #print(ext)
    if ext == "":
       continue
    if ext in [".txt", ".docx", ".doc", ".pdf"]:
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + "Document Files"
        path3 = to_dir + "/" + "Document Files" + "/" + file
    if (os.path.exists(path2)):
            print("moving")
            shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print("moving")
        shutil.move(path1, path3)    