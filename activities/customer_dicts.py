customers = []

while True:
    c_name = input("Enter Customer Name : ")
    customers.append({"name": c_name})
    user_continue = input("Enter Customer (Yes/No) : ")
    user_continue = user_continue[0].lower()
    if user_continue != "y":
        break

for cust in customers:
    print(cust["name"])