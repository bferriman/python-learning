my_list = [1, 2, 3, 4]

# using map function
doubled_list = list(map((lambda num: num * 2), my_list))
print("doubled_list: ", doubled_list)

# using list comprehension
tripled_list = [num * 3 for num in my_list]
print("tripled_list: ", tripled_list)
