# lambda creates an unnamed function
# format:
# lambda arg, arg, arg : return value

sum_1 = lambda x, y : x + y
print("Sum:", sum_1(4, 5))

# can use ternery operator to determine return value
can_vote = lambda age: True if age >= 18 else False
print("Can vote?:", can_vote(16))

# can create list of lambda funcs
power_list = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4]

for func in power_list:
    print(func(4))

# can store lambdas in dictionaries
attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("The Attack Missed"))
         }
attack["quick"]()

import random
attack_key = random.choice(list(attack.keys()))
attack[attack_key]()
