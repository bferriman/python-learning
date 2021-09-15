def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num_results = int(input("How many fibonacci numbers do you want to see? : "))

for n in range(num_results):
    print("Fibonacci", n + 1, ":", fibonacci(n + 1))