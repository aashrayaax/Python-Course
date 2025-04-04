import os

# Specify the directory path
directory_path = '/'

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
