def halvsies(arr):
    if len(arr) == 0:
        return [[], []]
    if len(arr) == 1:
        return [arr[0:], []]
    
    id = len(arr) // 2
    if len(arr) % 2 == 0:
        return [arr[:id], arr[id:]]
    else:
        return [arr[:id + 1], arr[id + 1:]]
    
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])