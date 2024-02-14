def flatten(lst):
    flattened_list = []
    for item in lst:
        if type(item)==list:
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list

lis = [1, 2, 3, ['x', 'y', 'x'], [[5, 3, 6], [3, 4, 8, ['x', 'x', 'x']]]]
result = flatten(lis)
print(result)
