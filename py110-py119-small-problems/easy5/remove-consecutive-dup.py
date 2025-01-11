def unique_sequence(lst):
    output = []

    for val in lst:
        if len(output) == 0: 
            output.append(val)

        if output[-1] != val:
            output.append(val)

    return output


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True