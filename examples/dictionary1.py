car_dict = {
    "make": "Honda",
    "model": "Civic",
    "year": 2007
}

print("My car is a", car_dict["make"], car_dict["model"])

car_dict["model"] = "Pilot"

print("My car is now a", car_dict["make"], car_dict["model"])

car_dict["milage"] = 112376
# check for existence of a key in a dictionary
print("Is there a year:", "year" in car_dict)
print(car_dict.values())
print(car_dict.keys())
for k, v in car_dict.items():
    print(k, v)
# print value of "color" key if found, otherwise print message
print(car_dict.get("color", "no color attribute found"))
# delete a key value pair
del car_dict["milage"]
# print all keys (not values)
for i in car_dict:
    print(i)
# delete all items in dictionary
car_dict.clear()

employees = []
f_name, l_name = input("Enter Employee Name: ").split()
employees.append({"f_name": f_name, "l_name": l_name})
print(employees)