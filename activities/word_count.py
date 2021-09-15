import os

def text_analyzer(file_name):
    with open(file_name, encoding="utf-8") as file:
        line_num = 1
        while True:
            line = file.readline()
            if not line:
                break
            
            print("Line", line_num)
            word_list = line.split()
            num_words = len(word_list)
            print("Number of Words :", num_words)
            total_chars = 0
            for word in word_list:
                total_chars += len(word)
            avg_chars = total_chars / num_words
            print("Avg Word Length : {:.2f}".format(avg_chars))

            line_num += 1

input_file = input("Enter name of file to read: ")
text_analyzer(input_file)