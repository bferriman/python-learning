def mult_by_2(num):
    return num * 2

# can assign a function to a variable
times_two = mult_by_2
print("4 * 2 =", times_two(4))

# can pass a function as an argument to another function
def do_math(func, num):
    return func(num)

print("8 * 2 =", do_math(times_two, 8))

# a function can generate and return another function
def get_func_mult_by_num(num):
    def mult_by(value):
        return num * value
    return mult_by

generated_func = get_func_mult_by_num(5)
print("5 * 9 =", generated_func(9))

#can embed functions in data structures
list_of_funcs = [times_two, generated_func]
print("5 * 9 =", list_of_funcs[1](9))