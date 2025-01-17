def running_total(lst):
    if len(lst) <= 1:
        return lst
    
    output_lst = [lst[0]]
    for i in range(1, len(lst)):
        output_lst.append(output_lst[-1] + lst[i])

    return output_lst


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True