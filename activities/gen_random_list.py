# generate a random list of 5 values between 1-9
import random

rand_list = []

for i in range(5):
    new_element = random.randrange(1, 10)
    rand_list.append(new_element)

print("Your Random List:", rand_list)
