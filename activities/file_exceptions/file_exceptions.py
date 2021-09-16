try:
    my_file = open("activities/file_exceptions/mydata2.txt", encoding="utf-8")


except FileNotFoundError as ex:
    print("File not found")
    print(ex.args)

else:
    print(my_file.read())
    my_file.close()

finally:
    print("***file access ended***")