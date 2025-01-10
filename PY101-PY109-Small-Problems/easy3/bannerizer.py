def print_in_box(string):
    length = len(string)
    print(f"+{(length + 2) * '-'}+")
    print(f"|{(length + 2) * ' '}|")
    print(f"| {string} |")
    print(f"|{(length + 2) * ' '}|")
    print(f"+{(length + 2) * '-'}+")

print_in_box('To boldly go where no one has gone before.')
print_in_box('')