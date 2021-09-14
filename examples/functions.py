def add_numbers(num_1, num_2):
    return num_1 + num_2


print("5 + 4 =", add_numbers(5, 4))

# variables defined inside functions are not accessible outside the function

# if accessing a global variable within a function, the variable must be declared within the function with the "global" keyword
name = "Bilbo"


def change_name():
    global name
    name = "Frodo"


change_name()
print(name)

# functions in python don't return anything by default
