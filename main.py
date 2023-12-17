import shutil
import os
from schedule import every, repeat, run_pending
import time

list_files = os.listdir('E:\\BackupAmin')
list_files.sort()
list_files.pop()

print(list_files)

src = "I:\\BackupAmin"  # example: D:\demo
dest = "C:\\Users\\JIHAD\\Dropbox\\BackupAmin"  # example: D:\DemoCopy
toSearch = list_files[-1]  # example: "Dataset.csv"
folder = file = 0

try:
    os.makedirs(dest)
except:
    print("ALREADY EXISTED")


@repeat(every(60).minutes, src, toSearch)
def checkFile(src, searchFile):  # Recursive Fuction to Check the file in each Folder
    global folder, file
    # listDir returns all files and folder within the src in src_file
    src_file = os.listdir(src)
    for file_name in src_file:
        # this create a path by joining src and file_name
        full_file_name = os.path.join(src, file_name)
        if os.path.isdir(full_file_name):  # check weather it is a directory or a file
            folder += 1
            # Again call the function recursively until it reach the last folder
            checkFile(full_file_name, toSearch)
        else:
            if file_name == toSearch:
                # Copy the file to the destination folder
                shutil.copy(full_file_name, dest)
            file += 1


while True:
    run_pending()
    time.sleep(1)


# checkFile(src, toSearch)
# print("FOLDER", folder)  # COUNT OF TOTAL FOLDERS
# print("FILE", file)  # COUNT OF TOTAL FILES