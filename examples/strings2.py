rand_string = "     this is an important string     "

# remove white space on left
rand_string = rand_string.lstrip()
# remove white space on the right
rand_string = rand_string.rstrip()
# remove white space from left and right
rand_string = rand_string.strip()

print(rand_string)

# capitalize first character
print(rand_string.capitalize())
# capitalize all characters
print(rand_string.upper())
# make all characters lower case
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
# concatenate list items into a string with a " " separator / delimiter
print(" ".join(a_list))

# create a list from words in a string and print
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)

# find num of occurances of a substring in a string
print(rand_string.count("is"))

# find index of a substring in a string
print(rand_string.find("string"))

# replace a substring
print(rand_string.replace(" an ", " a marginally "))
