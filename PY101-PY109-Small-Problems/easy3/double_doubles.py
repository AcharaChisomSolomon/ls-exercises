def is_double(num):
    num_str = str(num)
    length = len(num_str)
    return num_str[:length // 2] == num_str[length // 2:]

def twice(num):
    return num if is_double(num) else num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
