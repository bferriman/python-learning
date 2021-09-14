rand_list = ["string", 1.234, 56]
one_to_ten = list(range(1, 11))  # create list of values 1-10
rand_list = rand_list + one_to_ten
print(rand_list[0])

# most all string methods work with lists as well
print("List length", len(rand_list))

first_3 = rand_list[0:3]  # get slice of first 3 items in list
for i in first_3:
    # print index of the element, followed by element itself
    print("{} : {}".format(first_3.index(i), i))

print(first_3[0] * 3)  # print first element 3 times

# check for "string" in the list, returns True of False
print("string" in first_3)
print("Index of string:", first_3.index("string"))  # find index of "string"
# find num of occurences of "string"
print("How many strings:", first_3.count("string"))
first_3[0] = "New String"  # assign new value to element
first_3.append("Another Element")  # append new element to end of list
