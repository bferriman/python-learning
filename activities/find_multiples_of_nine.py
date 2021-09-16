# find multiples of nine from random 100 value list of values between 1 - 1000

import random

random_list = []
for i in range(100):
    random_list.append(random.randrange(1, 1001))

mults_of_9 = list(filter((lambda x: x % 9 == 0), random_list))
print(mults_of_9)