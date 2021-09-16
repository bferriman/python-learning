# multidimenstional lists and list comprehensions

multi_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([col[1] for col in multi_list])

print([multi_list[i][i] for i in range(len(multi_list))])