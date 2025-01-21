def count_occurrences(lst):
    dct = {}

    for value in lst:
        if value in dct:
            dct[value] += 1
        else:
            dct[value] = 1

    for k, v in dct.items():
        print(f"{k} => {v}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2