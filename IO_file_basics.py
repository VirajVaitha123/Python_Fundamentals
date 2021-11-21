## IO Basics

# pwd in cmd line shows you where the current file is
# read in text file
myfile = open(r'data/textfile.txt')

print(myfile.read())

# sometimes the file has been read and the cursor is at the end of line. So we use seek(0) to return to the start of the line.
myfile.seek(0)

# Read in each line as a string as a part of a list
print(myfile.readlines())

# Since we opened the file we have to close it
myfile.close()

# alternatively use the with statement
with open('data/textfile.txt') as f:
    contents = f.read()

# we no longer need to close the file with this technique.

# write or append to files (r, w or a)
with open('data/textfile.txt', mode = 'a') as f:
    f.write("\n additional text appended")
    contents = f
    print(contents)

with open('data/textfile.txt', mode = 'r') as f:
    print(f.read())
   
with open('data/writenfile.txt', mode = 'w') as f:
    f.write("I wrote this file")
    

