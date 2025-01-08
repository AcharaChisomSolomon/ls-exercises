def is_odd(number):
    if number < 0:
        number *= -1

    return number % 2 != 0

print(is_odd(11))
print(is_odd(12))
print(is_odd(-1))
print(is_odd(-4))