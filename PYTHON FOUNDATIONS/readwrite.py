"""
Reading and eriting to a file
topics:
1.Creating a new file and write to it
2.reading a file line by line
3.File open modes
4.With statement
"""
"""
creating a new file called funny.txt using
and write some statement in 
open statement for reading and writing a file
"""
"""
use \\
"""
"""
w- is a mode for writing to a file
"""
"""
always close a file after writing to it
f=open("C:\\Users\\DigitalEthers\\Desktop\\DATA SCIENCE FOR GITHUB\PYTHON FOUNDATIONS\\read_write_file\\funny.txt","a")
f.write("\nI Love JS")
f.close()
"""


"""
what if you dont want to ovveride the file
and just append to it
for that you need to use "append" mode-a
new line(\n)
"""

"""
Reading a file line by line
we want the python programme to read the file
and count the number of words in each sentence
and towards the end it sshould append the word count
and we are going to create a file with a word count at
the end of each line
"""

f=open("C:\\Users\\DigitalEthers\\Desktop\\DATA SCIENCE FOR GITHUB\PYTHON FOUNDATIONS\\read_write_file\\funny.txt","r")
"""
reading the entire file content
print(f.read())
f.close()
"""

"""
counting number of words in eachline usiing for loop
for line in f:
    print(line)

f.close()
words are seperated by spaces if you can detact the space
you can figure number of words
spilt()-function splits string using a seperator(' ')
when we split the string, it will give a list(array) of tokens
tokens is nothing but a list of words

for line in f:
    tokens=line.split(' ')
    print(len(tokens))

f.close()
"""
"""
we are going to open a file for word count called f_out
the name in the directory will be  funny_wc.txt
"""
f_out=open("C:\\Users\\DigitalEthers\\Desktop\\DATA SCIENCE FOR GITHUB\PYTHON FOUNDATIONS\\read_write_file\\funny_wc.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write("wordcount"+str(len(tokens))+line)


f.close()
f_out.close()
"""
oppening a file for reading and writng you use r+
W+ raeding and writing
diffrence : W+ if the doesnt exist it will create the file
r+ wont create a file
"""
"""
with statement
if you want to avoid explicitly closing a file you 
have to use a with statement
"""
with open("C:\\Users\\DigitalEthers\\Desktop\\DATA SCIENCE FOR GITHUB\PYTHON FOUNDATIONS\\read_write_file\\funny.txt","r") as f:
    print(f.read())
print(f.closed)
"""
f.closed tells you if a file open or closed
"""

