def sum_digits(number):
    num_str = str(number)
    total = 0

    for char in num_str:
        total += int(char)

    return total


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True