one_to_ten = range(1, 11)
def dbl_num(num):
    return num * 2

# map takes a function and executes it for each item in a list, range, etc.
# need to convert resulting map object to a list in most cases
print(list(map(dbl_num, one_to_ten)))

# the function passed to map can be an anonymous function
print(list(map((lambda x: x * 3), one_to_ten)))

# map can accept functions that execute against multiple lists
# if the function takes two args, you pass map two lists
a_list = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(a_list)