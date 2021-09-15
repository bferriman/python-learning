import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("Line:", line_num, ":", line, end="")
        line_num += 1