num1, num2 = input("Enter two values to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")
# else block executes if no errors are thrown
else:
    print("You didn't raise an exception")
# finally executes if no errors or if there are caught errors, but not if an uncaught error halts execution
finally:
    print("I execute no matter what")