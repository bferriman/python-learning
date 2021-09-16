# We can annotate functions to specify their expected argument
# and return types. This does not affect actual behavior of the 
# code, it is just for documentation and usability.

def random_func(name: str, age: int, weight: float) -> str:
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)
    return "{} is {} years old and weighs {} lbs".format(name, age, weight)

print(random_func("Geoffrey", 39, 218))
# this still executes just fine, in spite of not matching
# expected argument types
print(random_func(12, "Becky", True))
# print a function's annotations
print(random_func.__annotations__)