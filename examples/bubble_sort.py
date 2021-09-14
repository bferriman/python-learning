# Bubble sort iterates through list comparing and swapping values
# so that after the first iteration, the largest value is in the
# last position. The next iteration checks all values except the
# last, which we know is already sorted, and so on.

import random

num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 10))

i = len(num_list) - 1
while i > 0:
    j = 0
    while j < i:
        # swap values if element at ind j is > than next element
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        j += 1
    i -= 1
