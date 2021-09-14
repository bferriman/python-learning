height = int(input("Enter tree height: "))

for i in range(height + 1):
    if i < height:
        num_spaces = height - (i + 1)
        num_hashes = 2 * i + 1
        output = ""
        for j in range(num_spaces):
            output += " "
        for k in range(num_hashes):
            output += "#"
        print(output)
    else:
        num_spaces = height - 1
        num_hashes = 1
        output = ""
        for j in range(num_spaces):
            output += " "
        output += "#"
        print(output)
