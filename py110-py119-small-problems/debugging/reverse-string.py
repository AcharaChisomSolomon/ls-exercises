def reverse_string(string):
    output = ''

    for char in string:
        output = char + output

    return output

print(reverse_string("hello") == "olleh")