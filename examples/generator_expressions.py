# generator expressions look a lot like list comprehensions
# but return results one at a time
# generator expressions use () instead of []

double = (x * 2 for x in range(10))
print("Double:", next(double))
print("Double:", next(double))
print("Double:", next(double))

# you can iterate through as well
for num in double:
    print(num)