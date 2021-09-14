balance = float(input("Enter Starting Balance: "))
balance = "{:.2f}".format(balance)
balance = float(balance)

interest_rate = float(input("Enter Interest Rate: "))
interest_rate = interest_rate * .01

for i in range(10):
    balance = float("{:.2f}".format(balance + (balance * interest_rate)))

print("Ending Balance: {}".format(balance))

