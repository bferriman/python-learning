# drink = input("Pick One (Coke or Pepsi): ")
# if drink == "Coke":
#     print("Here is your Coke")
# elif drink == "Pepsi":
#     print("Here is your Pepsi")
# else:
#     print("Here's a water")

num_1, operator, num_2 = input("Enter Equation: ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 + num_2))
elif operator == "-":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 - num_2))
elif operator == "*":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 * num_2))
elif operator == "/":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 / num_2))
elif operator == "%":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 % num_2))
else:
    print("Inappropriate Input")
