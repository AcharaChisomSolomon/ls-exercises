def is_palindrome(string):
    end_id = -1
    mid = len(string) // 2

    for i in range(mid + 1):
        if string[i] != string[end_id]:
            return False
        end_id -= 1

    return True


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)