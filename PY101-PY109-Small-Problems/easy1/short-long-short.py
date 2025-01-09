def short_long_short(str1, str2):
    shortest = ''
    longest = ''

    if len(str1) > len(str2):
        longest = str1
        shortest = str2
    else:
        longest = str2
        shortest = str1

    return f"{shortest}{longest}{shortest}"


print(short_long_short('abc', 'defgh'))  # abcdefghabc
print(short_long_short('abcde', 'fgh'))  # fghabcdefgh