# A generator function returns a result generator 
# whenever it's called.
# They can be suspended and resumed during execution.
# We use these when we want a huge result set but don't
# want to slow down the program by creating it all
# at once.

# generator that calculates primes and returns the next
# prime on command

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):
        if is_prime(num1):
            yield num1
        # yield ^^ is what makes this a generator function
        # calling next will return the next result

prime = gen_primes(50)
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))