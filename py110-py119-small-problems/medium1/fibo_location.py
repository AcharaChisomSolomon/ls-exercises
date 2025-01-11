import sys

def find_fibonacci_index_by_length(count):
    if count > 4300:
        sys.set_int_max_str_digits(count)

    a = 1
    b = 1
    id = 2

    while True:
        c = a + b
        a = b
        b = c
        id += 1

        if len(str(c)) >= count:
            return id

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)