# count number of folders and files in given directory
import os
total_files = 0
total_folders = 0

user_path = input("Please enter a Directory = ")
if os.path.exists(user_path):
    for path, folder, file in os.walk(user_path):
        total_folders += len(folder)
        total_files += len(file)
    print(f"Total Folders = {total_folders}\nTotal Files = {total_files}")
else:
    print("Please enter a valid Directory/path")

