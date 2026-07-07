import os
path_var = input("Enter the directory you want to analyze: ")
count_dr = 0
count_root = 0
count_py = 0
if os.path.exists(path_var):
    for root,dirs,files in os.walk(path_var):
        for file in files:
            if file.endswith():
                count_py = count_py + 1 
        count_dr += len(dirs)
else:
    print("This directory does not exist!")
print(count_dr)
print(count_py)