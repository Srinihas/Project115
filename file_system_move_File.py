import os

source_path = input("What is the name of the file that you want to rename? ")
dest_path = input("What should we rename that file to? ")

os.rename(source_path, dest_path)
print(f"{source_path} has been renamed to {dest_path}")