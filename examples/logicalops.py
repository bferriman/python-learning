age = int(input("Enter age: "))

if age == 5:
    print("Go to Kindergarten")
elif age > 5 and age <= 17:
    print("Go to Grade {}".format(age - 5))
elif age > 17:
    print("Go to College")
else:
    print("Not a school age")


can_vote = True if age >= 18 else False
