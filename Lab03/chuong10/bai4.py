import os

os.chdir('E:/HOC TAP/AdvancedPython/Lab03/chuong10')

with open('example_file.txt','r') as file:
    next(file)
    contents = file.read()
    print(contents)
