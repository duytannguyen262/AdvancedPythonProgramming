import os

os.chdir('E:/HOC TAP/AdvancedPython/Lab03/chuong10')
filename = input('Write name of the file you want to backup: ')
new_filename = filename + '.txt'
bak_filename = filename + '.bak'
backup = open(bak_filename, 'w')
for line in open(new_filename):
    backup.write(line)

backup.close()


