def is_palindrome(string):
    end_id = -1
    mid = len(string) // 2

    for i in range(mid + 1):
        if string[i] != string[end_id]:
            return False
        end_id -= 1

    return True

def is_real_palindrome(string):
    new_string = ''.join([char.lower() for char in list(string) if char.isalnum()])
    return is_palindrome(new_string)


# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True