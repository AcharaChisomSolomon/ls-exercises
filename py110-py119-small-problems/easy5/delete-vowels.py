def remove_vowels_from_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_list = list(word)
    list_with_removed_vowels = [char 
                                for char in word_list 
                                if char.lower() not in vowels]
    new_word = ''.join(list_with_removed_vowels)
    return new_word

def remove_vowels(words):
    return [remove_vowels_from_word(word) for word in words]


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True