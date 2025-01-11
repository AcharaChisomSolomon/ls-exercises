from rotations_2 import rotate_rightmost_digits

def max_rotation(number):
    current_rotation = number

    for i in range(len(str(number)), 0, -1):
        current_rotation = rotate_rightmost_digits(current_rotation, i)

    return current_rotation


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True