# os module enables interaction with file system
import os

# with ensures file will close if program crashes
# open will open existing file or create new one if it doesn't exist
# modes: w = write (overwrite existing data), a = append
with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text\nMore random text\nAnd some more")

# if no mode specified, default is read
with open("mydata.txt", encoding="utf-8") as my_file:
    # read() reads entire file into one string
    # readline() reads up to and including first new line char
    # readlines() returns list of lines
    print(my_file.read())

# check whether file is closed
print(my_file.closed)

print(my_file.name)
print(my_file.mode)
os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
# make a directory
os.mkdir("mydir")
# navigate to a directory
os.chdir("mydir")
# print current working directory
print("Current Directory :", os.getcwd())
os.chdir("..")
# remove a directory
os.rmdir("mydir")