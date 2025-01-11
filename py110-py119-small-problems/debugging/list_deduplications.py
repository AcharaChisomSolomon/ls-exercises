# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list({key:1 for key in data}.keys())
# print(unique_data == [4, 2, 1, 3]) # order not guaranteed

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
seen = set()
unique_data = [x for x in data if not (x in seen or seen.add(x))]
print(unique_data == [4, 2, 1, 3])  # Output: True