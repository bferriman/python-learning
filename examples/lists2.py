import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 10))

num_list.sort()
num_list.reverse()
num_list.insert(5, 10)  # insert value, (index, value)
num_list.remove(10)  # remove first instance of value
num_list.pop(2)  # remove value at provided index

for k in num_list:
    print(k, end=", ")
print()  # print newline char
