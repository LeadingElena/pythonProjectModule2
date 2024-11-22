def calculate_structure_sum(list):
    total_sum = 0
    for element in list:
        if isinstance(element, dict):
            element = dict.items(element)
        if isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element
        else:
            total_sum += calculate_structure_sum(element)
    return total_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

