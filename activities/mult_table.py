mult_table = [[0] * 9 for i in range(9)]


for i in range(9):
    for j in range(9):
        mult_table[i][j] = (i + 1) * (j + 1)

for i in range(9):
    for j in range(9):
        print(mult_table[i][j], end=", ")
    print()
