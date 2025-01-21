def multiply_list(l1, l2):
    return [a * b for (a, b) in list(zip(l1, l2))]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True