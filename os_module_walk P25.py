# count number of folders and files in given directory
import os
total_files = 0
total_folders = 0

os.chdir('D:\\')

current_folder = os.getcwd()
for root, folders, files in os.walk(current_folder):
    total_folders += len(folders)
    total_files += len(files)

print(f"Total folders :- {total_folders} \n Total Files :- {total_files} \n Total :- {total_folders + total_files}")
