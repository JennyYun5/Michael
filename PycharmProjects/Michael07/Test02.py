import os

note = './note/English.txt'
print(os.path._getfullpathname(note))
f = open(os.path._getfullpathname(note))
txt = f.read()
print(txt)
for a, b, c in os.walk(note):
    print(a, b, c)
