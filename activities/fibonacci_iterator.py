# make a class that returns next value in fibonacci
# sequence each time next is called

class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        next_fib = self.first + self.second
        self.first = self.second
        self.second = next_fib
        return next_fib

my_fib = Fibonacci()
for i in range(10):
    print(next(my_fib))