from os import listdir
from matrix_cleaner import MatrixCleaner

# Open a file
path = '/home/tassia/Desktop/data/data/kernels'
dirs = listdir(path)

# This would print all the files and directories
file: str
for file in dirs:
    filepath = path + '/' + file
    data = MatrixCleaner.load(filepath)
    print(file)
    # print(data)
    print()


