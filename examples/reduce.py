# reduce receives a list and returns a single result
from functools import reduce
# reduce builds a combined result by using the passed
# function to iteratively combine each value in the
# range/list with the combined result so far

# on first pass, list[0] gets passes as x, list[1] as y
# second pass, result of first pass is x, list[2] is y
# and so on
print(reduce((lambda x, y: x - y), range(1, 6)))