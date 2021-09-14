def mult_divide(num_1, num_2):
    # functions can return multiple values, just comma separate
    return (num_1 * num_2), (num_1 / num_2)


mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)


def sum_all(*args):  # receive an unknown num of arguments
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


print("Sum =", sum_all(1, 2, 3, 4, 5))
