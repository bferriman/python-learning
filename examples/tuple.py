# a tuple is like a list that once created, the values in it cannot be changed
my_tuple = (1, 2, 3, 5, 8)

# values are accessed in the same way as lists
print("1st Value :", my_tuple[0])

# you can get slices
print(my_tuple[0:3])

# length
print("Length :", len(my_tuple))

# concatenate / join tuples
more_fibs = my_tuple + (13, 21, 34)

# check for a value in a tuple
print("34 in Tuple :", 34 in more_fibs)

# iterate over a tuple
for i in more_fibs:
    print(i)

# convert a list to a tuple
a_list = [55, 89, 144]
a_tuple = tuple(a_list)

# convert a tuple to a list
a_list = list(a_tuple)

# find max / min value in a tuple
print("Max :", max(a_tuple))
print("Min :", min(a_tuple))