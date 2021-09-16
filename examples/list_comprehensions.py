# this is how we previously did a map function
print(list(map((lambda x: x * 2), range(1, 11))))

# this is a list comprehension which does the same as above
# a list comprehension is a way to execute an expression
# against an iterable
print([2 * x for x in range(1, 11)])

# this is how we previously did a filter function
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

# this is how we can do a filter using a list comprehension
print([x for x in range(1, 11) if x % 2 != 0])

# gen list of 50 vals, take them to power of 2, then return all that are mults of 8
print([x ** 2 for x in range(1, 51) if (x ** 2) % 8 == 0])

# nested for loops
print([ x * y for x in range(1, 3) for y in range(11, 16)])

# nested list comprehensions - inner lc generates list for outer
# lc to iterate over
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])