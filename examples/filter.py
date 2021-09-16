# filter takes a function to evaluate each item in a list/range
# and return true or false, builing a filter object containing
# the values that returned true. Convert to list.
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))