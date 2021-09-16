# generate a list of 50 random values between 1-1000
# return those that are multiples of 9

import random

print([x for x in [random.randrange(1, 1001) for i in range(50)] if x % 9 == 0])