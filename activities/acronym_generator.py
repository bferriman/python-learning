# user enters a string
# create an acronym from it by taking the first letter of each word

user_input = input("Enter Your String: ")

input_list = user_input.split()

acronym = ""

for word in input_list:
    acronym += word[0]

acronym = acronym.upper()

print("Your acronym:", acronym)
