# take string of letters with no spaces
# translate it to string of unicodes
# translate it back to the original message

input_str = input("Enter a string: ")
coded_str = ""
reconstructed_str = ""

for char in input_str:
    coded_str += str(ord(char) - 23)

print(coded_str)

# this only works if each char is represented by a two digit number, hence
# shifting standard unicode values down by 23 before storing in coded_str
# to accomodate lower case letters with unicodes 100+
for i in range(0, len(coded_str)-1, 2):
    reconstructed_str += chr(int(coded_str[i] + coded_str[i + 1]) + 23)

print(reconstructed_str)
