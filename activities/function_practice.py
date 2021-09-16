# create func that receives list and func
# passed func will return bool if a list value is odd
# surrounding func will return list of odd numbers

def filter_list(num_data, filter):
    filtered_list = []
    for num in num_data:
        if filter(num):
            filtered_list.append(num)
    return filtered_list

def is_odd(num):
    return num % 2 == 1

test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Filtered data:", filter_list(test_data, is_odd))