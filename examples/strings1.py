# strings can be in single, double, or triple quotes
print(type('3'))
print(type("3"))
print(type('''3'''))

samp_string = "This is a very important string"

print("Length:", len(samp_string))

# reference first char in samp_string
print(samp_string[0])
# reference last char in samp_string
print(samp_string[-1])
# grab slice of samp_string from char 0 (inclusive) to 4 (exclusive)
print(samp_string[0:4])
# a slice from 8 (inclusive) through end of string
print(samp_string[8:])
# from 0 to last char (exclusive) skipping every other char
print(samp_string[0:-1:2])
# reverses characters in string
print(samp_string[::-1])

# concatenation
print("Green " + "eggs")
# repeat a string
print("Hello " * 3)
# convert int to string
num_string = str(4)
# can iterate through string like array with for in, char is just a var name, can be anything
for char in samp_string:
    print(char)
# range returns 0 - (len - 1 exclusive), skipping every other number
# so this prints the string in blocks of two chars, omitting last char for odd len strings
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])
