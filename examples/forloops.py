for i in [2, 4, 6, 8, 10]:
    print("i =", i)

# range(x) returns an array of numbers from 0 to x-1
for i in range(5):
    print("i =", i)

# range(x, y) returns numbers from x (inclusive) to y-1
for i in range(2, 5):
    print("i =", i)

# print all odd numbers from 1 - 20

for i in range(1, 21):
    print("{} is odd?: {}".format(i, (i % 2 == 1)))

your_float = input("Enter a float: ")
your_float = float(your_float)
print("Rounded to 2 decimals: {:.2f}".format(your_float))
