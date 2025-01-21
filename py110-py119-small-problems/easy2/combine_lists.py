def interleave(a1, a2):
    output = []

    for i in range(len(a1)):
        output.append(a1[i])
        output.append(a2[i])

    return output


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True