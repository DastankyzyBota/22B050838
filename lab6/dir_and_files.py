#1
import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#2
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))

# Exist: False
# Readable: False
# Writable: False
# Executable: False

#3
import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
"""
Test a path exists or not:
False
False

File name of the path:
g:\\testpath\\p.txt

Dir name of the path:
"""

#4
def file_lengthy (num):
        with open(num) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

print("Number of lines in the file: ",file_lengthy("test.txt"))

#5 list to file
fruits = ['Orange', 'Kiwi', 'Apple', 'Banana']
with open('abc.txt', "w") as myfile:
    for i in fruits:
        myfile.write("%s\n" % i)

content = open('abc.txt')
print(content.read())

"""
Orange
Kiwi
Apple
Banana
"""
#6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#7
from copy import copyfile
copyfile('test.py', 'abc.py')

#8
import os

file = 'file.txt'  
location = "/home/User/Documents"
path = os.path.join(location, file)  
os.remove(path)

print(“The file has been removed")