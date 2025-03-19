'''
Reading Files

Open function does not read the file, but makes the possible you can read the file

This is the function: open()

Return a file "file handle" a variable used to perform operations on the file

Similar to file open 

handle = open(filename, mode)

The mode is optional to (r)ead it or (w)rite 

A text can be thought of as a sequence of lines

/n = indicates that we're supposed to go to another line

fhand = open('mbox.txt')
print(fhand)


fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])


Searching Through a file 

varToFile = open("document to read")
for line in varToFile
    if line.startswith('From:') :
        print(line)

Strip the second line break

varToFile = open("document to read")
for line in varToFile
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

        The second way but is the same

varToFile = open("document to read")
for line in varToFile
    line = line.rstrip()
    if not line.startswith('From:') :
    continue 
    print(line)        

- The newline is considered "white space" and is stripped

The difference between .strip() and .rstrip() in Python is:

.strip() → Removes both leading (left) and trailing (right) whitespace.
.rstrip() → Removes only trailing (right) whitespace.

input_file = input("Enter the file name: ")
varToFile = open(input_file)
count = 0
for line in varToFile:
    #line = line.rstrip()
    if line.startswith('Subject:') :
        count = count + 1
    print('There were ', count , 'subject lines in ', input_file)

    fname = input("Enter the file name: ")
try: 
    fhand = open(fname)
except: 
    print('File cannot be opened: ', fname)
    quit() ##Comes and never returns
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were ', count, 'subject lines in ', fname)
'''


