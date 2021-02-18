def sort_function(element):
    return element[1:]

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort.sort(key=sort_function)
print(list_to_sort)

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
list_to_sort_2.sort(key=sort_function)
print(list_to_sort_2)