# iterables are objects with an __iter__ method which return an iterator
# an iterator is an object with a __next__ method which returns the next
# value from a sequence of values

# make an iterator
samp_str = iter("Sample")

print("Char:", next(samp_str))
print("Char:", next(samp_str))