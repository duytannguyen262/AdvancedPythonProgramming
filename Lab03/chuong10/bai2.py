import os

os.chdir('E:/HOC TAP/AdvancedPython/Lab03/chuong10')

alkaline_metals = []
for line in open('alkaline_metals.txt'):
    alkaline_metals.append(line.strip().split(' '))

print(alkaline_metals)