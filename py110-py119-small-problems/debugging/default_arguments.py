def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])  # Output: True
print(append_to_list(2) == [2])  # Output: True